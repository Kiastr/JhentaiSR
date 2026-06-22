import 'dart:convert';
import 'dart:io';

import 'package:dio/dio.dart';
import 'package:flutter/foundation.dart';
import 'package:flutter/services.dart';
import 'package:get/get_core/src/get_main.dart';
import 'package:get/get_instance/get_instance.dart';
import 'package:get/get_state_manager/src/simple/get_controllers.dart';
import 'package:get/get_utils/get_utils.dart';
import 'package:jhentai/src/database/database.dart';
import 'package:jhentai/src/enum/config_enum.dart';
import 'package:jhentai/src/extension/dio_exception_extension.dart';
import 'package:jhentai/src/extension/get_logic_extension.dart';
import 'package:jhentai/src/network/eh_request.dart';
import 'package:jhentai/src/service/local_config_service.dart';
import 'package:jhentai/src/setting/colorization_setting.dart';
import 'package:path/path.dart';
import 'package:retry/retry.dart';

import '../model/gallery_image.dart';
import 'archive_download_service.dart';
import 'gallery_download_service.dart';
import 'jh_service.dart';
import 'log.dart';
import 'path_service.dart';
import 'super_resolution_service.dart' show SuperResolutionType;
import '../utils/archive_util.dart';
import '../utils/colorize/colorize_upscaler.dart';
import '../utils/eh_executor.dart';
import '../utils/toast_util.dart';
import '../widget/loading_state_indicator.dart';

ColorizationService colorizationService = ColorizationService();

/// 上色服务
class ColorizationService extends GetxController with JHLifeCircleBeanErrorCatch implements JHLifeCircleBean {
  static const String downloadId = 'colorizationDownloadId';
  static const String pythonDownloadId = 'pythonDownloadId';
  static const String colorizationId = 'colorizationId';
  static const String colorizationImageId = 'colorizationImageId';

  LoadingState downloadState = LoadingState.idle;
  String downloadProgress = '0%';

  LoadingState pythonDownloadState = LoadingState.idle;
  String pythonDownloadProgress = '0%';

  EHExecutor executor = EHExecutor(concurrency: 1);

  /// 移动端使用 Dart 原生 ONNX 推理（不依赖 Python 环境）
  bool get _useDartNative => !GetPlatform.isDesktop;

  /// 内存中的上色信息表: gid -> type -> info
  final Map<int, Map<int, ColorizationInfo>> _infoTable = {};

  /// colorize.py 脚本在磁盘上的路径（从 asset 复制出来）
  String? _scriptPath;

  static const String imageDirName = 'colorization';

  @override
  List<JHLifeCircleBean> get initDependencies => super.initDependencies
    ..add(galleryDownloadService)
    ..add(archiveDownloadService);

  @override
  Future<void> doInitBean() async {
    Get.put(this, permanent: true);

    await _extractScript();

    if (!await galleryDownloadService.completed) {
      return;
    }
    if (!await archiveDownloadService.completed) {
      return;
    }

    await _loadAllColorizationInfo();
    _checkInfoSourceExists();

    Future.wait(_infoTable.entries
        .expand((gidEntry) => gidEntry.value.entries.map((e) => (gid: gidEntry.key, typeIndex: e.key, info: e.value)))
        .where((e) => e.info.status == ColorizationStatus.running)
        .map((e) => executor.scheduleTask(0, () => _doColorize(e.gid, SuperResolutionType.values[e.typeIndex])))
        .toList());
    super.onInit();
  }

  @override
  Future<void> doAfterBeanReady() async {}

  /// 从 asset 中提取 colorize.py 到磁盘
  Future<void> _extractScript() async {
    try {
      final dir = pathService.getVisibleDir();
      final scriptDir = Directory(join(dir.path, 'colorize'));
      if (!await scriptDir.exists()) {
        await scriptDir.create(recursive: true);
      }
      _scriptPath = join(scriptDir.path, 'colorize.py');
      final scriptFile = File(_scriptPath!);
      // 总是覆盖，确保应用更新后使用最新版脚本
      final data = await rootBundle.load('assets/colorize/colorize.py');
      await scriptFile.writeAsBytes(data.buffer.asUint8List());
    } catch (e) {
      log.error('Extract colorize.py failed: $e');
    }
  }

