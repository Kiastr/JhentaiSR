import 'dart:io';
import 'dart:typed_data';

import 'package:flutter/foundation.dart';
import 'package:flutter_onnxruntime/flutter_onnxruntime.dart';
import 'package:image/image.dart' as img;

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

/// 图像上色引擎（Dart 原生，基于 ONNX Runtime + image 包）
///
/// 移植自 colorize.py，支持 DDColor 和 DeOldify 两种模型
/// 所有计算都在单线程内完成，可通过 compute() 放入 Isolate
class ColorizeUpscaler {
  /// 执行 DDColor 上色（文件路径版，用于 compute() Isolate）
  static Future<bool> colorizeDDColor(ColorizeParams params) async {
    try {
      final File inputFile = File(params.inputPath);
      final Uint8List inputBytes = await inputFile.readAsBytes();

      final img.Image? srcImage = img.decodeImage(inputBytes);
      if (srcImage == null) {
        return false;
      }

      final int origWidth = srcImage.width;
      final int origHeight = srcImage.height;
      final int origPixels = origWidth * origHeight;

      final Float32List origL = Float32List(origPixels);
      final Float32List _unusedA = Float32List(origPixels);
      final Float32List _unusedB = Float32List(origPixels);
      extractLabFromRgbUint8(
        srcImage.bytes,
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

      final Float32List resizedL = Float32List(modelSize * modelSize);
      final Float32List _unusedL2 = Float32List(modelSize * modelSize);
      final Float32List _unusedL3 = Float32List(modelSize * modelSize);
      extractLabFromRgbUint8(
        resized.bytes,
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

      final OnnxRuntime ort = OnnxRuntime();
      final session = await ort.createSessionFromFile(params.modelPath);
      final List<int> inputShape = [1, 3, modelSize, modelSize];

      final List<double> inputList = nchwInput.toList(growable: false);
      final Map<String, OrtValue> inputs = {
        params.inputName ?? 'input': await OrtValue.fromList(inputList, inputShape),
      };

      final Map<String, OrtValue> outputs = await session.run(inputs);
      final String outName = params.outputName ?? (outputs.keys.firstWhere(
            (k) => k.toLowerCase().contains('output') || k.toLowerCase().contains('ab'),
        orElse: () => outputs.keys.first,
      ));

      final outputOrtValue = outputs[outName];
      if (outputOrtValue == null) {
        return false;
      }

      final List outputShape = await outputOrtValue.shape;
      final List outputData = await outputOrtValue.data;
      final List<double> abFlat = outputData.cast<double>();

      final int outC = outputShape[1] as int;
      final int outH = outputShape[2] as int;
      final int outW = outputShape[3] as int;

      final Float32List abA = Float32List(outH * outW);
      final Float32List abB = Float32List(outH * outW);
      for (int y = 0; y < outH; y++) {
        for (int x = 0; x < outW; x++) {
          final int linearIdx = y * outW + x;
          abA[linearIdx] = abFlat[0 * outH * outW + linearIdx];
          abB[linearIdx] = abFlat[1 * outH * outW + linearIdx];
        }
      }

      final Float32List resizedA = Float32List(origPixels);
      final Float32List resizedB = Float32List(origPixels);
      _resizePlanarBilinear(abA, outW, outH, resizedA, origWidth, origHeight);
      _resizePlanarBilinear(abB, outW, outH, resizedB, origWidth, origHeight);

      final img.Image result = img.Image(width: origWidth, height: origHeight, numChannels: 4);
      composeLabToRgbUint8(origL, resizedA, resizedB, origWidth, origHeight, result.bytes);

      final Uint8List pngBytes = img.encodePng(result);
      await File(params.outputPath).writeAsBytes(pngBytes);

      return true;
    } catch (e) {
      debugPrint('DDColor colorization failed: $e');
      return false;
    }
  }

  /// 执行 DeOldify 上色（文件路径版，用于 compute() Isolate）
  static Future<bool> colorizeDeOldify(ColorizeParams params) async {
    try {
      final File inputFile = File(params.inputPath);
      final Uint8List inputBytes = await inputFile.readAsBytes();

      final img.Image? srcImage = img.decodeImage(inputBytes);
      if (srcImage == null) {
        return false;
      }

      final int origWidth = srcImage.width;
      final int origHeight = srcImage.height;

      const int modelSize = 256;
      final img.Image resizedGray = img.copyResize(
        srcImage,
        width: modelSize,
        height: modelSize,
        interpolation: img.Interpolation.linear,
      );

      final Uint8List grayRgbBytes = _toGrayscale3Channel(resizedGray);

      final Float32List nchwInput = Float32List(1 * 3 * modelSize * modelSize);
      for (int c = 0; c < 3; c++) {
        for (int y = 0; y < modelSize; y++) {
          for (int x = 0; x < modelSize; x++) {
            final int hwIndex = (y * modelSize + x) * 4;
            final int chwIndex = c * modelSize * modelSize + y * modelSize + x;
            nchwInput[chwIndex] = grayRgbBytes[hwIndex + c].toDouble();
          }
        }
      }

      final OnnxRuntime ort = OnnxRuntime();
      final session = await ort.createSessionFromFile(params.modelPath);
      final List<int> inputShape = [1, 3, modelSize, modelSize];

      final List<double> inputList = nchwInput.toList(growable: false);
      final Map<String, OrtValue> inputs = {
        params.inputName ?? 'input.1': await OrtValue.fromList(inputList, inputShape),
      };

      final Map<String, OrtValue> outputs = await session.run(inputs);
      final String outName = params.outputName ?? (outputs.keys.firstWhere(
            (k) => k.toLowerCase().contains('output'),
        orElse: () => outputs.keys.first,
      ));

      final outputOrtValue = outputs[outName];
      if (outputOrtValue == null) {
        return false;
      }

      final List outputShape = await outputOrtValue.shape;
      final List outputData = await outputOrtValue.data;
      final List<double> flatOutput = outputData.cast<double>();

      final int outC = outputShape[1] as int;
      final int outH = outputShape[2] as int;
      final int outW = outputShape[3] as int;

      final img.Image outImage = img.Image(width: outW, height: outH, numChannels: 4);
      for (int y = 0; y < outH; y++) {
        for (int x = 0; x < outW; x++) {
          final int outIdx = (y * outW + x) * 4;
          final int ch0 = 0 * outH * outW + y * outW + x;
          final int ch1 = 1 * outH * outW + y * outW + x;
          final int ch2 = 2 * outH * outW + y * outW + x;
          outImage.bytes[outIdx] = flatOutput[ch2].round().clamp(0, 255);
          outImage.bytes[outIdx + 1] = flatOutput[ch1].round().clamp(0, 255);
          outImage.bytes[outIdx + 2] = flatOutput[ch0].round().clamp(0, 255);
          outImage.bytes[outIdx + 3] = 255;
        }
      }

      final img.Image colorized = img.copyResize(
        outImage,
        width: origWidth,
        height: origHeight,
        interpolation: img.Interpolation.linear,
      );

      final img.Image blurred = img.gaussianBlur(colorized, radius: 6);

      final int origPixels = origWidth * origHeight;
      final Float32List origL = Float32List(origPixels);
      final Float32List _ua1 = Float32List(origPixels);
      final Float32List _ua2 = Float32List(origPixels);
      extractLabFromRgbUint8(srcImage.bytes, origWidth, origHeight, origL, _ua1, _ua2);

      final Float32List colorA = Float32List(origPixels);
      final Float32List colorB = Float32List(origPixels);
      final Float32List colorL = Float32List(origPixels);
      extractLabFromRgbUint8(blurred.bytes, origWidth, origHeight, colorL, colorA, colorB);

      final img.Image result = img.Image(width: origWidth, height: origHeight, numChannels: 4);
      composeLabToRgbUint8(origL, colorA, colorB, origWidth, origHeight, result.bytes);

      final Uint8List pngBytes = img.encodePng(result);
      await File(params.outputPath).writeAsBytes(pngBytes);

      return true;
    } catch (e) {
      debugPrint('DeOldify colorization failed: $e');
      return false;
    }
  }

  /// 将图像转为 3 通道灰度图（返回 RGBA 格式字节）
  static Uint8List _toGrayscale3Channel(img.Image src) {
    final int w = src.width;
    final int h = src.height;
    final Uint8List out = Uint8List(w * h * 4);
    for (int i = 0, j = 0; i < src.bytes.length; i += 4, j += 4) {
      final int r = src.bytes[i];
      final int g = src.bytes[i + 1];
      final int b = src.bytes[i + 2];
      final int gray = (0.299 * r + 0.587 * g + 0.114 * b).round().clamp(0, 255);
      out[j] = gray;
      out[j + 1] = gray;
      out[j + 2] = gray;
      out[j + 3] = 255;
    }
    return out;
  }

  /// 双线性插值 resize 单通道 float32
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
