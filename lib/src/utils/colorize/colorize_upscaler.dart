import 'dart:async';
import 'dart:io';
import 'dart:isolate';
import 'dart:math' as math;
import 'dart:typed_data';
import 'dart:ui' as ui;

import 'package:flutter/foundation.dart';
import 'package:image/image.dart' as img;
import 'package:onnxruntime_v2/onnxruntime_v2.dart';

/// 上色任务参数（仅含可跨 Isolate 传递的原始类型）
class ColorizeParams {
  final String inputPath;
  final String outputPath;
  final String modelPath;
  final ColorizeModelType modelType;
  final int threads;
  final String? inputName;
  final String? outputName;

  const ColorizeParams({
    required this.inputPath,
    required this.outputPath,
    required this.modelPath,
    required this.modelType,
    int? threads,
    this.inputName,
    this.outputName,
  }) : threads = threads ?? 2;

  Map<String, dynamic> toJson() => {
        'inputPath': inputPath,
        'outputPath': outputPath,
        'modelPath': modelPath,
        'modelType': modelType.index,
        'threads': threads,
        'inputName': inputName,
        'outputName': outputName,
      };

  factory ColorizeParams.fromJson(Map<String, dynamic> json) => ColorizeParams(
        inputPath: json['inputPath'] as String,
        outputPath: json['outputPath'] as String,
        modelPath: json['modelPath'] as String,
        modelType: ColorizeModelType.values[json['modelType'] as int],
        threads: json['threads'] as int,
        inputName: json['inputName'] as String?,
        outputName: json['outputName'] as String?,
      );
}

enum ColorizeModelType { ddcolor, deoldify }

// ========================================================================
// Isolate 入口：整个上色流水线在独立 Isolate 中运行，完全不阻塞 UI
// ========================================================================

/// 在独立 Isolate 中执行一张图片的上色（图像解码已在主 Isolate 完成）。
/// message = {'params': Map, 'width': int, 'height': int, 'bytes': Uint8List}
Future<bool> _colorizeInIsolate(Map<String, dynamic> message) async {
  final ColorizeParams params = ColorizeParams.fromJson(message['params'] as Map<String, dynamic>);
  final int width = message['width'] as int;
  final int height = message['height'] as int;
  final Uint8List rgbaBytes = message['bytes'] as Uint8List;

  try {
    // 1. 构造解码后的 img.Image（纯 Dart，不依赖 dart:ui）
    final img.Image decoded = img.Image.fromBytes(
      width: width,
      height: height,
      bytes: rgbaBytes.buffer,
      bytesOffset: rgbaBytes.offsetInBytes,
      numChannels: 4,
    );

    // 2. 预缩放：限制长边 <= 1024，避免 OOM 和推理过慢
    const int maxSide = 1024;
    img.Image src = decoded;
    if (decoded.width > maxSide || decoded.height > maxSide) {
      final double scale = maxSide /
          (decoded.width > decoded.height ? decoded.width : decoded.height);
      src = img.copyResize(
        decoded,
        width: (decoded.width * scale).round(),
        height: (decoded.height * scale).round(),
        interpolation: img.Interpolation.linear,
      );
    }

    final int origWidth = src.width;
    final int origHeight = src.height;
    final Uint8List srcBytes = src.buffer.asUint8List();

    // 3. 缩放到模型输入尺寸（256）
    const int modelSize = 256;
    final img.Image resized = img.copyResize(
      src,
      width: modelSize,
      height: modelSize,
      interpolation: img.Interpolation.linear,
    );
    final Uint8List resizedBytes = resized.buffer.asUint8List();

    // 4. 构造灰度三通道 NCHW float32 输入
    final Float32List nchwInput = Float32List(1 * 3 * modelSize * modelSize);
    for (int i = 0; i < modelSize * modelSize; i++) {
      final double gray = resizedBytes[i * 4].toDouble();
      nchwInput[i] = gray;
      nchwInput[modelSize * modelSize + i] = gray;
      nchwInput[2 * modelSize * modelSize + i] = gray;
    }

    // 5. ONNX 推理（此 isolate 内完成，不跨 Isolate 传递任何 Ort* 对象）
    final Float32List outputFlat;
    OrtSession? session;
    OrtValueTensor? inputOrt;
    OrtRunOptions? runOptions;

    try {
      OrtEnv.instance.init();

      final sessionOptions = OrtSessionOptions();
      try {
        sessionOptions.setIntraOpNumThreads(params.threads);
        sessionOptions.setSessionExecutionMode(OrtSessionExecutionMode.ortParallel);
        sessionOptions.setSessionGraphOptimizationLevel(GraphOptimizationLevel.ortEnableAll);

        // 启用 NNAPI / CoreML / XNNPACK 等硬件加速
        try {
          sessionOptions.appendDefaultProviders();
        } catch (_) {
          // 某些平台可能不支持，忽略即可
        }
      } catch (_) {
        // 即使 options 设置失败，也继续尝试推理
      }

      final Uint8List modelBytes = await File(params.modelPath).readAsBytes();
      session = OrtSession.fromBuffer(modelBytes, sessionOptions);

      final String inputName = params.inputName ?? session.inputNames[0];
      inputOrt = OrtValueTensor.createTensorWithDataList(
        nchwInput.toList(growable: false),
        [1, 3, modelSize, modelSize],
      );

      runOptions = OrtRunOptions();
      final result = session.runAsync(runOptions, {inputName: inputOrt});

      final dynamic outputs;
      if (result is Future) {
        outputs = await result.timeout(
          const Duration(seconds: 120),
          onTimeout: () => throw TimeoutException('ONNX inference timeout (120s)'),
        );
      } else {
        outputs = result;
      }

      final OrtValue? outputOrt = _extractFirstOutput(outputs);
      if (outputOrt == null) {
        debugPrint('colorizeInIsolate: model output is null');
        return false;
      }

      // 提取数值——FFI，必须在同一 Isolate 中读取
      final dynamic rawValue = outputOrt.value;
      try {
        outputOrt.release();
      } catch (_) {}

      if (rawValue == null) {
        debugPrint('colorizeInIsolate: model output.value is null');
        return false;
      }

      // 将嵌套 List/double 展平为 Float32List
      outputFlat = _flattenToFloat32List(rawValue);
    } finally {
      // 推理完成后立刻释放所有 ONNX 资源，防止 FFI 句柄泄漏
      try {
        inputOrt?.release();
      } catch (_) {}
      try {
        runOptions?.release();
      } catch (_) {}
      try {
        session?.release();
      } catch (_) {}
    }

    // 6. 后处理 + 保存图像
    final Uint8List pngBytes;
    if (params.modelType == ColorizeModelType.ddcolor) {
      pngBytes = img.encodePng(_ddcolorPostProcessImage(
        outputFlat,
        srcBytes,
        origWidth,
        origHeight,
      ));
    } else {
      pngBytes = img.encodePng(_deoldifyPostProcessImage(
        outputFlat,
        srcBytes,
        origWidth,
        origHeight,
        modelSize,
      ));
    }

    await File(params.outputPath).writeAsBytes(pngBytes);
    return true;
  } catch (e, st) {
    debugPrint('colorizeInIsolate failed: $e\n$st');
    return false;
  }
}

