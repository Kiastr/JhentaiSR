import 'dart:io';
import 'dart:typed_data';
import 'dart:ui' as ui;

import 'package:flutter/foundation.dart';
import 'package:image/image.dart' as img;
import 'package:onnxruntime_v2/onnxruntime_v2.dart';

import 'lab_color.dart';

/// 尝试用 image 包解码，如果失败则尝试用 dart:ui 解码（支持 WebP）
img.Image? _decodeImage(Uint8List bytes) {
  img.Image? result = img.decodeImage(bytes);
  if (result != null) return result;

  try {
    ui.Image decoded = ui.decodeImageFromListSync(bytes);
    ByteData? byteData = decoded.toByteData(format: ui.ImageByteFormat.rawRgba);
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
    return result;
  } catch (e) {
    debugPrint('Failed to decode image with dart:ui: $e');
    return null;
  }
}

/// 上色模型类型
enum ColorizeModelType {
  deoldify,
  ddcolor,
}

/// 上色推理参数
class ColorizeParams {
  final String inputPath;
  final String outputPath;
  final String modelPath;
  final ColorizeModelType modelType;
  final int threads;

  ColorizeParams({
    required this.inputPath,
    required this.outputPath,
    required this.modelPath,
    required this.modelType,
    this.threads = 2,
  });
}

/// ==================== DeOldify / DDColor 上色引擎 ====================
///
/// 精确复现 Python colorize.py 的处理流程：
/// - DeOldify: gray_rgb → resize(256,256) → ONNX 推理 → resize 回原图 → GaussianBlur(13,13)
///   → LAB 分解 → 替换 a,b 通道 → 合成 → RGB
/// - DDColor: BGR float32 → LAB L 通道 → gray_rgb → resize(256,256) → ONNX 推理 ab
///   → resize 回原图 → 与原图 L 合成 → LAB→BGR→RGB
///
/// 输入: 原始图片路径 (通常是灰度漫画)
/// 输出: 上色后的 PNG 图片路径
class ColorizeUpscaler {
  static bool _ortEnvInitialized = false;

  static void _ensureOrtEnvInitialized() {
    if (!_ortEnvInitialized) {
      try {
        OrtEnv.instance.init();
        _ortEnvInitialized = true;
      } catch (e) {
        // 可能已经初始化过，忽略
        _ortEnvInitialized = true;
      }
    }
  }

