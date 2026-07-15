import 'dart:convert';

import 'package:get/get.dart';
import 'package:jhentai/src/enum/config_enum.dart';
import 'package:jhentai/src/service/log.dart';

import '../service/jh_service.dart';

ColorizationSetting colorizationSetting = ColorizationSetting();

/// 上色设置
class ColorizationSetting with JHLifeCircleBeanWithConfigStorage implements JHLifeCircleBean {
  static const String pythonEnvDownloadUrl = 'https://github.com/Kiastr/JhentaiSR/releases/download/python-env-v1/python_env_ddcolor.zip';

  /// Python 可执行文件路径，为 null 时使用系统默认 python
  RxnString pythonPath = RxnString();

  /// 模型文件所在目录路径
  RxnString modelDirectoryPath = RxnString();

  /// 当前选择的模型类型
  Rx<ColorizationModelType> model = Rx<ColorizationModelType>(ColorizationModelType.DeOldifyInt8);

  /// 渲染因子（render factor），控制模型内部处理分辨率
  RxInt renderFactor = 19.obs;

  /// 是否使用 GPU 加速（桌面端 CUDA）
  RxBool useGPU = true.obs;

  /// 推理线程数（桌面端可选）
  RxnInt numThreads = RxnInt(2);

  /// 移动端是否使用 NNAPI 加速（GPU/NPU 统一抽象，不支持时自动回退 CPU）
  RxBool useNNAPI = true.obs;

  @override
  ConfigEnum get configEnum => ConfigEnum.colorizationSetting;

  @override
  void applyBeanConfig(String configString) {
    Map map = jsonDecode(configString);

    pythonPath.value = map['pythonPath'];
    modelDirectoryPath.value = map['modelDirectoryPath'];
    model.value = map['model'] == null ? ColorizationModelType.DeOldifyInt8 : ColorizationModelType.values[map['model']];
    renderFactor.value = map['renderFactor'] ?? 19;
    useGPU.value = map['useGPU'] ?? true;
    numThreads.value = map['numThreads'] ?? 2;
    useNNAPI.value = map['useNNAPI'] ?? true;
  }

  @override
  String toConfigString() {
    return jsonEncode({
      'pythonPath': pythonPath.value,
      'modelDirectoryPath': modelDirectoryPath.value,
      'model': model.value.index,
      'renderFactor': renderFactor.value,
      'useGPU': useGPU.value,
      'numThreads': numThreads.value,
      'useNNAPI': useNNAPI.value,
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

  Future<void> saveUseGPU(bool useGPU) async {
    log.debug('saveUseGPU:$useGPU');
    this.useGPU.value = useGPU;
    await saveBeanConfig();
  }

  Future<void> saveNumThreads(int numThreads) async {
    log.debug('saveNumThreads:$numThreads');
    this.numThreads.value = numThreads;
    await saveBeanConfig();
  }

  Future<void> saveUseNNAPI(bool useNNAPI) async {
    log.debug('saveUseNNAPI:$useNNAPI');
    this.useNNAPI.value = useNNAPI;
    await saveBeanConfig();
  }
}

/// 上色模型类型
enum ColorizationModelType {
  Artistic(
    'DeOldify Artistic',
    'deoldify_artistic.onnx',
    'https://github.com/instant-high/deoldify-onnx/releases/download/deoldify-onnx/deoldify.onnx',
    '色彩鲜艳、细节丰富，但偶有瑕疵',
    'Vivid colors and rich details, occasional artifacts',
    'deoldify',
  ),
  Stable(
    'DeOldify Stable',
    'deoldify_stable.onnx',
    'https://huggingface.co/Jonny001/deepfake/resolve/main/deoldify_stable.onnx',
    '更自然稳定，人像/风景效果更好',
    'More natural and stable, better for portraits/landscapes',
    'deoldify',
  ),
  DeOldifyInt8(
    'DeOldify Int8',
    'deoldify_int8.onnx',
    'https://github.com/Kiastr/AiColorize/releases/download/models/deoldify_int8.onnx',
    'int8 量化版 DeOldify，体积小、速度快，色彩鲜活，默认推荐',
    'int8 quantized DeOldify, small and fast, vivid colors, default',
    'deoldify',
  ),
  DDColorTiny(
    'DDColor Tiny',
    'ddcolor_tiny.onnx',
    'https://huggingface.co/facefusion/models-3.0.0/resolve/main/ddcolor.onnx',
    'DDColor Tiny 版本，速度快，效果好',
    'DDColor Tiny version, fast and good quality',
    'ddcolor',
  ),
  DDColorInt8(
    'DDColor Int8',
    'ddcolor-int8.onnx',
    'https://github.com/Kiastr/AiColorize/releases/download/models/ddcolor-int8.onnx',
    'int8 量化版，体积最小、速度最快，安卓首选',
    'int8 quantized, smallest and fastest, recommended on Android',
    'ddcolor',
  );

  const ColorizationModelType(
    this.displayName,
    this.fileName,
    this.downloadUrl,
    this.descriptionZh,
    this.descriptionEn,
    this.scriptType,
  );

  final String displayName;

  /// 下载后保存的文件名
  final String fileName;

  final String downloadUrl;

  final String descriptionZh;

  final String descriptionEn;

  final String scriptType;
}
