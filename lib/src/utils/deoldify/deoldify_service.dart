import 'dart:async';
import 'dart:io';
import 'dart:typed_data';

import 'package:jhentai/src/service/log.dart';
import 'package:flutter/foundation.dart';
import 'package:path_provider/path_provider.dart';
import 'package:path/path.dart' as path;
import 'package:jhentai/src/setting/deoldify_setting.dart';

import 'deoldify_processor.dart';

/// DeOldify 图像上色服务
///
/// 提供图像 AI 上色处理功能，支持缓存机制以避免重复处理。
/// 采用单例模式，通过 [DeOldifyService.instance] 访问。
class DeOldifyService {
  DeOldifyService._internal();

  static final DeOldifyService _instance = DeOldifyService._internal();

  factory DeOldifyService() => _instance;

  static DeOldifyService get instance => _instance;

  /// 缓存目录路径
  String? _cacheDir;

  /// 正在处理的任务集合（避免重复处理同一图片）
  final Set<String> _processingKeys = {};

  /// 最大并发处理数
  static const int _maxConcurrentTasks = 2;

  /// 当前正在运行的任务数
  int _runningTasks = 0;

  /// 任务队列
  final List<Function> _taskQueue = [];

  /// 初始化缓存目录
  Future<void> init() async {
    if (!Platform.isWindows) return;

    try {
      final dir = await getTemporaryDirectory();
      _cacheDir = path.join(dir.path, 'deoldify_cache');
      final cacheDirectory = Directory(_cacheDir!);
      if (!await cacheDirectory.exists()) {
        await cacheDirectory.create(recursive: true);
      }
    } catch (e) {
      log.error('DeOldify cache init error: $e');
    }
  }

  /// 获取缓存文件路径
  String? _getCachePath(String key) {
    if (_cacheDir == null) return null;
    return path.join(_cacheDir!, '${key.hashCode.abs()}.png');
  }

  /// 检查是否有缓存，有则返回缓存数据
  Future<Uint8List?> _getFromCache(String key) async {
    final cachePath = _getCachePath(key);
    if (cachePath == null) return null;

    final file = File(cachePath);
    if (await file.exists()) {
      try {
        return await file.readAsBytes();
      } catch (e) {
        return null;
      }
    }
    return null;
  }

  /// 保存处理结果到缓存
  Future<void> _saveToCache(String key, Uint8List data) async {
    final cachePath = _getCachePath(key);
    if (cachePath == null) return;

    try {
      final file = File(cachePath);
      await file.writeAsBytes(data);
    } catch (e) {
      log.error('DeOldify cache save error: $e');
    }
  }

  /// 处理图片字节数据，返回上色后的 PNG 字节数据
  ///
  /// [imageBytes] 原始图片字节数据
  /// [cacheKey] 缓存键，用于避免重复处理（通常使用图片 URL 或文件路径）
  /// [modelType] 模型类型，'stable' 或 'artistic'
  Future<Uint8List?> processImage({
    required Uint8List imageBytes,
    required String cacheKey,
    String modelType = 'stable',
  }) async {
    // 非 Windows 平台直接返回 null
    if (!Platform.isWindows) return null;

    // 生成唯一缓存键（包含模型类型信息）
    final fullKey = '${cacheKey}_$modelType';

    // 优先从缓存读取
    final cached = await _getFromCache(fullKey);
    if (cached != null) {
      log.debug('DeOldify: cache hit for $cacheKey');
      return cached;
    }

    // 防止重复处理同一图片
    if (_processingKeys.contains(fullKey)) {
      log.debug('DeOldify: already processing $cacheKey');
      return null;
    }

    _processingKeys.add(fullKey);

    return _enqueueTask(() async {
      try {
        log.debug('DeOldify: processing image $cacheKey, model: $modelType');

        final modelDirPath = deOldifySetting.modelDirectoryPath.value;
        if (modelDirPath == null) {
          log.error('DeOldify: model directory path not set');
          return null;
        }

        final params = DeOldifyParams(
          imageBytes: imageBytes,
          modelType: modelType,
          modelDirectoryPath: modelDirPath,
        );

        final result = await DeOldifyProcessor.processInIsolate(params);

        if (result != null) {
          // 保存到缓存
          await _saveToCache(fullKey, result);
          log.debug('DeOldify: processing complete for $cacheKey');
        }

        return result;
      } catch (e) {
        log.error('DeOldify processing error: $e');
        return null;
      } finally {
        _processingKeys.remove(fullKey);
      }
    });
  }

  /// 处理本地图片文件
  ///
  /// [filePath] 本地图片文件路径
  /// [modelType] 模型类型
  Future<Uint8List?> processFile({
    required String filePath,
    String modelType = 'stable',
  }) async {
    if (!Platform.isWindows) return null;

    try {
      final file = File(filePath);
      if (!await file.exists()) return null;

      final imageBytes = await file.readAsBytes();
      return processImage(
        imageBytes: imageBytes,
        cacheKey: filePath,
        modelType: modelType,
      );
    } catch (e) {
      log.error('DeOldify file processing error: $e');
      return null;
    }
  }

  /// 将任务加入队列并按序执行
  Future<T?> _enqueueTask<T>(Future<T?> Function() task) async {
    final completer = Completer<T?>();

    _taskQueue.add(() async {
      _runningTasks++;
      try {
        final result = await task();
        completer.complete(result);
      } catch (e) {
        completer.completeError(e);
      } finally {
        _runningTasks--;
        _nextTask();
      }
    });

    _nextTask();
    return completer.future;
  }

  /// 执行下一个任务
  void _nextTask() {
    if (_runningTasks < _maxConcurrentTasks && _taskQueue.isNotEmpty) {
      final task = _taskQueue.removeAt(0);
      task();
    }
  }

  /// 清除所有上色缓存
  Future<void> clearCache() async {
    if (_cacheDir == null) return;
    try {
      final dir = Directory(_cacheDir!);
      if (await dir.exists()) {
        await dir.delete(recursive: true);
        await dir.create(recursive: true);
      }
      log.debug('DeOldify: cache cleared');
    } catch (e) {
      log.error('DeOldify cache clear error: $e');
    }
  }

  /// 获取缓存占用的磁盘大小（字节）
  Future<int> getCacheSize() async {
    if (_cacheDir == null) return 0;
    try {
      final dir = Directory(_cacheDir!);
      if (!await dir.exists()) return 0;

      int totalSize = 0;
      await for (final entity in dir.list(recursive: true)) {
        if (entity is File) {
          totalSize += await entity.length();
        }
      }
      return totalSize;
    } catch (e) {
      return 0;
    }
  }
}