  /// ==================== DeOldify 上色 ====================
  static Future<bool> colorizeDeOldify(ColorizeParams params) async {
    final String inputPath = params.inputPath;
    final String outputPath = params.outputPath;
    final String modelPath = params.modelPath;
    final int numThreads = params.threads;
    try {
      _ensureOrtEnvInitialized();

      // ============== 读取图像 ==============
      final Uint8List inputBytes = await File(inputPath).readAsBytes();
      final img.Image? srcImage = _decodeImage(inputBytes);
      if (srcImage == null) return false;

      final int origWidth = srcImage.width;
      final int origHeight = srcImage.height;

      // image v4: 使用 buffer.asUint8List() 访问像素数据
      final Uint8List srcBytes = srcImage.buffer.asUint8List();

      // ============== 预处理: resize(256,256) ==============
      // image v4: copyResize 返回新图像，interpolation 使用 Interpolation.linear
      final img.Image resized = img.copyResize(
        srcImage,
        width: 256,
        height: 256,
        interpolation: img.Interpolation.linear,
      );
      final Uint8List resizedBytes = resized.buffer.asUint8List();

      // ============== 构建 NCHW float32 tensor ==============
      final Float32List nchwInput = Float32List(1 * 3 * 256 * 256);
      for (int y = 0; y < 256; y++) {
        for (int x = 0; x < 256; x++) {
          final int srcIdx = (y * 256 + x) * resized.numChannels;
          // image 库是 RGBA/RGB 格式
          final int rVal = resizedBytes[srcIdx];
          final int gVal = resizedBytes[srcIdx + 1];
          final int bVal = resizedBytes[srcIdx + 2];
          // 模型期望 BGR 顺序
          nchwInput[0 * 256 * 256 + y * 256 + x] = bVal.toDouble();
          nchwInput[1 * 256 * 256 + y * 256 + x] = gVal.toDouble();
          nchwInput[2 * 256 * 256 + y * 256 + x] = rVal.toDouble();
        }
      }

      // ============== ONNX 推理 ==============
      OrtSession? session;
      OrtValueTensor? inputOrt;
      OrtRunOptions? runOptions;
      dynamic outputs;

      try {
        final sessionOptions = OrtSessionOptions();
        try {
          sessionOptions.setIntraOpNumThreads(numThreads);
        } catch (_) {}
        try {
          sessionOptions.appendDefaultProviders();
        } catch (_) {
          // GPU provider 不可用时忽略
        }

        // 从文件加载模型
        final Uint8List modelBytes = await File(modelPath).readAsBytes();
        session = OrtSession.fromBuffer(modelBytes, sessionOptions);

        final String inputName = session.inputNames[0];

        inputOrt = OrtValueTensor.createTensorWithDataList(
          nchwInput.toList(growable: false),
          [1, 3, 256, 256],
        );

        runOptions = OrtRunOptions();
        outputs = await session.runAsync(runOptions, {inputName: inputOrt});
      } catch (e) {
        debugPrint('DeOldify ONNX inference error: $e');
        _safeRelease(inputOrt, runOptions, session, outputs);
        return false;
      }

      // 解析输出
      final OrtValue? outputOrt = _extractFirstOutput(outputs);
      if (outputOrt == null) {
        debugPrint('DeOldify output is null');
        _safeRelease(inputOrt, runOptions, session, outputs);
        return false;
      }

      // outputOrt.value 返回 List<double> (float32)
      final dynamic outputValue = outputOrt.value;
      _safeRelease(inputOrt, runOptions, session, outputs);

      if (outputValue == null) {
        debugPrint('DeOldify output value is null');
        return false;
      }

      // DeOldify 模型输出: [1, 3, 256, 256] float32 → shape [3, 256, 256]
      // 从 List<double> 中提取数据
      final List<dynamic> rawData = outputValue as List<dynamic>;
      final Float32List flatOutput = Float32List(rawData.length);
      for (int i = 0; i < rawData.length; i++) {
        flatOutput[i] = (rawData[i] as num).toDouble();
      }

      // ============== 后处理 1: CHW → RGBA uint8 图像 ==============
      // 模型输出 BGR 顺序 [3, 256, 256]
      final int outH = 256;
      final int outW = 256;
      final int outChannels = 4; // RGBA

      final img.Image colorized256 = img.Image(
        width: outW,
        height: outH,
        numChannels: outChannels,
      );
      final Uint8List c256Bytes = colorized256.buffer.asUint8List();
      for (int y = 0; y < outH; y++) {
        for (int x = 0; x < outW; x++) {
          final int pi = y * outW + x;
          final int dstIdx = pi * outChannels;
          // BGR → RGBA
          c256Bytes[dstIdx] = flatOutput[0 * outH * outW + pi].round().clamp(0, 255);
          c256Bytes[dstIdx + 1] = flatOutput[1 * outH * outW + pi].round().clamp(0, 255);
          c256Bytes[dstIdx + 2] = flatOutput[2 * outH * outW + pi].round().clamp(0, 255);
          c256Bytes[dstIdx + 3] = 255;
        }
      }

      // ============== 后处理 2: resize 回原图大小 ==============
      final img.Image colorizedFull = img.copyResize(
        colorized256,
        width: origWidth,
        height: origHeight,
        interpolation: img.Interpolation.linear,
      );
      final Uint8List cfBytes = colorizedFull.buffer.asUint8List();

      // ============== 后处理 3: 高斯模糊 ==============
      // image v4: gaussianBlur(src, radius: int)
      final img.Image colorizedBlurred = img.gaussianBlur(
        colorizedFull,
        radius: 2, // int 类型 (原 radius 2.3 → 近似取 2)
      );
      final Uint8List cbBytes = colorizedBlurred.buffer.asUint8List();

      // ============== 后处理 4: LAB 分解与合成 ==============
      // 提取 target_l (原图 B 通道作为 LAB L uint8)
      final Uint8List targetL = Uint8List(origWidth * origHeight);
      for (int i = 0; i < origWidth * origHeight; i++) {
        targetL[i] = srcBytes[i * srcImage.numChannels + 2]; // B 通道
      }

      // 构造结果图
      final img.Image resultImage = img.Image(
        width: origWidth,
        height: origHeight,
        numChannels: 4,
      );
      final Uint8List resultBytes = resultImage.buffer.asUint8List();

      for (int y = 0; y < origHeight; y++) {
        for (int x = 0; x < origWidth; x++) {
          final int pi = y * origWidth + x;
          final int srcIdx = pi * colorizedBlurred.numChannels;

          // colorizedBlurred 被当做 BGR 图处理 LAB 转换
          // 传入 bgrToLabPixel: b=cbBytes[srcIdx+2], g=cbBytes[srcIdx+1], r=cbBytes[srcIdx]
          double bInput = cbBytes[srcIdx + 2] / 255.0;
          double gInput = cbBytes[srcIdx + 1] / 255.0;
          double rInput = cbBytes[srcIdx] / 255.0;

          final List<double> labPixel = List<double>.filled(3, 0.0);
          bgrToLabPixel(bInput, gInput, rInput, labPixel);

          int aUint8 = (labPixel[1] + 128.0).round().clamp(0, 255);
          int bUint8 = (labPixel[2] + 128.0).round().clamp(0, 255);
          int lVal = targetL[pi];

          double lStd = lVal * 100.0 / 255.0;
          double aStd = aUint8 - 128.0;
          double bStd = bUint8 - 128.0;

          final List<double> bgrBuf = List<double>.filled(3, 0.0);
          labToBgrPixel(lStd, aStd, bStd, bgrBuf);

          final int dstIdx = pi * 4;
          resultBytes[dstIdx] = (bgrBuf[2] * 255.0).round().clamp(0, 255);
          resultBytes[dstIdx + 1] = (bgrBuf[1] * 255.0).round().clamp(0, 255);
          resultBytes[dstIdx + 2] = (bgrBuf[0] * 255.0).round().clamp(0, 255);
          resultBytes[dstIdx + 3] = 255;
        }
      }

      // ============== 保存输出 ==============
      final Uint8List pngBytes = img.encodePng(resultImage);
      await File(outputPath).writeAsBytes(pngBytes);

      return true;
    } catch (e, stack) {
      debugPrint('DeOldify colorization failed: $e');
      debugPrint('Stack: $stack');
      return false;
    }
  }

