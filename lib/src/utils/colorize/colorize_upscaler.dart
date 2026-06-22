import 'dart:async';
import 'dart:io';
import 'dart:math' as math;
import 'dart:typed_data';
import 'dart:ui' as ui;

import 'package:flutter/foundation.dart';
import 'package:image/image.dart' as img;
import 'package:onnxruntime_v2/onnxruntime_v2.dart';

import 'lab_color.dart';

/// 上色任务参数
class ColorizeParams {
  final String inputPath;
  final String outputPath;
  final String modelPath;
  final ColorizeModelType modelType;
  final int? threads;
  final String? inputName;
  final String? outputName;

  const ColorizeParams({
    required this.inputPath,
    required this.outputPath,
    required this.modelPath,
    required this.modelType,
    this.threads,
    this.inputName,
    this.outputName,
  });
}

/// 上色模型类型
enum ColorizeModelType { ddcolor, deoldify }

/// ONNX Session 缓存（避免每次重新加载模型）
class _OrtSessionCache {
  final OrtSession session;
  final String modelPath;
  _OrtSessionCache(this.session, this.modelPath);
}

final Map<String, _OrtSessionCache> _sessionCache = {};
bool _providersLogged = false;

/// 尝试用 image 包解码，如果失败则尝试用 dart:ui 解码（支持 WebP）
Future<img.Image?> _decodeImage(Uint8List bytes) async {
  img.Image? result = img.decodeImage(bytes);
  if (result != null) return result;

  try {
    final codec = await ui.instantiateImageCodec(bytes);
    final frameInfo = await codec.getNextFrame();
    final ui.Image decoded = frameInfo.image;
    final ByteData? byteData = await decoded.toByteData(format: ui.ImageByteFormat.rawRgba);
    if (byteData != null) {
      Uint8List rgbaBytes = byteData.buffer.asUint8List();
      result = img.Image.fromBytes(
        width: decoded.width,
        height: decoded.height,
        bytes: rgbaBytes.buffer,
        bytesOffset: rgbaBytes.offsetInBytes,
        numChannels: 4,
      );
    }
    decoded.dispose();
    codec.dispose();
    return result;
  } catch (e) {
    debugPrint('Failed to decode image with dart:ui: $e');
    return null;
  }
}

/// ONNX Runtime 环境初始化标志
bool _ortEnvInitialized = false;

/// 确保 ONNX Runtime 环境已初始化
void _ensureOrtEnvInitialized() {
  if (!_ortEnvInitialized) {
    try {
      OrtEnv.instance.init();
      _ortEnvInitialized = true;
    } catch (e) {
      debugPrint('ONNX Env init error (may already initialized): $e');
      _ortEnvInitialized = true;
    }
  }
}

/// 获取或创建 ONNX Session（带缓存）
Future<OrtSession> _getOrCreateSession(
  String modelPath,
  int numThreads,
) async {
  final cacheKey = '$modelPath:$numThreads';
  final cached = _sessionCache[cacheKey];
  if (cached != null) {
    return cached.session;
  }

  final sessionOptions = OrtSessionOptions();
  try {
    sessionOptions.setIntraOpNumThreads(numThreads);
    // 关键：启用ortParallel模式以利用多线程
    sessionOptions.setSessionExecutionMode(OrtSessionExecutionMode.ortParallel);
    // 关键：启用所有图优化
    sessionOptions.setSessionGraphOptimizationLevel(GraphOptimizationLevel.ortEnableAll);

    // 尝试启用硬件加速 (NNAPI for Android, CoreML for iOS)
    try {
      sessionOptions.appendDefaultProviders();
      debugPrint('ONNX: Default providers appended (NNAPI/CoreML/XNNPACK)');
    } catch (e) {
      debugPrint('ONNX: Failed to append default providers: $e');
    }

    if (!_providersLogged) {
      _providersLogged = true;
      try {
        final providers = OrtEnv.instance.availableProviders();
        debugPrint('ONNX available providers: $providers');
      } catch (e) {
        debugPrint('ONNX availableProviders error: $e');
      }
    }
  } catch (e) {
    debugPrint('SessionOptions config warning: $e');
  }

  final Uint8List modelBytes = await File(modelPath).readAsBytes();
  final session = OrtSession.fromBuffer(modelBytes, sessionOptions);
  _sessionCache[cacheKey] = _OrtSessionCache(session, modelPath);
  return session;
}