// ========================================================================
// 对外 API
// ========================================================================

class ColorizeUpscaler {
  /// 执行 DDColor 上色（在独立 Isolate 中运行，不阻塞 UI）。
  static Future<bool> colorizeDDColor(ColorizeParams params) async {
    assert(params.modelType == ColorizeModelType.ddcolor);
    return await _runColorizeInIsolate(params);
  }

  /// 执行 DeOldify 上色（在独立 Isolate 中运行，不阻塞 UI）。
  static Future<bool> colorizeDeOldify(ColorizeParams params) async {
    assert(params.modelType == ColorizeModelType.deoldify);
    return await _runColorizeInIsolate(params);
  }

  /// 统一入口：在主 Isolate 用 dart:ui 解码图像（支持 webp），
  /// 然后把 RGBA bytes 传到后台 Isolate 完成 ONNX 推理与后处理。
  ///
  /// 注意：dart:ui 的 API 在后台 Isolate 不可用，必须在主 Isolate 调用。
  static Future<bool> _runColorizeInIsolate(ColorizeParams params) async {
    try {
      // 1. 主 Isolate：读取 + 解码（dart:ui 仅在此可用）
      final Uint8List inputBytes = await File(params.inputPath).readAsBytes();
      final img.Image? decoded = await _decodeImage(inputBytes);
      if (decoded == null) {
        debugPrint('colorize: failed to decode image ${params.inputPath}');
        return false;
      }
      final Uint8List rgbaBytes = decoded.buffer.asUint8List();

      // 2. 后台 Isolate：所有耗时逻辑（缩放、ONNX 推理、LAB 合成）
      final message = <String, dynamic>{
        'params': params.toJson(),
        'width': decoded.width,
        'height': decoded.height,
        'bytes': rgbaBytes,
      };

      return await Isolate.run(
        () => _colorizeInIsolate(message),
        debugName: 'colorize_${params.modelType.name}',
      );
    } catch (e, st) {
      debugPrint('Isolate.run failed: $e\n$st');
      return false;
    }
  }
}

