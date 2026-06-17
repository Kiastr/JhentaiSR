import 'dart:convert';
import 'dart:io';

import 'package:dio/dio.dart';
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
import '../utils/eh_executor.dart';
import '../utils/toast_util.dart';
import '../widget/loading_state_indicator.dart';

ColorizationService colorizationService = ColorizationService();

/// DeOldify 上色服务
///
/// 通过调用外部 Python 脚本（colorize.py + onnxruntime）对已下载的画廊/档案图片进行批量上色。
/// 采用 LocalConfig 键值表持久化上色状态，避免 Drift 代码生成。
/// 仅桌面端（Windows/macOS/Linux）可用。
class ColorizationService extends GetxController with JHLifeCircleBeanErrorCatch implements JHLifeCircleBean {
  static const String downloadId = 'colorizationDownloadId';
  static const String colorizationId = 'colorizationId';
  static const String colorizationImageId = 'colorizationImageId';

  LoadingState downloadState = LoadingState.idle;
  String downloadProgress = '0%';

  EHExecutor executor = EHExecutor(concurrency: 1);

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
      if (!await scriptFile.exists()) {
        final data = await rootBundle.load('assets/colorize/colorize.py');
        await scriptFile.writeAsBytes(data.buffer.asUint8List());
      }
    } catch (e) {
      log.error('Extract colorize.py failed: $e');
    }
  }

  ColorizationInfo? get(int gid, SuperResolutionType type) {
    return _infoTable[gid]?[type.index];
  }

  /// 下载 DeOldify ONNX 模型文件
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
      /// cancelled
      if (get(gid, type) == null) {
        return;
      }

      if (info.status == ColorizationStatus.paused) {
        return;
      }

      if (info.imageStatuses[i] == ColorizationStatus.success) {
        continue;
      }

      if (colorizationSetting.modelDirectoryPath.value == null || _scriptPath == null) {
        return;
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

    process.stderr.listen((event) {
      log.trace(String.fromCharCodes(event).trim());
    });

    int exitCode = await process.exitCode;

    /// pause and kill the process
    if (exitCode == -1 || exitCode == -15 || exitCode == 15) {
      return false;
    }

    if (exitCode != 0) {
      toast('${'internalError'.tr} exitCode:$exitCode', isShort: false);
      log.error('${'internalError'.tr} exitCode:$exitCode');
      log.uploadError(
        Exception('Process Error'),
        extraInfos: {'rawImage': rawImage, 'exitCode': exitCode},
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
      '-r ${colorizationSetting.renderFactor.value}',
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
        '-r',
        colorizationSetting.renderFactor.value.toString(),
      ],
      workingDirectory: pathService.getVisibleDir().path,
      runInShell: true,
    );
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
