import 'dart:io';
import 'dart:typed_data';

import 'package:flutter/foundation.dart';
import 'package:image/image.dart' as img;
import 'package:path/path.dart' as path;
import 'package:path_provider/path_provider.dart';

/// DeOldify 处理参数（用于 Isolate 传递）
class DeOldifyParams {
  final Uint8List imageBytes;
  final String modelType;
  final String modelDirectoryPath;

  const DeOldifyParams({
    required this.imageBytes,
    this.modelType = 'stable',
    required this.modelDirectoryPath,
  });
}

/// DeOldify 图像上色处理器
///
/// 负责调用 deoldify.exe 对图像进行 AI 上色处理，
/// 在 Isolate 中运行以避免阻塞 UI 线程。
class DeOldifyProcessor {
  /// 在 Isolate 中处理图像上色
  /// [params] DeOldify 处理参数
  /// 返回处理后的图像字节数据 (PNG 格式)
  static Future<Uint8List?> processInIsolate(DeOldifyParams params) async {
    try {
      return await compute(_processImage, params);
    } catch (e) {
      debugPrint('DeOldify processing error: $e');
      return null;
    }
  }

  /// 查找 deoldify exe 的路径
  /// 根据模型类型选择 deoldify_stable.exe 或 deoldify_artistic.exe
  /// 按优先级检查：应用目录/deoldify/、模型目录/、应用目录/
  static String? _findExePath(String modelDirectoryPath, String modelType) {
    final exeName = modelType == 'artistic' ? 'deoldify_artistic.exe' : 'deoldify_stable.exe';

    final candidates = <String>[
      // 1. 应用运行目录下的 deoldify 子目录
      path.join(Directory.current.path, 'deoldify', exeName),
      // 2. 模型目录中
      path.join(modelDirectoryPath, exeName),
      // 3. 模型目录的上级目录
      path.join(path.dirname(modelDirectoryPath), exeName),
      // 4. 应用运行目录
      path.join(Directory.current.path, exeName),
      // 5. 通用名称 deoldify.exe（兼容旧版）
      path.join(Directory.current.path, 'deoldify', 'deoldify.exe'),
      path.join(modelDirectoryPath, 'deoldify.exe'),
    ];

    for (final candidate in candidates) {
      if (File(candidate).existsSync()) {
        return candidate;
      }
    }
    return null;
  }

  /// 将图片字节数据转换为 PNG 格式
  /// deoldify.exe 使用 System.Drawing.Bitmap，不支持 WebP，需要先转换
  static Uint8List _convertToPng(Uint8List imageBytes) {
    try {
      // 检查是否已经是 PNG（magic bytes: 89 50 4E 47）
      if (imageBytes.length >= 4 &&
          imageBytes[0] == 0x89 &&
          imageBytes[1] == 0x50 &&
          imageBytes[2] == 0x4E &&
          imageBytes[3] == 0x47) {
        return imageBytes;
      }

      // 检查是否是 JPEG（magic bytes: FF D8 FF）
      if (imageBytes.length >= 3 &&
          imageBytes[0] == 0xFF &&
          imageBytes[1] == 0xD8 &&
          imageBytes[2] == 0xFF) {
        // JPEG 也被 System.Drawing.Bitmap 支持，但为统一处理也转换
      }

      // 检查是否是 BMP（magic bytes: 42 4D）
      if (imageBytes.length >= 2 &&
          imageBytes[0] == 0x42 &&
          imageBytes[1] == 0x4D) {
        return imageBytes;
      }

      // 检查是否是 GIF（magic bytes: 47 49 46 38）
      if (imageBytes.length >= 4 &&
          imageBytes[0] == 0x47 &&
          imageBytes[1] == 0x49 &&
          imageBytes[2] == 0x46 &&
          imageBytes[3] == 0x38) {
        return imageBytes;
      }

      // WebP 或其他格式：用 image 包解码并重新编码为 PNG
      final decoded = img.decodeImage(imageBytes);
      if (decoded != null) {
        return Uint8List.fromList(img.encodePng(decoded));
      }

      // 解码失败，返回原始数据让 exe 尝试
      return imageBytes;
    } catch (e) {
      debugPrint('DeOldify: image format conversion error: $e');
      return imageBytes;
    }
  }

  /// 在 Isolate 中执行的静态方法
  static Future<Uint8List?> _processImage(DeOldifyParams params) async {
    File? inputFile;
    File? outputFile;

    try {
      final tempDir = await getTemporaryDirectory();
      final timestamp = DateTime.now().millisecondsSinceEpoch;

      inputFile = File(path.join(tempDir.path, 'deoldify_in_$timestamp.png'));
      outputFile = File(path.join(tempDir.path, 'deoldify_out_$timestamp.png'));

      // 将图片转换为 PNG 格式（deoldify.exe 不支持 WebP）
      final pngBytes = _convertToPng(params.imageBytes);
      await inputFile.writeAsBytes(pngBytes);

      // 查找 deoldify exe
      final exePath = _findExePath(params.modelDirectoryPath, params.modelType);
      if (exePath == null) {
        debugPrint('DeOldify: deoldify exe not found for model type "${params.modelType}". '
            'Please ensure deoldify_${params.modelType}.exe is placed in the deoldify directory.');
        return null;
      }

      final result = await Process.run(
        exePath,
        [inputFile.path, outputFile.path, params.modelType, params.modelDirectoryPath],
        stdoutEncoding: null,
        stderrEncoding: null,
      );

      if (result.exitCode != 0) {
        final stderr = result.stderr != null ? String.fromCharCodes(result.stderr as List<int>) : '';
        debugPrint('DeOldify process failed with exit code ${result.exitCode}: $stderr');
        return null;
      }

      if (!await outputFile.exists()) {
        debugPrint('DeOldify output file not found');
        return null;
      }

      return await outputFile.readAsBytes();
    } catch (e) {
      debugPrint('DeOldify _processImage error: $e');
      return null;
    } finally {
      try {
        if (inputFile != null && await inputFile.exists()) {
          await inputFile.delete();
        }
      } catch (_) {}
      try {
        if (outputFile != null && await outputFile.exists()) {
          await outputFile.delete();
        }
      } catch (_) {}
    }
  }
}