  ColorizationInfo? get(int gid, SuperResolutionType type) {
    return _infoTable[gid]?[type.index];
  }

  /// 下载并自动配置 Python 环境
  Future<void> downloadPythonEnv() async {
    pythonDownloadProgress = '0%';
    pythonDownloadState = LoadingState.loading;
    updateSafely([pythonDownloadId]);

    final String downloadPath = join(pathService.getVisibleDir().path, 'python_env_ddcolor.zip');
    final String extractPath = join(pathService.getVisibleDir().path, 'python_env_ddcolor');

    try {
      await retry(
        () => ehRequest.download(
          url: ColorizationSetting.pythonEnvDownloadUrl,
          path: downloadPath,
          receiveTimeout: 15 * 60 * 1000,
          onReceiveProgress: (count, total) {
            pythonDownloadProgress = (count / total * 100).toStringAsFixed(2) + '%';
            updateSafely([pythonDownloadId]);
          },
        ),
        maxAttempts: 5,
        onRetry: (error) => log.warning('Download python env failed, retry.'),
      );
    } on DioException catch (e) {
      log.error('Download python env failed after 5 times', e.errorMsg);
      pythonDownloadState = LoadingState.error;
      updateSafely([pythonDownloadId]);
      return;
    }

    log.info('Python env downloaded, start unzipping...');

    bool success = await extractZipArchive(downloadPath, extractPath);
    if (!success) {
      log.error('Extract python env failed');
      pythonDownloadState = LoadingState.error;
      updateSafely([pythonDownloadId]);
      return;
    }

    try {
      File(downloadPath).deleteSync();
    } catch (e) {
      log.error('Delete python_env_ddcolor.zip failed: $e');
    }

    if (GetPlatform.isWindows) {
      log.info('Running install.bat...');
      try {
        ProcessResult result = await Process.run(
          'install.bat',
          [],
          workingDirectory: extractPath,
          runInShell: true,
        );
        log.info('install.bat finished with exitCode: ${result.exitCode}');
      } catch (e) {
        log.error('Run install.bat failed: $e');
      }
    }

    String pythonPath = join(extractPath, GetPlatform.isWindows ? 'python.exe' : 'bin/python3');
    if (await File(pythonPath).exists()) {
      await colorizationSetting.savePythonPath(pythonPath);
    } else {
      // 尝试在解压目录下递归寻找 python.exe (针对可能的嵌套目录)
      try {
        List<FileSystemEntity> entities = Directory(extractPath).listSync(recursive: true);
        for (var entity in entities) {
          if (entity is File && basename(entity.path).toLowerCase() == (GetPlatform.isWindows ? 'python.exe' : 'python3')) {
            await colorizationSetting.savePythonPath(entity.path);
            break;
          }
        }
      } catch (e) {
        log.error('Find python executable failed: $e');
      }
    }

    pythonDownloadState = LoadingState.success;
    updateSafely([pythonDownloadId]);
    toast('success'.tr);
  }

  /// 下载上色 ONNX 模型文件
  Future<void> downloadModelFile(ColorizationModelType model) async {
    downloadProgress = '0%';
    downloadState = LoadingState.loading;
    updateSafely([downloadId]);

    final String modelDirPath = join(pathService.getVisibleDir().path, 'colorize_models');
    final String modelFilePath = join(modelDirPath, model.fileName);

    try {
      await Directory(modelDirPath).create(recursive: true);
    } catch (e) {
      log.error('Create model dir failed: $e');
    }

    try {
      await retry(
        () => ehRequest.download(
          url: model.downloadUrl,
          path: modelFilePath,
          receiveTimeout: 10 * 60 * 1000,
          onReceiveProgress: (count, total) {
            downloadProgress = (count / total * 100).toStringAsFixed(2) + '%';
            updateSafely([downloadId]);
          },
        ),
        maxAttempts: 5,
        onRetry: (error) => log.warning('Download colorization model failed, retry.'),
      );
    } on DioException catch (e) {
      log.error('Download colorization model failed after 5 times', e.errorMsg);
      downloadState = LoadingState.error;
      updateSafely([downloadId]);
      return;
    }

    log.info('Colorization model downloaded: ${model.displayName}');

    colorizationSetting.saveModelDirectoryPath(modelDirPath);

    downloadState = LoadingState.success;
    updateSafely([downloadId]);
  }

