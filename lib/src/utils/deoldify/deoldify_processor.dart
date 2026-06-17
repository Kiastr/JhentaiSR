import 'dart:io';
import 'dart:typed_data';

import 'package:flutter/foundation.dart';
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

  /// 在 Isolate 中执行的静态方法
  static Future<Uint8List?> _processImage(DeOldifyParams params) async {
    File? inputFile;
    File? outputFile;

    try {
      final tempDir = await getTemporaryDirectory();
      final timestamp = DateTime.now().millisecondsSinceEpoch;

      inputFile = File(path.join(tempDir.path, 'deoldify_in_$timestamp.png'));
      outputFile = File(path.join(tempDir.path, 'deoldify_out_$timestamp.png'));

      await inputFile.writeAsBytes(params.imageBytes);

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