/// 释放所有缓存的 session
void releaseAllSessions() {
  for (final cache in _sessionCache.values) {
    try {
      cache.session.release();
    } catch (e) {
      debugPrint('Session release error: $e');
    }
  }
  _sessionCache.clear();
}

/// 让出主线程（让UI有机会刷新）
Future<void> _yieldToUI() async {
  await Future<void>.delayed(Duration.zero);
}

/// 图像上色引擎（Dart 原生，基于 ONNX Runtime + image 包）
///
/// 移植自 colorize.py，支持 DDColor 和 DeOldify 两种模型
class ColorizeUpscaler {
  /// 执行 DDColor 上色
  static Future<bool> colorizeDDColor(ColorizeParams params) async {
    try {
      _ensureOrtEnvInitialized();

      debugPrint('DDColor: Reading image from ${params.inputPath}');
      final Uint8List inputBytes = await File(params.inputPath).readAsBytes();
      debugPrint('DDColor: Image size ${inputBytes.length} bytes');

      final img.Image? decodedImage = await _decodeImage(inputBytes);
      if (decodedImage == null) {
        debugPrint('DDColor: Failed to decode image');
        return false;
      }
      debugPrint('DDColor: Decoded image ${decodedImage.width}x${decodedImage.height}');

      await _yieldToUI();

      // 预缩放: 如果原图过大，先缩小到长边 <= 1024
      const int maxSide = 1024;
      img.Image srcImage = decodedImage;
      if (decodedImage.width > maxSide || decodedImage.height > maxSide) {
        final double scale = maxSide / (decodedImage.width > decodedImage.height ? decodedImage.width : decodedImage.height);
        final int newW = (decodedImage.width * scale).round();
        final int newH = (decodedImage.height * scale).round();
        debugPrint('DDColor: Pre-scaling to ${newW}x${newH}');
        // 在 isolate 中执行 resize
        srcImage = await compute(_resizeImage, {
          'image': decodedImage,
          'width': newW,
          'height': newH,
        });
      }

      final int origWidth = srcImage.width;
      final int origHeight = srcImage.height;
      final int origPixels = origWidth * origHeight;
      final Uint8List srcBytes = srcImage.buffer.asUint8List();

      const int modelSize = 256;
      // 在 isolate 中执行模型输入 resize
      final img.Image resized = await compute(_resizeImage, {
        'image': srcImage,
        'width': modelSize,
        'height': modelSize,
      });
      final Uint8List resizedBytes = resized.buffer.asUint8List();

      await _yieldToUI();

      // 直接构造 nchwInput - 不需要 LAB 来回转换
      // DDColor 期望输入是 LAB 转换后的 RGB 灰度图 (1, 3, 256, 256)
      // 简单方案: 直接将灰度图作为三通道输入
      final Float32List nchwInput = Float32List(1 * 3 * modelSize * modelSize);

      // 在 isolate 中构造灰度三通道
      final Float32List inputData = await compute(_toGrayscaleFloat32NCHW, {
        'rgbaBytes': resizedBytes,
        'modelSize': modelSize,
      });
      nchwInput.setAll(0, inputData);

      await _yieldToUI();

      // ONNX 推理 - 使用缓存的 session
      debugPrint('DDColor: Getting session for ${params.modelPath}');
      final session = await _getOrCreateSession(
        params.modelPath,
        params.threads ?? 2,
      );
      debugPrint('DDColor: Session input names: ${session.inputNames}');

      final String inputName = params.inputName ?? session.inputNames[0];
      final inputOrt = OrtValueTensor.createTensorWithDataList(
        nchwInput.toList(growable: false),
        [1, 3, modelSize, modelSize],
      );
      debugPrint('DDColor: Input tensor created');

      final runOptions = OrtRunOptions();
      debugPrint('DDColor: Starting inference...');

      final result = session.runAsync(runOptions, {inputName: inputOrt});
      if (result == null) {
        debugPrint('DDColor: runAsync returned null');
        inputOrt.release();
        runOptions.release();
        return false;
      }

      final outputs = await result.timeout(
        const Duration(seconds: 120),
        onTimeout: () {
          debugPrint('DDColor: Inference timeout after 120 seconds');
          throw TimeoutException('ONNX推理超时(120秒)，可能模型较大或设备性能不足');
        },
      );
      debugPrint('DDColor: Inference completed');

      // 关键：释放输入tensor和runOptions
      inputOrt.release();
      runOptions.release();

      final OrtValue? outputOrt = _extractFirstOutput(outputs);
      if (outputOrt == null) {
        debugPrint('DDColor: output is null');
        for (final o in outputs ?? []) {
          o?.release();
        }
        return false;
      }

      await _yieldToUI();

      // 关键：outputOrt.value 是同步 FFI 复制，对大输出可能耗时
      // 在主 isolate 上完成（无法放到 compute 中，因为 OrtValue 不能跨 isolate）
      final dynamic outputValue = outputOrt.value;
      outputOrt.release();

      if (outputValue == null) {
        debugPrint('DDColor: output value is null');
        return false;
      }

      // 解析输出并 resize - 在 isolate 中完成
      final Float32List outputFlat = await compute(_parseFloat32List, {
        'data': outputValue as List<dynamic>,
      });

      const int outH = 256;
      const int outW = 256;
      final int origPixelsValue = origPixels;

      // 在 isolate 中完成 AB resize 和 LAB 合成
      final Uint8List resultBytes = await compute(_ddcolorPostProcess, {
        'outputFlat': outputFlat,
        'srcBytes': srcBytes,
        'origWidth': origWidth,
        'origHeight': origHeight,
        'outW': outW,
        'outH': outH,
      });

      await File(params.outputPath).writeAsBytes(resultBytes);

      debugPrint('DDColor: Success, saved to ${params.outputPath}');
      return true;
    } catch (e, st) {
      debugPrint('DDColor colorization failed: $e\n$st');
      return false;
    }
  }