/// 旧 API 兼容（仅释放 session 缓存——Isolate 模式下其实无缓存，保留空实现以避免编译报错）
void releaseAllSessions() {}

// ========================================================================
// 工具函数（纯 Dart，无 FFI，跨 Isolate 安全）
// ========================================================================

Future<img.Image?> _decodeImage(Uint8List bytes) async {
  // 优先用 image 包（纯 Dart，速度快）
  final img.Image? fromPackage = img.decodeImage(bytes);
  if (fromPackage != null) return fromPackage;

  // 否则用 dart:ui 解码（支持 webp / heic 等格式）
  try {
    final ui.Codec codec = await ui.instantiateImageCodec(bytes);
    final ui.FrameInfo frame = await codec.getNextFrame();
    final ui.Image image = frame.image;

    final ByteData? byteData = await image.toByteData(
      format: ui.ImageByteFormat.rawRgba,
    );
    if (byteData == null) {
      image.dispose();
      codec.dispose();
      return null;
    }

    final Uint8List rgba = byteData.buffer.asUint8List(
      byteData.offsetInBytes,
      byteData.lengthInBytes,
    );
    final img.Image result = img.Image.fromBytes(
      width: image.width,
      height: image.height,
      bytes: rgba.buffer,
      bytesOffset: rgba.offsetInBytes,
      numChannels: 4,
    );

    image.dispose();
    codec.dispose();
    return result;
  } catch (e) {
    debugPrint('dart:ui decode failed: $e');
    return null;
  }
}

OrtValue? _extractFirstOutput(dynamic outputs) {
  if (outputs == null) return null;
  if (outputs is List) {
    for (final item in outputs) {
      if (item != null) return item as OrtValue;
    }
    return null;
  }
  if (outputs is Map) {
    for (final v in outputs.values) {
      if (v != null) return v as OrtValue;
    }
    return null;
  }
  return null;
}

/// 把任意嵌套的 List<num>/num 展平为 Float32List
Float32List _flattenToFloat32List(dynamic value) {
  final List<double> flat = <double>[];
  void walk(dynamic x) {
    if (x is num) {
      flat.add(x.toDouble());
    } else if (x is List) {
      for (final item in x) {
        walk(item);
      }
    } else if (x is Float32List) {
      flat.addAll(x);
    } else if (x is Iterable<double>) {
      flat.addAll(x);
    } else {
      // 兜底：尝试 toString + 解析，通常不会到这里
      final double? parsed = double.tryParse(x.toString());
      if (parsed != null) flat.add(parsed);
    }
  }

  walk(value);
  return Float32List.fromList(flat);
}

// ============ DDColor 后处理 ============
img.Image _ddcolorPostProcessImage(
  Float32List outputFlat,
  Uint8List srcBytes,
  int origWidth,
  int origHeight,
) {
  const int outH = 256;
  const int outW = 256;

  // LAB A/B 通道双线性 resize 到原图尺寸
  final Float32List srcA = Float32List(outH * outW);
  final Float32List srcB = Float32List(outH * outW);
  for (int i = 0; i < outH * outW; i++) {
    srcA[i] = outputFlat[i];
    srcB[i] = outputFlat[outH * outW + i];
  }

  final Float32List aChannel = _resizePlanarBilinear(srcA, outW, outH, origWidth, origHeight);
  final Float32List bChannel = _resizePlanarBilinear(srcB, outW, outH, origWidth, origHeight);

  // 合成：原图 L + 模型 AB -> BGR -> PNG
  final img.Image result = img.Image(width: origWidth, height: origHeight, numChannels: 4);
  final Uint8List resultBytes = result.buffer.asUint8List();

  for (int i = 0; i < origWidth * origHeight; i++) {
    final double l = srcBytes[i * 4] / 255.0; // 用 R 作为亮度近似
    final double a = (aChannel[i] * 128.0).clamp(-128.0, 127.0);
    final double b = (bChannel[i] * 128.0).clamp(-128.0, 127.0);

    final List<double> bgr = _labToBgrFast(l * 100.0, a, b);

    resultBytes[i * 4] = (bgr[2] * 255.0).round().clamp(0, 255);
    resultBytes[i * 4 + 1] = (bgr[1] * 255.0).round().clamp(0, 255);
    resultBytes[i * 4 + 2] = (bgr[0] * 255.0).round().clamp(0, 255);
    resultBytes[i * 4 + 3] = 255;
  }

  return result;
}

