import 'dart:convert';
import 'dart:io';
import 'dart:typed_data';

import 'package:flutter/foundation.dart';
import 'package:image/image.dart' as img;
import 'package:jhentai/src/service/log.dart';
import 'package:path/path.dart' as path;

/// DeOldify 处理参数（用于 Isolate 传递）
class DeOldifyParams {
  final Uint8List imageBytes;
  final String modelType;
  final String modelDirectoryPath;
  final String tempDirPath;

  const DeOldifyParams({
    required this.imageBytes,
    this.modelType = 'stable',
    required this.modelDirectoryPath,
    required this.tempDirPath,
  });
}

/// DeOldify 处理结果
class DeOldifyResult {
  final Uint8List? imageBytes;
  final String? error;

  const DeOldifyResult.success(this.imageBytes) : error = null;
  const DeOldifyResult.failure(this.error) : imageBytes = null;
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
      final result = await compute(_processImage, params);
      if (result.error != null) {
        log.error('DeOldify: ${result.error}');
      }
      return result.imageBytes;
    } catch (e) {
      log.error('DeOldify processing error: $e');
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

      // WebP、JPEG 或其他格式：用 image 包解码并重新编码为 PNG
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

  /// 在 Isolate 中执行的静态方法（同步，因为 compute 需要）
  static DeOldifyResult _processImage(DeOldifyParams params) {
    File? inputFile;
    File? outputFile;

    try {
      final tempDir = Directory(params.tempDirPath);
      final timestamp = DateTime.now().millisecondsSinceEpoch;

      inputFile = File(path.join(tempDir.path, 'deoldify_in_$timestamp.png'));
      outputFile = File(path.join(tempDir.path, 'deoldify_out_$timestamp.png'));

      // 将图片转换为 PNG 格式（deoldify.exe 不支持 WebP）
      final pngBytes = _convertToPng(params.imageBytes);
      inputFile.writeAsBytesSync(pngBytes);

      // 查找 deoldify exe
      final exePath = _findExePath(params.modelDirectoryPath, params.modelType);
      if (exePath == null) {
        final exeName = params.modelType == 'artistic' ? 'deoldify_artistic.exe' : 'deoldify_stable.exe';
        return DeOldifyResult.failure(
          'deoldify exe not found. Please ensure $exeName is placed in the deoldify directory. '
          'Searched: ${path.join(Directory.current.path, 'deoldify', exeName)}, '
          '${path.join(params.modelDirectoryPath, exeName)}, etc.'
        );
      }

      final result = Process.runSync(
        exePath,
        [inputFile.path, outputFile.path, params.modelType, params.modelDirectoryPath],
        stdoutEncoding: null,
        stderrEncoding: null,
      );

      if (result.exitCode != 0) {
        // Decode stderr/stdout bytes, handling potential GBK encoding on Chinese Windows
        final stderr = _decodeBytes(result.stderr as List<int>?);
        final stdout = _decodeBytes(result.stdout as List<int>?);
        final exitCodeDesc = _describeExitCode(result.exitCode);
        // Check if the stdout contains format detection info
        final formatInfo = _extractFormatInfo(stdout);
        String hint = '';
        if (result.exitCode == -1073741819) {
          // STATUS_ACCESS_VIOLATION
          if (stdout.contains('Architecture mismatch')) {
            hint = '\n\nHint: Architecture mismatch! The exe was compiled for a different '
                'model type (stable vs artistic). Please use the correct exe: '
                'deoldify_artistic.exe for artistic models, deoldify_stable.exe for stable models.';
          } else if (stdout.contains('model file loaded successfully')) {
            // Model loaded fine but crashed during inference - likely architecture mismatch
            hint = '\n\nHint: Model loaded successfully but crashed during processing. '
                'This is likely an architecture mismatch: the exe was compiled with '
                '/define:stable but is being used with an artistic model (or vice versa). '
                'Please recompile using Compile.artistic.unified.bat for artistic models.';
          } else if (formatInfo == null) {
            hint = '\n\nHint: This is a memory access violation. The exe may be '
                'outdated. Please recompile deoldify_artistic.exe from the fixed '
                'source code in DeOldify.NET/Implementation/src/.';
          }
        } else if (result.exitCode == 2) {
          // Architecture mismatch detected by Program.cs
          hint = '\n\nHint: Architecture mismatch detected. See stderr for details.';
        }
        return DeOldifyResult.failure(
          'process failed ($exitCodeDesc). exe: $exePath$hint, stderr: $stderr, stdout: $stdout'
        );
      }

      if (!outputFile.existsSync()) {
        final stdout = _decodeBytes(result.stdout as List<int>?);
        final stderr = _decodeBytes(result.stderr as List<int>?);
        return DeOldifyResult.failure(
          'output file not found after processing. '
          'exit code: ${result.exitCode}, stdout: $stdout, stderr: $stderr'
        );
      }

      return DeOldifyResult.success(outputFile.readAsBytesSync());
    } catch (e) {
      return DeOldifyResult.failure('_processImage error: $e');
    } finally {
      try {
        if (inputFile != null && inputFile.existsSync()) {
          inputFile.deleteSync();
        }
      } catch (_) {}
      try {
        if (outputFile != null && outputFile.existsSync()) {
          outputFile.deleteSync();
        }
      } catch (_) {}
    }
  }

  /// Decode bytes from process output, trying UTF-8 first then falling back to Latin-1.
  /// On Chinese Windows, stderr may be GBK-encoded which appears as garbled text in UTF-8.
  static String _decodeBytes(List<int>? bytes) {
    if (bytes == null || bytes.isEmpty) return '';
    try {
      return utf8.decode(bytes, allowMalformed: true);
    } catch (_) {
      return String.fromCharCodes(bytes);
    }
  }

  /// Convert Windows process exit code to a human-readable description.
  /// Common crash codes:
  /// - 0xC0000005 (-1073741819): STATUS_ACCESS_VIOLATION (memory access violation)
  /// - 0xC000001D (-1073741795): STATUS_ILLEGAL_INSTRUCTION
  /// - 0xC00000FD (-1073741571): STATUS_STACK_OVERFLOW
  /// - 0xC0000142 (-1073741502): STATUS_DLL_INIT_FAILED
  static String _describeExitCode(int exitCode) {
    if (exitCode == 0) return 'exit code 0 (success)';
    // Convert negative to unsigned 32-bit
    int unsigned = exitCode < 0 ? (0x100000000 + exitCode) : exitCode;
    switch (unsigned) {
      case 0xC0000005:
        return 'exit code $exitCode (STATUS_ACCESS_VIOLATION: memory access violation)';
      case 0xC000001D:
        return 'exit code $exitCode (STATUS_ILLEGAL_INSTRUCTION)';
      case 0xC00000FD:
        return 'exit code $exitCode (STATUS_STACK_OVERFLOW)';
      case 0xC0000142:
        return 'exit code $exitCode (STATUS_DLL_INIT_FAILED: a DLL initialization routine failed)';
      default:
        return 'exit code $exitCode (0x${unsigned.toRadixString(16).toUpperCase()})';
    }
  }

  /// Extract model format info from the exe's stdout output.
  /// The fixed exe prints: "DeOldify: model format detected: ..."
  /// Returns null if the format info is not found (old exe without format detection).
  static String? _extractFormatInfo(String stdout) {
    final marker = 'DeOldify: model format detected:';
    final idx = stdout.indexOf(marker);
    if (idx == -1) return null;
    final end = stdout.indexOf('\n', idx);
    return stdout.substring(idx, end == -1 ? stdout.length : end).trim();
  }
}