  Future<bool> colorize(int gid, SuperResolutionType type) async {
    if (type == SuperResolutionType.gallery) {
      GalleryDownloadInfo? galleryDownloadInfo = galleryDownloadService.galleryDownloadInfos[gid];
      if (galleryDownloadInfo?.downloadProgress.downloadStatus != DownloadStatus.downloaded) {
        toast('requireDownloadComplete'.tr);
        return false;
      }
    } else {
      ArchiveDownloadInfo? archiveDownloadInfo = archiveDownloadService.archiveDownloadInfos[gid];
      if (archiveDownloadInfo?.archiveStatus != ArchiveStatus.completed) {
        toast('requireDownloadComplete'.tr);
        return false;
      }
    }

    String? envError = await _checkEnvironment();
    if (envError != null) {
      toast(envError, isShort: false);
      log.error(envError);
      return false;
    }

    ColorizationInfo? info = get(gid, type);
    if (info?.status == ColorizationStatus.success) {
      return true;
    }
    if (info?.status == ColorizationStatus.running) {
      return true;
    }

    if (info == null) {
      List<GalleryImage> rawImages;
      if (type == SuperResolutionType.gallery) {
        rawImages = galleryDownloadService.galleryDownloadInfos[gid]!.images.cast();
      } else {
        rawImages = await archiveDownloadService.getUnpackedImages(gid);
      }

      info = ColorizationInfo(
        type,
        ColorizationStatus.running,
        List.generate(rawImages.length, (_) => ColorizationStatus.running),
      );
      _infoTable.putIfAbsent(gid, () => {});
      _infoTable[gid]![type.index] = info;
      await _saveColorizationInfo(gid, type, info);

      Directory(dirname(computeImageOutputAbsolutePath(rawImages[0].path!))).createSync(recursive: true);

      updateSafely(['$colorizationId::$gid']);
    }

    toast('${'startProcess'.tr}: $gid');
    executor.scheduleTask(0, () => _doColorize(gid, type));
    return true;
  }

  Future<void> pauseColorize(int gid, SuperResolutionType type) async {
    ColorizationInfo? info = get(gid, type);

    if (info == null ||
        info.status == ColorizationStatus.success ||
        info.status == ColorizationStatus.paused) {
      return;
    }

    bool? success = info.currentProcess?.kill();
    log.info('pause colorization: $gid $success');

    info.status = ColorizationStatus.paused;
    for (int i = 0; i < info.imageStatuses.length; i++) {
      if (info.imageStatuses[i] == ColorizationStatus.running) {
        info.imageStatuses[i] = ColorizationStatus.paused;
      }
    }
    await _saveColorizationInfo(gid, type, info);
    updateSafely(['$colorizationId::$gid']);
  }

  Future<void> deleteColorize(int gid, SuperResolutionType type) async {
    ColorizationInfo? info = get(gid, type);
    if (info == null) {
      return;
    }

    log.info('delete colorization: $gid');

    info.currentProcess?.kill();
    _infoTable[gid]?.remove(type.index);
    if (_infoTable[gid]?.isEmpty ?? false) {
      _infoTable.remove(gid);
    }
    await localConfigService.delete(configKey: ConfigEnum.colorizationInfo, subConfigKey: '${gid}_${type.index}');

    String dirPath;
    if (type == SuperResolutionType.gallery) {
      GalleryDownloadedData? gallery = galleryDownloadService.gallerys.firstWhereOrNull((g) => g.gid == gid);
      if (gallery == null) {
        return;
      }
      dirPath = join(galleryDownloadService.computeGalleryDownloadAbsolutePath(gallery.title, gallery.gid), imageDirName);
    } else {
      ArchiveDownloadedData? archive = archiveDownloadService.archives.firstWhereOrNull((a) => a.gid == gid);
      if (archive == null) {
        return;
      }
      dirPath = join(archiveDownloadService.computeArchiveUnpackingPath(archive.title, archive.gid), imageDirName);
    }

    Directory directory = Directory(dirPath);
    if (directory.existsSync()) {
      directory.deleteSync(recursive: true);
    }

    updateSafely(['$colorizationId::$gid']);
  }