// ============ DeOldify 后处理 ============
img.Image _deoldifyPostProcessImage(
  Float32List outputFlat,
  Uint8List srcBytes,
  int origWidth,
  int origHeight,
  int modelSize,
) {
  // outputFlat 形状应为 [1, 3, modelSize, modelSize]（CHW）
  final img.Image color256 = img.Image(width: modelSize, height: modelSize, numChannels: 4);
  final Uint8List c256 = color256.buffer.asUint8List();
  for (int i = 0; i < modelSize * modelSize; i++) {
    c256[i * 4] = outputFlat[i].clamp(0.0, 255.0).round();
    c256[i * 4 + 1] = outputFlat[modelSize * modelSize + i].clamp(0.0, 255.0).round();
    c256[i * 4 + 2] = outputFlat[2 * modelSize * modelSize + i].clamp(0.0, 255.0).round();
    c256[i * 4 + 3] = 255;
  }

  // 放大到原图尺寸 + 高斯模糊（防止噪声）
  final img.Image colorFull = img.copyResize(
    color256,
    width: origWidth,
    height: origHeight,
    interpolation: img.Interpolation.linear,
  );
  final img.Image colorBlurred = img.gaussianBlur(colorFull, radius: 6);
  final Uint8List cb = colorBlurred.buffer.asUint8List();

  // 用原图的 L 替换上色图的 L（保留原图亮度）
  final img.Image result = img.Image(width: origWidth, height: origHeight, numChannels: 4);
  final Uint8List rb = result.buffer.asUint8List();

  for (int i = 0; i < origWidth * origHeight; i++) {
    final double lStd = srcBytes[i * 4] / 255.0; // 原图亮度

    final double bIn = cb[i * 4 + 2] / 255.0;
    final double gIn = cb[i * 4 + 1] / 255.0;
    final double rIn = cb[i * 4] / 255.0;
    final List<double> lab = _bgrToLabFast(bIn, gIn, rIn);

    final List<double> bgr = _labToBgrFast(lStd * 100.0, lab[1], lab[2]);
    rb[i * 4] = (bgr[2] * 255.0).round().clamp(0, 255);
    rb[i * 4 + 1] = (bgr[1] * 255.0).round().clamp(0, 255);
    rb[i * 4 + 2] = (bgr[0] * 255.0).round().clamp(0, 255);
    rb[i * 4 + 3] = 255;
  }

  return result;
}

// ============ 双线性插值 & LAB 工具 ============
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

List<double> _bgrToLabFast(double b, double g, double r) {
  final double lr = r <= 0.04045 ? r / 12.92 : _pow((r + 0.055) / 1.055, 2.4);
  final double lg = g <= 0.04045 ? g / 12.92 : _pow((g + 0.055) / 1.055, 2.4);
  final double lb = b <= 0.04045 ? b / 12.92 : _pow((b + 0.055) / 1.055, 2.4);

  final double x = 0.412453 * lr + 0.357580 * lg + 0.180423 * lb;
  final double y = 0.212671 * lr + 0.715160 * lg + 0.072169 * lb;
  final double z = 0.019334 * lr + 0.119193 * lg + 0.950227 * lb;

  const double xn = 0.95047, yn = 1.0, zn = 1.08883;
  const double epsilon = 216.0 / 24389.0;
  const double kappa = 24389.0 / 27.0;

  double f(double t) => t > epsilon ? _pow(t, 1.0 / 3.0) : (kappa * t + 16.0) / 116.0;

  final double fx = f(x / xn);
  final double fy = f(y / yn);
  final double fz = f(z / zn);

  return [116.0 * fy - 16.0, 500.0 * (fx - fy), 200.0 * (fy - fz)];
}

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

  final double lr = (3.240479 * x - 1.537150 * y - 0.498535 * z).clamp(0.0, 1.0);
  final double lg = (-0.969256 * x + 1.875992 * y + 0.041556 * z).clamp(0.0, 1.0);
  final double lb = (0.055648 * x - 0.204043 * y + 1.057311 * z).clamp(0.0, 1.0);

  double toSrgb(double c) =>
      c <= 0.0031308 ? 12.92 * c : 1.055 * _pow(c, 1.0 / 2.4) - 0.055;
  return [toSrgb(lb), toSrgb(lg), toSrgb(lr)];
}

double _pow(double base, double exp) {
  if (base <= 0) return 0;
  return math.pow(base, exp).toDouble();
}