  /// 执行 DeOldify 上色
  static Future<bool> colorizeDeOldify(ColorizeParams params) async {
    try {
      _ensureOrtEnvInitialized();

      debugPrint('DeOldify: Reading image from ${params.inputPath}');
      final Uint8List inputBytes = await File(params.inputPath).readAsBytes();
      debugPrint('DeOldify: Image size ${inputBytes.length} bytes');

      final img.Image? decodedImage = await _decodeImage(inputBytes);
      if (decodedImage == null) {
        debugPrint('DeOldify: Failed to decode image');
        return false;
      }
      debugPrint('DeOldify: Decoded image ${decodedImage.width}x${decodedImage.height}');

      await _yieldToUI();

      const int maxSide = 1024;
      img.Image srcImage = decodedImage;
      if (decodedImage.width > maxSide || decodedImage.height > maxSide) {
        final double scale = maxSide / (decodedImage.width > decodedImage.height ? decodedImage.width : decodedImage.height);
        final int newW = (decodedImage.width * scale).round();
        final int newH = (decodedImage.height * scale).round();
        debugPrint('DeOldify: Pre-scaling to ${newW}x${newH}');
        srcImage = await compute(_resizeImage, {
          'image': decodedImage,
          'width': newW,
          'height': newH,
        });
      }

      final int origWidth = srcImage.width;
      final int origHeight = srcImage.height;
      final Uint8List srcBytes = srcImage.buffer.asUint8List();

      const int modelSize = 256;
      final img.Image resized = await compute(_resizeImage, {
        'image': srcImage,
        'width': modelSize,
        'height': modelSize,
      });
      final Uint8List resizedBytes = resized.buffer.asUint8List();

      await _yieldToUI();

      // 灰度图转 float32 NCHW
      final Float32List nchwInput = await compute(_toGrayscaleFloat32NCHW, {
        'rgbaBytes': resizedBytes,
        'modelSize': modelSize,
      });

      await _yieldToUI();

      // ONNX 推理
      debugPrint('DeOldify: Getting session for ${params.modelPath}');
      final session = await _getOrCreateSession(
        params.modelPath,
        params.threads ?? 2,
      );
      debugPrint('DeOldify: Session input names: ${session.inputNames}');

      final String inputName = params.inputName ?? session.inputNames[0];
      final inputOrt = OrtValueTensor.createTensorWithDataList(
        nchwInput.toList(growable: false),
        [1, 3, modelSize, modelSize],
      );
      debugPrint('DeOldify: Input tensor created');

      final runOptions = OrtRunOptions();
      debugPrint('DeOldify: Starting inference...');

      final result = session.runAsync(runOptions, {inputName: inputOrt});
      if (result == null) {
        debugPrint('DeOldify: runAsync returned null');
        inputOrt.release();
        runOptions.release();
        return false;
      }

      final outputs = await result.timeout(
        const Duration(seconds: 120),
        onTimeout: () {
          debugPrint('DeOldify: Inference timeout after 120 seconds');
          throw TimeoutException('ONNX推理超时(120秒)');
        },
      );
      debugPrint('DeOldify: Inference completed');

      inputOrt.release();
      runOptions.release();

      final OrtValue? outputOrt = _extractFirstOutput(outputs);
      if (outputOrt == null) {
        debugPrint('DeOldify: output is null');
        for (final o in outputs ?? []) {
          o?.release();
        }
        return false;
      }

      await _yieldToUI();

      final dynamic outputValue = outputOrt.value;
      outputOrt.release();

      if (outputValue == null) {
        debugPrint('DeOldify: output value is null');
        return false;
      }

      // 后处理 - 在 isolate 中完成
      final Uint8List resultBytes = await compute(_deoldifyPostProcess, {
        'outputData': outputValue as List<dynamic>,
        'srcBytes': srcBytes,
        'origWidth': origWidth,
        'origHeight': origHeight,
        'modelSize': modelSize,
      });

      await File(params.outputPath).writeAsBytes(resultBytes);

      debugPrint('DeOldify: Success, saved to ${params.outputPath}');
      return true;
    } catch (e, st) {
      debugPrint('DeOldify colorization failed: $e\n$st');
      return false;
    }
  }