  /// 检查上色所需环境：Python 可执行文件、关键依赖、模型文件、脚本文件
  Future<String?> _checkEnvironment() async {
    // 移动端：使用 Dart 原生 ONNX 推理，无需 Python，仅检查模型文件
    if (_useDartNative) {
      String? modelDir = colorizationSetting.modelDirectoryPath.value;
      if (modelDir == null) {
        return '未设置上色模型目录，请先下载模型';
      }
      String modelPath = join(modelDir, colorizationSetting.model.value.fileName);
      if (!await File(modelPath).exists()) {
        return '模型文件不存在: $modelPath，请先下载模型';
      }
      return null;
    }

    String pythonPath = colorizationSetting.pythonPath.value ?? (GetPlatform.isWindows ? 'python' : 'python3');

    // 1. 检查 Python 可执行文件是否存在
    if (colorizationSetting.pythonPath.value != null) {
      if (!await File(pythonPath).exists()) {
        return 'Python 可执行文件不存在: $pythonPath';
      }
    }

    // 2. 检查关键 Python 依赖
    try {
      ProcessResult result = await Process.run(
        pythonPath,
        ['-c', 'import onnxruntime, numpy, cv2, PIL; print("ok")'],
        runInShell: true,
      );
      if (result.exitCode != 0 || (result.stdout as String).trim() != 'ok') {
        return 'Python 依赖缺失，请在终端运行：\n$pythonPath -m pip install onnxruntime-gpu numpy opencv-python Pillow';
      }
    } catch (e) {
      return '无法调用 Python ($pythonPath)，请检查是否已安装 Python 3.8+ 并添加到系统 PATH';
    }

    // 3. 检查模型文件
    String? modelDir = colorizationSetting.modelDirectoryPath.value;
    if (modelDir == null) {
      return '未设置上色模型目录，请先下载模型';
    }
    String modelPath = join(modelDir, colorizationSetting.model.value.fileName);
    if (!await File(modelPath).exists()) {
      return '模型文件不存在: $modelPath，请先下载模型';
    }

    // 4. 检查脚本文件是否已提取
    if (_scriptPath == null || !await File(_scriptPath!).exists()) {
      return '上色脚本 colorize.py 未就绪，请重启应用后重试';
    }

    return null;
  }

  Future<void> _doColorize(int gid, SuperResolutionType type) async {
    List<GalleryImage> rawImages;
    if (type == SuperResolutionType.gallery) {
      rawImages = galleryDownloadService.galleryDownloadInfos[gid]!.images.cast();
    } else {
      rawImages = await archiveDownloadService.getUnpackedImages(gid);
    }

    ColorizationInfo info = get(gid, type)!;
    if (info.status != ColorizationStatus.running) {
      info.status = ColorizationStatus.running;
      await _saveColorizationInfo(gid, type, info);
      updateSafely(['$colorizationId::$gid']);
    }

    for (int i = 0; i < rawImages.length; i++) {
      if (get(gid, type) == null) {
        return;
      }

      if (info.status == ColorizationStatus.paused) {
        return;
      }

      if (info.imageStatuses[i] == ColorizationStatus.success) {
        continue;
      }

      if (_useDartNative) {
        if (colorizationSetting.modelDirectoryPath.value == null) {
          return;
        }
      } else {
        if (colorizationSetting.modelDirectoryPath.value == null || _scriptPath == null) {
          return;
        }
      }

      info.imageStatuses[i] = ColorizationStatus.running;
      await _saveColorizationInfo(gid, type, info);
      updateSafely(['$colorizationId::$gid']);

      bool success = await _handleImage(rawImages[i], info);
      if (!success) {
        pauseColorize(gid, type);
        return;
      }

      info.imageStatuses[i] = ColorizationStatus.success;
      log.download('colorize image ${rawImages[i].path} success');

      if (get(gid, type) != null) {
        await _saveColorizationInfo(gid, type, info);
      }
      updateSafely(['$colorizationId::$gid', '$colorizationImageId::$gid::$i']);
    }

    if (get(gid, type) != null && info.imageStatuses.every((status) => status == ColorizationStatus.success)) {
      info.status = ColorizationStatus.success;
      await _saveColorizationInfo(gid, type, info);
      updateSafely(['$colorizationId::$gid']);
      log.info('colorize success, gid:$gid');
    }
  }