  /// ==================== DDColor Tiny 上色 ====================
  static Future<bool> colorizeDDColor(ColorizeParams params) async {
    final String inputPath = params.inputPath;
    final String outputPath = params.outputPath;
    final String modelPath = params.modelPath;
    final int numThreads = params.threads;
    try {
      _ensureOrtEnvInitialized();

      final Uint8List inputBytes = await File(inputPath).readAsBytes();
      final img.Image? srcImage = _decodeImage(inputBytes);
      if (srcImage == null) return false;

      final int origWidth = srcImage.width;
      final int origHeight = srcImage.height;
      final Uint8List srcBytes = srcImage.buffer.asUint8List();

      // ============== 提取原图 LAB L 通道 (float32 [0, 100]) ==============
      final Float32List origL = Float32List(origWidth * origHeight);
      final List<double> labPixel = List<double>.filled(3, 0.0);

      for (int i = 0; i < origWidth * origHeight; i++) {
        final int srcIdx = i * srcImage.numChannels;
        double b0 = srcBytes[srcIdx + 2] / 255.0;
        double g0 = srcBytes[srcIdx + 1] / 255.0;
        double r0 = srcBytes[srcIdx] / 255.0;
        bgrToLabPixel(b0, g0, r0, labPixel);
        origL[i] = labPixel[0];
      }

      // ============== resize → (256, 256) ==============
      final img.Image resized = img.copyResize(
        srcImage,
        width: 256,
        height: 256,
        interpolation: img.Interpolation.linear,
      );
      final Uint8List resizedBytes = resized.buffer.asUint8List();

      // ============== img_l: resized → LAB L 通道 float32 [0,100] ==============
      final Float32List imgL = Float32List(256 * 256);
      for (int i = 0; i < 256 * 256; i++) {
        final int srcIdx = i * resized.numChannels;
        double b0 = resizedBytes[srcIdx + 2] / 255.0;
        double g0 = resizedBytes[srcIdx + 1] / 255.0;
        double r0 = resizedBytes[srcIdx] / 255.0;
        bgrToLabPixel(b0, g0, r0, labPixel);
        imgL[i] = labPixel[0];
      }

      // ============== img_gray_lab = (L, 0, 0) → RGB float32 [0,1] ==============
      final List<double> bgrBuf = List<double>.filled(3, 0.0);
      final Float32List grayR = Float32List(256 * 256);
      final Float32List grayG = Float32List(256 * 256);
      final Float32List grayB = Float32List(256 * 256);

      for (int i = 0; i < 256 * 256; i++) {
        labToBgrPixel(imgL[i], 0.0, 0.0, bgrBuf);
        grayR[i] = bgrBuf[2];
        grayG[i] = bgrBuf[1];
        grayB[i] = bgrBuf[0];
      }

      // ============== NCHW [0,1] float32 ==============
      final Float32List nchwInput = Float32List(1 * 3 * 256 * 256);
      for (int y = 0; y < 256; y++) {
        for (int x = 0; x < 256; x++) {
          final int pi = y * 256 + x;
          nchwInput[0 * 256 * 256 + pi] = grayR[pi];
          nchwInput[1 * 256 * 256 + pi] = grayG[pi];
          nchwInput[2 * 256 * 256 + pi] = grayB[pi];
        }
      }

      // ============== ONNX 推理 ==============
      OrtSession? session;
      OrtValueTensor? inputOrt;
      OrtRunOptions? runOptions;
      dynamic outputs;

      try {
        final sessionOptions = OrtSessionOptions();
        try {
          sessionOptions.setIntraOpNumThreads(numThreads);
        } catch (_) {}
        try {
          sessionOptions.appendDefaultProviders();
        } catch (_) {}

        final Uint8List modelBytes = await File(modelPath).readAsBytes();
        session = OrtSession.fromBuffer(modelBytes, sessionOptions);
        final String inputName = session.inputNames[0];

        inputOrt = OrtValueTensor.createTensorWithDataList(
          nchwInput.toList(growable: false),
          [1, 3, 256, 256],
        );

        runOptions = OrtRunOptions();
        outputs = await session.runAsync(runOptions, {inputName: inputOrt});
      } catch (e) {
        debugPrint('DDColor ONNX inference error: $e');
        _safeRelease(inputOrt, runOptions, session, outputs);
        return false;
      }

      final OrtValue? outputOrt = _extractFirstOutput(outputs);
      if (outputOrt == null) {
        debugPrint('DDColor output is null');
        _safeRelease(inputOrt, runOptions, session, outputs);
        return false;
      }

      final dynamic outputValue = outputOrt.value;
      _safeRelease(inputOrt, runOptions, session, outputs);

      if (outputValue == null) {
        debugPrint('DDColor output value is null');
        return false;
      }

      // DDColor 模型输出: [1, 2, 256, 256] float32 → shape [2, 256, 256]
      final List<dynamic> rawData = outputValue as List<dynamic>;
      final Float32List flatOutput = Float32List(rawData.length);
      for (int i = 0; i < rawData.length; i++) {
        flatOutput[i] = (rawData[i] as num).toDouble();
      }

      // ============== 后处理: ab → resize → 与 origL 合成 ==============
      final int outH = 256;
      final int outW = 256;
      final Float32List abA = Float32List(outH * outW);
      final Float32List abB = Float32List(outH * outW);
      for (int y = 0; y < outH; y++) {
        for (int x = 0; x < outW; x++) {
          final int pi = y * outW + x;
          abA[pi] = flatOutput[0 * outH * outW + pi];
          abB[pi] = flatOutput[1 * outH * outW + pi];
        }
      }

      // resize ab 到原图大小 (双线性插值)
      final Float32List abAResized = Float32List(origWidth * origHeight);
      final Float32List abBResized = Float32List(origWidth * origHeight);
      _resizePlanarBilinear(abA, outW, outH, abAResized, origWidth, origHeight);
      _resizePlanarBilinear(abB, outW, outH, abBResized, origWidth, origHeight);

      // ============== LAB → BGR → RGB 保存 ==============
      final img.Image resultImage = img.Image(
        width: origWidth,
        height: origHeight,
        numChannels: 4,
      );
      final Uint8List resultBytes = resultImage.buffer.asUint8List();

      for (int i = 0; i < origWidth * origHeight; i++) {
        final int dstIdx = i * 4;
        labToBgrPixel(origL[i], abAResized[i], abBResized[i], bgrBuf);
        resultBytes[dstIdx] = (bgrBuf[2] * 255.0).round().clamp(0, 255);
        resultBytes[dstIdx + 1] = (bgrBuf[1] * 255.0).round().clamp(0, 255);
        resultBytes[dstIdx + 2] = (bgrBuf[0] * 255.0).round().clamp(0, 255);
        resultBytes[dstIdx + 3] = 255;
      }

      final Uint8List pngBytes = img.encodePng(resultImage);
      await File(outputPath).writeAsBytes(pngBytes);

      return true;
    } catch (e, stack) {
      debugPrint('DDColor colorization failed: $e');
      debugPrint('Stack: $stack');
      return false;
    }
  }

  /// 从 runAsync 输出 (List 或 Map) 中提取第一个 OrtValue
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

  /// 安全释放 ONNX 资源
  static void _safeRelease(
    OrtValueTensor? inputOrt,
    OrtRunOptions? runOptions,
    OrtSession? session,
    dynamic outputs,
  ) {
    try {
      inputOrt?.release();
    } catch (_) {}
    try {
      runOptions?.release();
    } catch (_) {}
    try {
      if (outputs is List) {
        for (var v in outputs) {
          try {
            (v as OrtValue?)?.release();
          } catch (_) {}
        }
      } else if (outputs is Map) {
        for (var v in outputs.values) {
          try {
            (v as OrtValue?)?.release();
          } catch (_) {}
        }
      }
    } catch (_) {}
    try {
      session?.release();
    } catch (_) {}
  }

  /// 平面图像的双线性插值 (float32 单通道)
  static void _resizePlanarBilinear(
    Float32List src,
    int srcW,
    int srcH,
    Float32List dst,
    int dstW,
    int dstH,
  ) {
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
        final double v = v0 * (1 - fy) + v1 * fy;

        dst[y * dstW + x] = v;
      }
    }
  }
}