  /// 从 runAsync 输出中提取第一个 OrtValue
  static OrtValue? _extractFirstOutput(dynamic outputs) {
    if (outputs == null) return null;
    if (outputs is List) {
      for (var item in outputs) {
        if (item != null) return item as OrtValue;
      }
      return null;
    }
    if (outputs is Map) {
      for (var v in outputs.values) {
        if (v != null) return v as OrtValue;
      }
      return null;
    }
    return null;
  }
}

// =================================================================
// 后台 isolate 工具函数（必须为顶层函数才能在 compute 中使用）
// =================================================================

/// 在 isolate 中缩放图像
img.Image _resizeImage(Map<String, dynamic> args) {
  final img.Image image = args['image'] as img.Image;
  final int width = args['width'] as int;
  final int height = args['height'] as int;
  return img.copyResize(
    image,
    width: width,
    height: height,
    interpolation: img.Interpolation.linear,
  );
}

/// 在 isolate 中将 RGBA 字节转为灰度三通道 NCHW float32
Float32List _toGrayscaleFloat32NCHW(Map<String, dynamic> args) {
  final Uint8List rgbaBytes = args['rgbaBytes'] as Uint8List;
  final int modelSize = args['modelSize'] as int;
  final int pixelCount = modelSize * modelSize;
  final Float32List result = Float32List(1 * 3 * pixelCount);

  for (int i = 0; i < pixelCount; i++) {
    final int gray = rgbaBytes[i * 4];
    // CHW 格式: 通道在前
    result[0 * pixelCount + i] = gray.toDouble();
    result[1 * pixelCount + i] = gray.toDouble();
    result[2 * pixelCount + i] = gray.toDouble();
  }
  return result;
}

/// 在 isolate 中将 List<dynamic> 转为 Float32List
Float32List _parseFloat32List(Map<String, dynamic> args) {
  final List<dynamic> data = args['data'] as List<dynamic>;
  final Float32List result = Float32List(data.length);
  for (int i = 0; i < data.length; i++) {
    result[i] = (data[i] as num).toDouble();
  }
  return result;
}