  Future<bool> _handleImage(GalleryImage rawImage, ColorizationInfo info) async {
    if (extension(rawImage.path!) == '.gif') {
      String inputAbsolutePath = GalleryDownloadService.computeImageDownloadAbsolutePathFromRelativePath(rawImage.path!);
      String outputAbsolutePath = computeImageOutputAbsolutePath(rawImage.path!);
      try {
        File(inputAbsolutePath).copySync(outputAbsolutePath);
      } catch (e, s) {
        log.error('copy gif image failed', e, s);
        return false;
      }
      return true;
    }

    // 移动端：使用 Dart 原生 ONNX 推理
    if (_useDartNative) {
      return await _handleImageDart(rawImage);
    }

    Process? process;
    try {
      process = await _callProcess(rawImage);
    } on Exception catch (e) {
      toast('internalError'.tr + e.toString(), isShort: false);
      log.error(e);
      log.uploadError(e, extraInfos: {'rawImage': rawImage});
      return false;
    } on Error catch (e) {
      toast('internalError'.tr + e.toString(), isShort: false);
      log.error(e);
      log.uploadError(e, extraInfos: {'rawImage': rawImage});
      return false;
    }

    info.currentProcess = process;

    final StringBuffer outputBuffer = StringBuffer();
    void appendOutput(List<int> event) {
      final String text = utf8.decode(event, allowMalformed: true).trim();
      if (text.isNotEmpty) {
        outputBuffer.writeln(text);
        log.trace(text);
      }
    }

    process.stdout.listen(appendOutput);
    process.stderr.listen(appendOutput);

    int exitCode = await process.exitCode;

    /// pause and kill the process
    if (exitCode == -1 || exitCode == -15 || exitCode == 15) {
      return false;
    }

    if (exitCode != 0) {
      String output = outputBuffer.toString().trim();
      String errorMsg = '${'internalError'.tr} exitCode:$exitCode\n$output';
      toast(errorMsg, isShort: false);
      log.error(errorMsg);
      log.uploadError(
        Exception('Process Error'),
        extraInfos: {'rawImage': rawImage, 'exitCode': exitCode, 'output': output},
      );
      return false;
    }

    return true;
  }

  Future<Process> _callProcess(GalleryImage rawImage) {
    log.download('start to colorize image ${rawImage.path}');

    String inputRelativePath = rawImage.path!;
    String outputRelativePath = computeImageOutputRelativePath(rawImage.path!);

    String pythonPath = colorizationSetting.pythonPath.value ?? (GetPlatform.isWindows ? 'python' : 'python3');
    String modelPath = join(
      colorizationSetting.modelDirectoryPath.value!,
      colorizationSetting.model.value.fileName,
    );

    log.trace(
      'Run: $pythonPath "$_scriptPath" '
      '-i $inputRelativePath '
      '-o $outputRelativePath '
      '-m "$modelPath" '
      '--type ${colorizationSetting.model.value.scriptType} '
      '--device ${colorizationSetting.useGPU.value ? 'cuda' : 'cpu'}',
    );

    return Process.start(
      pythonPath,
      [
        _scriptPath!,
        '-i',
        inputRelativePath,
        '-o',
        outputRelativePath,
        '-m',
        modelPath,
        '--type',
        colorizationSetting.model.value.scriptType,
        '--device',
        colorizationSetting.useGPU.value ? 'cuda' : 'cpu',
      ],
      workingDirectory: pathService.getVisibleDir().path,
      runInShell: true,
    );
  }

