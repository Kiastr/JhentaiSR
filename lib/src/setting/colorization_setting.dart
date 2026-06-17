import 'dart:convert';

import 'package:get/get.dart';
import 'package:jhentai/src/enum/config_enum.dart';
import 'package:jhentai/src/service/log.dart';

import '../service/jh_service.dart';

ColorizationSetting colorizationSetting = ColorizationSetting();

/// DeOldify 上色设置
///
/// 基于 DeOldify ONNX 模型，通过 Python + onnxruntime 进行推理。
/// 支持 Artistic（色彩鲜艳）和 Stable（更自然稳定）两种模型。
class ColorizationSetting with JHLifeCircleBeanWithConfigStorage implements JHLifeCircleBean {
  /// Python 可执行文件路径，为 null 时使用系统默认 python
  RxnString pythonPath = RxnString();

  /// 模型文件所在目录路径
  RxnString modelDirectoryPath = RxnString();

  /// 当前选择的模型类型
  Rx<ColorizationModelType> model = Rx<ColorizationModelType>(ColorizationModelType.Artistic);

  /// 渲染因子（render factor），控制模型内部处理分辨率，越大越清晰但越慢
  /// DeOldify 模型以 renderFactor * 2 的分辨率进行推理，默认 19（即 38px？实际 ONNX 模型固定 256x256，此值保留以备扩展）
  RxInt renderFactor = 19.obs;

  @override
  ConfigEnum get configEnum => ConfigEnum.colorizationSetting;

  @override
  void applyBeanConfig(String configString) {
    Map map = jsonDecode(configString);

    pythonPath.value = map['pythonPath'];
    modelDirectoryPath.value = map['modelDirectoryPath'];
    model.value = map['model'] == null ? ColorizationModelType.Artistic : ColorizationModelType.values[map['model']];
    renderFactor.value = map['renderFactor'] ?? renderFactor.value;
  }

  @override
  String toConfigString() {
    return jsonEncode({
      'pythonPath': pythonPath.value,
      'modelDirectoryPath': modelDirectoryPath.value,
      'model': model.value.index,
      'renderFactor': renderFactor.value,
    });
  }

  @override
  Future<void> doInitBean() async {}

  @override
  void doAfterBeanReady() {}

  Future<void> savePythonPath(String? pythonPath) async {
    log.debug('savePythonPath:$pythonPath');
    this.pythonPath.value = pythonPath;
    await saveBeanConfig();
  }

  Future<void> saveModelDirectoryPath(String? modelDirectoryPath) async {
    log.debug('saveModelDirectoryPath:$modelDirectoryPath');
    this.modelDirectoryPath.value = modelDirectoryPath;
    await saveBeanConfig();
  }

  Future<void> saveModel(ColorizationModelType model) async {
    log.debug('saveColorizationModel:$model');
    this.model.value = model;
    await saveBeanConfig();
  }

  Future<void> saveRenderFactor(int renderFactor) async {
    log.debug('saveRenderFactor:$renderFactor');
    this.renderFactor.value = renderFactor;
    await saveBeanConfig();
  }
}

/// DeOldify 模型类型
enum ColorizationModelType {
  Artistic(
    'Artistic',
    'deoldify_artistic.onnx',
    'https://github.com/instant-high/deoldify-onnx/releases/download/deoldify-onnx/deoldify.onnx',
    '色彩鲜艳、细节丰富，但偶有瑕疵',
    'Vivid colors and rich details, occasional artifacts',
  ),
  Stable(
    'Stable',
    'deoldify_stable.onnx',
    'https://huggingface.co/Jonny001/deepfake/resolve/main/deoldify_stable.onnx',
    '更自然稳定，人像/风景效果更好',
    'More natural and stable, better for portraits/landscapes',
  );

  const ColorizationModelType(
    this.displayName,
    this.fileName,
    this.downloadUrl,
    this.descriptionZh,
    this.descriptionEn,
  );

  final String displayName;

  /// 下载后保存的文件名
  final String fileName;

  final String downloadUrl;

  final String descriptionZh;

  final String descriptionEn;
}