/// DDColor 后处理（在 isolate 中执行）
/// 1. 解析 AB 通道 (1, 2, 256, 256) -> (256, 256, 2)
/// 2. 提取原图 LAB L 通道
/// 3. resize AB 到原图尺寸
/// 4. 合成 LAB -> RGB
Uint8List _ddcolorPostProcess(Map<String, dynamic> args) {
  final Float32List outputFlat = args['outputFlat'] as Float32List;
  final Uint8List srcBytes = args['srcBytes'] as Uint8List;
  final int origWidth = args['origWidth'] as int;
  final int origHeight = args['origHeight'] as int;
  final int outW = args['outW'] as int;
  final int outH = args['outH'] as int;
  final int origPixels = origWidth * origHeight;

  // 1. 提取原图 L 通道
  final Float32List origL = Float32List(origPixels);
  for (int i = 0; i < origPixels; i++) {
    // srcBytes 是 RGBA，取 R 作为亮度
    origL[i] = srcBytes[i * 4] / 255.0;
  }

  // 2. CHW -> HWC: (1, 2, 256, 256) -> 2x(256, 256)
  final Float32List abA = Float32List(outH * outW);
  final Float32List abB = Float32List(outH * outW);
  for (int i = 0; i < outH * outW; i++) {
    abA[i] = outputFlat[0 * outH * outW + i];
    abB[i] = outputFlat[1 * outH * outW + i];
  }

  // 3. resize AB 到原图尺寸 (双线性插值)
  final Float32List resizedA = _resizePlanarBilinear(abA, outW, outH, origWidth, origHeight);
  final Float32List resizedB = _resizePlanarBilinear(abB, outW, outH, origWidth, origHeight);

  // 4. LAB -> RGB (简化版: 直接用 L*gray + AB*color)
  // DDColor 输出 AB 是 [-1, 1] 范围，需要映射到 [-128, 128] 再用 cv2.Lab2BGR
  final Uint8List result = Uint8List(origPixels * 4);
  for (int i = 0; i < origPixels; i++) {
    final double l = origL[i]; // [0, 1]
    final double a = (resizedA[i] * 128.0).clamp(-128.0, 127.0);
    final double b = (resizedB[i] * 128.0).clamp(-128.0, 127.0);

    // 简化的 LAB -> RGB (此为近似实现，与原算法略有差异但视觉效果接近)
    final double lLab = l * 100.0;
    final List<double> bgr = _labToBgrFast(lLab, a, b);

    result[i * 4] = (bgr[2] * 255.0).round().clamp(0, 255);
    result[i * 4 + 1] = (bgr[1] * 255.0).round().clamp(0, 255);
    result[i * 4 + 2] = (bgr[0] * 255.0).round().clamp(0, 255);
    result[i * 4 + 3] = 255;
  }
  return result;
}

/// DeOldify 后处理（在 isolate 中执行）
/// 1. CHW -> HWC RGB
/// 2. resize 到原图尺寸
/// 3. Gaussian blur
/// 4. 提取原图 L 通道
/// 5. 合成 LAB -> RGB
Uint8List _deoldifyPostProcess(Map<String, dynamic> args) {
  final List<dynamic> outputData = args['outputData'] as List<dynamic>;
  final Uint8List srcBytes = args['srcBytes'] as Uint8List;
  final int origWidth = args['origWidth'] as int;
  final int origHeight = args['origHeight'] as int;
  final int modelSize = args['modelSize'] as int;

  // 1. CHW -> HWC RGB
  final int pixelCount = modelSize * modelSize;
  final img.Image colorized256 = img.Image(width: modelSize, height: modelSize, numChannels: 4);
  final Uint8List c256Bytes = colorized256.buffer.asUint8List();
  for (int i = 0; i < pixelCount; i++) {
    c256Bytes[i * 4] = (outputData[0 * pixelCount + i] as num).round().clamp(0, 255);
    c256Bytes[i * 4 + 1] = (outputData[1 * pixelCount + i] as num).round().clamp(0, 255);
    c256Bytes[i * 4 + 2] = (outputData[2 * pixelCount + i] as num).round().clamp(0, 255);
    c256Bytes[i * 4 + 3] = 255;
  }

  // 2. resize 回原图
  final img.Image colorizedFull = img.copyResize(
    colorized256,
    width: origWidth,
    height: origHeight,
    interpolation: img.Interpolation.linear,
  );

  // 3. 高斯模糊
  final img.Image colorizedBlurred = img.gaussianBlur(colorizedFull, radius: 6);
  final Uint8List cbBytes = colorizedBlurred.buffer.asUint8List();

  // 4. 提取原图 L (用 R 通道)
  final int origPixels = origWidth * origHeight;
  final Uint8List result = Uint8List(origPixels * 4);
  for (int i = 0; i < origPixels; i++) {
    final int lVal = srcBytes[i * 4]; // 0-255

    // 上色图的 LAB 通道
    final double bInput = cbBytes[i * 4 + 2] / 255.0;
    final double gInput = cbBytes[i * 4 + 1] / 255.0;
    final double rInput = cbBytes[i * 4] / 255.0;

    final List<double> lab = _bgrToLabFast(bInput, gInput, rInput);

    // 用原图的 L 替换上色图的 L
    final double lStd = lVal * 100.0 / 255.0;
    final List<double> bgr = _labToBgrFast(lStd, lab[1], lab[2]);

    result[i * 4] = (bgr[2] * 255.0).round().clamp(0, 255);
    result[i * 4 + 1] = (bgr[1] * 255.0).round().clamp(0, 255);
    result[i * 4 + 2] = (bgr[0] * 255.0).round().clamp(0, 255);
    result[i * 4 + 3] = 255;
  }
  return result;
}