  /// 移动端：使用 Dart 原生 ONNX Runtime 上色（不需要 Python）
  /// 使用 compute() 在后台 isolate 执行，避免阻塞主线程
  Future<bool> _handleImageDart(GalleryImage rawImage) async {
    log.download('start to colorize image (Dart native) ${rawImage.path}');

    final String inputAbsolutePath =
        GalleryDownloadService.computeImageDownloadAbsolutePathFromRelativePath(rawImage.path!);
    final String outputAbsolutePath = computeImageOutputAbsolutePath(rawImage.path!);
    final String modelPath = join(
      colorizationSetting.modelDirectoryPath.value!,
      colorizationSetting.model.value.fileName,
    );

    final ColorizeModelType type = colorizationSetting.model.value.scriptType == 'deoldify'
        ? ColorizeModelType.deoldify
        : ColorizeModelType.ddcolor;

    try {
      final params = ColorizeParams(
        inputPath: inputAbsolutePath,
        outputPath: outputAbsolutePath,
        modelPath: modelPath,
        modelType: type,
        threads: colorizationSetting.numThreads.value ?? 2,
      );

      // 使用 compute() 在后台 isolate 执行，避免阻塞主线程
      final bool success = await compute(
        _colorizeInIsolate,
        params,
      );

      if (!success) {
        String errorMsg = '上色失败: ${rawImage.path}';
        toast(errorMsg, isShort: false);
        log.error(errorMsg);
        return false;
      }

      return true;
    } catch (e, s) {
      String errorMsg = '上色失败: ${rawImage.path}\n错误: $e';
      toast(errorMsg, isShort: false);
      log.error('Dart colorization failed', e, s);
      log.uploadError(e, extraInfos: {'rawImage': rawImage});
      return false;
    }
  }

  /// 在 isolate 中执行上色（compute() 的入口函数）
  static Future<bool> _colorizeInIsolate(ColorizeParams params) async {
    if (params.modelType == ColorizeModelType.deoldify) {
      return await ColorizeUpscaler.colorizeDeOldify(params);
    } else {
      return await ColorizeUpscaler.colorizeDDColor(params);
    }
  }

  void _checkInfoSourceExists() {
    List<({int gid, SuperResolutionType type})> toDelete = [];

    _infoTable.forEach((gid, typeMap) {
      typeMap.forEach((typeIndex, info) {
        SuperResolutionType type = SuperResolutionType.values[typeIndex];
        if (type == SuperResolutionType.gallery && galleryDownloadService.galleryDownloadInfos.containsKey(gid)) {
          return;
        }
        if (type == SuperResolutionType.archive && archiveDownloadService.archiveDownloadInfos.containsKey(gid)) {
          return;
        }
        log.error('Colorization info source not exists: gid=$gid, type=$type');
        toDelete.add((gid: gid, type: type));
      });
    });

    for (var item in toDelete) {
      deleteColorize(item.gid, item.type);
    }
  }

  // ============ LocalConfig 持久化 ============

  Future<void> _loadAllColorizationInfo() async {
    List<LocalConfig> configs = await localConfigService.readWithAllSubKeys(configKey: ConfigEnum.colorizationInfo);
    for (var config in configs) {
      try {
        List parts = config.subConfigKey.split('_');
        int gid = int.parse(parts[0]);
        int typeIndex = int.parse(parts[1]);
        Map map = jsonDecode(config.value);

        ColorizationInfo info = ColorizationInfo(
          SuperResolutionType.values[typeIndex],
          ColorizationStatus.values[map['status']],
          (map['imageStatuses'] as List).map((e) => ColorizationStatus.values[e]).toList(),
        );
        _infoTable.putIfAbsent(gid, () => {});
        _infoTable[gid]![typeIndex] = info;
      } catch (e) {
        log.error('Parse colorization info failed: $e');
      }
    }
  }

  Future<void> _saveColorizationInfo(int gid, SuperResolutionType type, ColorizationInfo info) async {
    String json = jsonEncode({
      'status': info.status.index,
      'imageStatuses': info.imageStatuses.map((e) => e.index).toList(),
    });
    await localConfigService.write(
      configKey: ConfigEnum.colorizationInfo,
      subConfigKey: '${gid}_${type.index}',
      value: json,
    );
  }

  // ============ 路径计算 ============

  String computeImageOutputAbsolutePath(String rawImagePath) {
    return join(pathService.getVisibleDir().path, computeImageOutputRelativePath(rawImagePath));
  }

  String computeImageOutputRelativePath(String rawImagePath) {
    return join(computeImageOutputDirPath(rawImagePath), basenameWithoutExtension(rawImagePath) + (extension(rawImagePath) == '.gif' ? '.gif' : '.png'));
  }

  String computeImageOutputDirPath(String rawImagePath) {
    return join(dirname(rawImagePath), imageDirName);
  }
}

class ColorizationInfo {
  Process? currentProcess;

  SuperResolutionType type;

  ColorizationStatus status;

  List<ColorizationStatus> imageStatuses;

  ColorizationInfo(this.type, this.status, this.imageStatuses);
}

enum ColorizationStatus { paused, running, success }
