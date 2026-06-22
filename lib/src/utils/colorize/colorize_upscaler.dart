import 'dart:async';
import 'dart:io';
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
    sessionOptions.setSessionExecutionMode(OrtSessionExecutionMode.ortParallel);
    sessionOptions.setSessionGraphOptimizationLevel(GraphOptimizationLevel.ortEnableAll);
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

      // 预缩放: 如果原图过大，先缩小到长边 <= 1024（更激进以减少后处理耗时）
      const int maxSide = 1024;
      img.Image srcImage = decodedImage;
      if (decodedImage.width > maxSide || decodedImage.height > maxSide) {
        final double scale = maxSide / (decodedImage.width > decodedImage.height ? decodedImage.width : decodedImage.height);
        final int newW = (decodedImage.width * scale).round();
        final int newH = (decodedImage.height * scale).round();
        debugPrint('DDColor: Pre-scaling to ${newW}x${newH}');
        srcImage = img.copyResize(
          decodedImage,
          width: newW,
          height: newH,
          interpolation: img.Interpolation.linear,
        );
      }

      final int origWidth = srcImage.width;
      final int origHeight = srcImage.height;
      final int origPixels = origWidth * origHeight;
      final Uint8List srcBytes = srcImage.buffer.asUint8List();

      // 提取原图 LAB L 通道
      final Float32List origL = Float32List(origPixels);
      final Float32List _unusedA = Float32List(origPixels);
      final Float32List _unusedB = Float32List(origPixels);
      extractLabFromRgbUint8(
        srcBytes,
        origWidth,
        origHeight,
        origL,
        _unusedA,
        _unusedB,
      );

      const int modelSize = 256;
      final img.Image resized = img.copyResize(
        srcImage,
        width: modelSize,
        height: modelSize,
        interpolation: img.Interpolation.linear,
      );
      final Uint8List resizedBytes = resized.buffer.asUint8List();

      final Float32List resizedL = Float32List(modelSize * modelSize);
      final Float32List _unusedL2 = Float32List(modelSize * modelSize);
      final Float32List _unusedL3 = Float32List(modelSize * modelSize);
      extractLabFromRgbUint8(
        resizedBytes,
        modelSize,
        modelSize,
        resizedL,
        _unusedL2,
        _unusedL3,
      );

      final Float32List fakeLabBgr = Float32List(modelSize * modelSize * 3);
      composeLabPlanarToBgrFloat32(
        resizedL,
        Float32List(modelSize * modelSize),
        Float32List(modelSize * modelSize),
        modelSize,
        modelSize,
        fakeLabBgr,
      );

      final Float32List nchwInput = Float32List(1 * 3 * modelSize * modelSize);
      for (int c = 0; c < 3; c++) {
        for (int y = 0; y < modelSize; y++) {
          for (int x = 0; x < modelSize; x++) {
            final int hwIndex = (y * modelSize + x) * 3;
            final int chwIndex = c * modelSize * modelSize + y * modelSize + x;
            nchwInput[chwIndex] = fakeLabBgr[hwIndex + c];
          }
        }
      }

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
        const Duration(seconds: 60),
        onTimeout: () {
          debugPrint('DDColor: Inference timeout after 60 seconds');
          throw TimeoutException('ONNX推理超时(60秒)');
        },
      );
      debugPrint('DDColor: Inference completed');

      final OrtValue? outputOrt = _extractFirstOutput(outputs);
      if (outputOrt == null) {
        debugPrint('DDColor: output is null');
        inputOrt.release();
        runOptions.release();
        return false;
      }

      // 让出主线程，避免阻塞
      await Future<void>.delayed(Duration.zero);

      final dynamic outputValue = outputOrt.value;
      inputOrt.release();
      runOptions.release();
      outputOrt.release();

      if (outputValue == null) {
        debugPrint('DDColor: output value is null');
        return false;
      }

      // 解析输出
      final List<dynamic> rawData = outputValue as List<dynamic>;
      final Float32List abFlat = Float32List(rawData.length);
      for (int i = 0; i < rawData.length; i++) {
        abFlat[i] = (rawData[i] as num).toDouble();
      }

      const int outH = 256;
      const int outW = 256;

      final Float32List abA = Float32List(outH * outW);
      final Float32List abB = Float32List(outH * outW);
      for (int y = 0; y < outH; y++) {
        for (int x = 0; x < outW; x++) {
          final int linearIdx = y * outW + x;
          abA[linearIdx] = abFlat[0 * outH * outW + linearIdx];
          abB[linearIdx] = abFlat[1 * outH * outW + linearIdx];
        }
      }

      // 让出主线程
      await Future<void>.delayed(Duration.zero);

      // resize ab 到原图大小
      final Float32List resizedA = Float32List(origPixels);
      final Float32List resizedB = Float32List(origPixels);
      _resizePlanarBilinear(abA, outW, outH, resizedA, origWidth, origHeight);
      _resizePlanarBilinear(abB, outW, outH, resizedB, origWidth, origHeight);

      // 让出主线程
      await Future<void>.delayed(Duration.zero);

      // 合成最终图像
      final img.Image resultImg = img.Image(width: origWidth, height: origHeight, numChannels: 4);
      composeLabToRgbUint8(origL, resizedA, resizedB, origWidth, origHeight, resultImg.buffer.asUint8List());

      final Uint8List pngBytes = img.encodePng(resultImg);
      await File(params.outputPath).writeAsBytes(pngBytes);

      debugPrint('DDColor: Success, saved to ${params.outputPath}');
      return true;
    } catch (e) {
      debugPrint('DDColor colorization failed: $e');
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

      // 预缩放
      const int maxSide = 1024;
      img.Image srcImage = decodedImage;
      if (decodedImage.width > maxSide || decodedImage.height > maxSide) {
        final double scale = maxSide / (decodedImage.width > decodedImage.height ? decodedImage.width : decodedImage.height);
        final int newW = (decodedImage.width * scale).round();
        final int newH = (decodedImage.height * scale).round();
        debugPrint('DeOldify: Pre-scaling to ${newW}x${newH}');
        srcImage = img.copyResize(
          decodedImage,
          width: newW,
          height: newH,
          interpolation: img.Interpolation.linear,
        );
      }

      final int origWidth = srcImage.width;
      final int origHeight = srcImage.height;
      final Uint8List srcBytes = srcImage.buffer.asUint8List();

      const int modelSize = 256;
      final img.Image resizedGray = img.copyResize(
        srcImage,
        width: modelSize,
        height: modelSize,
        interpolation: img.Interpolation.linear,
      );
      final Uint8List resizedBytes = resizedGray.buffer.asUint8List();

      final Uint8List grayRgbBytes = _toGrayscale3Channel(resizedBytes);

      final Float32List nchwInput = Float32List(1 * 3 * modelSize * modelSize);
      for (int c = 0; c < 3; c++) {
        for (int y = 0; y < modelSize; y++) {
          for (int x = 0; x < modelSize; x++) {
            final int hwIndex = (y * modelSize + x) * 3;
            final int chwIndex = c * modelSize * modelSize + y * modelSize + x;
            nchwInput[chwIndex] = grayRgbBytes[hwIndex + c].toDouble();
          }
        }
      }

      // ONNX 推理 - 使用缓存的 session
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
        const Duration(seconds: 60),
        onTimeout: () {
          debugPrint('DeOldify: Inference timeout after 60 seconds');
          throw TimeoutException('ONNX推理超时(60秒)');
        },
      );
      debugPrint('DeOldify: Inference completed');

      final OrtValue? outputOrt = _extractFirstOutput(outputs);
      if (outputOrt == null) {
        debugPrint('DeOldify: output is null');
        inputOrt.release();
        runOptions.release();
        return false;
      }

      // 让出主线程
      await Future<void>.delayed(Duration.zero);

      final dynamic outputValue = outputOrt.value;
      inputOrt.release();
      runOptions.release();
      outputOrt.release();

      if (outputValue == null) {
        debugPrint('DeOldify: output value is null');
        return false;
      }

      // 解析输出
      final List<dynamic> rawData = outputValue as List<dynamic>;
      final Float32List flatOutput = Float32List(rawData.length);
      for (int i = 0; i < rawData.length; i++) {
        flatOutput[i] = (rawData[i] as num).toDouble();
      }

      // 后处理: CHW → RGBA
      final img.Image colorized256 = img.Image(width: modelSize, height: modelSize, numChannels: 4);
      final Uint8List c256Bytes = colorized256.buffer.asUint8List();
      for (int y = 0; y < modelSize; y++) {
        for (int x = 0; x < modelSize; x++) {
          final int pi = y * modelSize + x;
          final int dstIdx = pi * 4;
          c256Bytes[dstIdx] = flatOutput[0 * modelSize * modelSize + pi].round().clamp(0, 255);
          c256Bytes[dstIdx + 1] = flatOutput[1 * modelSize * modelSize + pi].round().clamp(0, 255);
          c256Bytes[dstIdx + 2] = flatOutput[2 * modelSize * modelSize + pi].round().clamp(0, 255);
          c256Bytes[dstIdx + 3] = 255;
        }
      }

      // 让出主线程
      await Future<void>.delayed(Duration.zero);

      // resize 回原图
      final img.Image colorizedFull = img.copyResize(
        colorized256,
        width: origWidth,
        height: origHeight,
        interpolation: img.Interpolation.linear,
      );

      // 高斯模糊
      final img.Image colorizedBlurred = img.gaussianBlur(colorizedFull, radius: 6);
      final Uint8List cbBytes = colorizedBlurred.buffer.asUint8List();

      // LAB 合成
      final Uint8List targetL = Uint8List(origWidth * origHeight);
      for (int i = 0; i < origWidth * origHeight; i++) {
        targetL[i] = srcBytes[i * srcImage.numChannels + 2];
      }

      final img.Image resultImg = img.Image(width: origWidth, height: origHeight, numChannels: 4);
      final Uint8List resultBytes = resultImg.buffer.asUint8List();

      for (int y = 0; y < origHeight; y++) {
        for (int x = 0; x < origWidth; x++) {
          final int pi = y * origWidth + x;
          final int srcIdx = pi * colorizedBlurred.numChannels;

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

      final Uint8List pngBytes = img.encodePng(resultImg);
      await File(params.outputPath).writeAsBytes(pngBytes);

      debugPrint('DeOldify: Success, saved to ${params.outputPath}');
      return true;
    } catch (e) {
      debugPrint('DeOldify colorization failed: $e');
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

  /// 灰度图转 RGB 三通道（每个通道都是灰度值）
  static Uint8List _toGrayscale3Channel(Uint8List rgbaBytes) {
    final int pixelCount = rgbaBytes.length ~/ 4;
    final Uint8List result = Uint8List(pixelCount * 3);
    for (int i = 0; i < pixelCount; i++) {
      final int gray = rgbaBytes[i * 4]; // R 通道作为灰度值
      result[i * 3] = gray;
      result[i * 3 + 1] = gray;
      result[i * 3 + 2] = gray;
    }
    return result;
  }

  /// 平面图像的双线性插值
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