/// 双线性插值
Float32List _resizePlanarBilinear(
  Float32List src,
  int srcW,
  int srcH,
  int dstW,
  int dstH,
) {
  final Float32List dst = Float32List(dstW * dstH);
  final double scaleX = srcW / dstW;
  final double scaleY = srcH / dstH;
  for (int y = 0; y < dstH; y++) {
    for (int x = 0; x < dstW; x++) {
      final double sx = (x + 0.5) * scaleX - 0.5;
      final double sy = (y + 0.5) * scaleY - 0.5;

      final int x0 = sx.floor().clamp(0, srcW - 1);
      final int y0 = sy.floor().clamp(0, srcH - 1);
      final int x1 = (x0 + 1).clamp(0, srcW - 1);
      final int y1 = (y0 + 1).clamp(0, srcH - 1);

      final double fx = (sx - x0).clamp(0.0, 1.0);
      final double fy = (sy - y0).clamp(0.0, 1.0);

      final double v00 = src[y0 * srcW + x0];
      final double v10 = src[y0 * srcW + x1];
      final double v01 = src[y1 * srcW + x0];
      final double v11 = src[y1 * srcW + x1];

      final double v0 = v00 * (1 - fx) + v10 * fx;
      final double v1 = v01 * (1 - fx) + v11 * fx;
      dst[y * dstW + x] = v0 * (1 - fy) + v1 * fy;
    }
  }
  return dst;
}

/// 简化的 BGR [0,1] -> LAB
List<double> _bgrToLabFast(double b, double g, double r) {
  // sRGB -> linear
  double lr = r <= 0.04045 ? r / 12.92 : _pow((r + 0.055) / 1.055, 2.4);
  double lg = g <= 0.04045 ? g / 12.92 : _pow((g + 0.055) / 1.055, 2.4);
  double lb = b <= 0.04045 ? b / 12.92 : _pow((b + 0.055) / 1.055, 2.4);

  // linear RGB -> XYZ (D65)
  final double x = 0.412453 * lr + 0.357580 * lg + 0.180423 * lb;
  final double y = 0.212671 * lr + 0.715160 * lg + 0.072169 * lb;
  final double z = 0.019334 * lr + 0.119193 * lg + 0.950227 * lb;

  // XYZ -> LAB
  const double xn = 0.95047, yn = 1.0, zn = 1.08883;
  const double epsilon = 216.0 / 24389.0;
  const double kappa = 24389.0 / 27.0;

  double f(double t) => t > epsilon ? _pow(t, 1.0 / 3.0) : (kappa * t + 16.0) / 116.0;
  final double fx = f(x / xn), fy = f(y / yn), fz = f(z / zn);

  return [
    116.0 * fy - 16.0,
    500.0 * (fx - fy),
    200.0 * (fy - fz),
  ];
}

/// 简化的 LAB -> BGR [0,1]
List<double> _labToBgrFast(double l, double a, double b) {
  const double xn = 0.95047, yn = 1.0, zn = 1.08883;
  const double epsilon = 216.0 / 24389.0;
  const double kappa = 24389.0 / 27.0;

  final double fy = (l + 16.0) / 116.0;
  final double fx = a / 500.0 + fy;
  final double fz = fy - b / 200.0;

  double fInv(double t) {
    final double t3 = t * t * t;
    return t3 > epsilon ? t3 : (116.0 * t - 16.0) / kappa;
  }

  final double x = fInv(fx) * xn;
  final double y = fInv(fy) * yn;
  final double z = fInv(fz) * zn;

  // XYZ -> linear RGB
  double lr = (3.240479 * x - 1.537150 * y - 0.498535 * z).clamp(0.0, 1.0);
  double lg = (-0.969256 * x + 1.875992 * y + 0.041556 * z).clamp(0.0, 1.0);
  double lb = (0.055648 * x - 0.204043 * y + 1.057311 * z).clamp(0.0, 1.0);

  // linear -> sRGB
  double toSrgb(double c) => c <= 0.0031308 ? 12.92 * c : 1.055 * _pow(c, 1.0 / 2.4) - 0.055;
  return [toSrgb(lb), toSrgb(lg), toSrgb(lr)];
}

double _pow(double base, double exp) {
  if (base <= 0) return 0;
  return math.pow(base, exp).toDouble();
}
