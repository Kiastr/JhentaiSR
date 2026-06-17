import 'dart:convert';

import 'package:get/get.dart';
import 'package:jhentai/src/enum/config_enum.dart';
import 'package:jhentai/src/service/log.dart';

import '../service/jh_service.dart';

DeOldifySetting deOldifySetting = DeOldifySetting();

class DeOldifySetting with JHLifeCircleBeanWithConfigStorage implements JHLifeCircleBean {
  RxBool enableDeOldify = false.obs;
  RxString modelType = 'stable'.obs;
  RxnString modelDirectoryPath = RxnString(null);

  @override
  ConfigEnum get configEnum => ConfigEnum.deOldifySetting;

  @override
  void applyBeanConfig(String configString) {
    Map map = jsonDecode(configString);

    enableDeOldify.value = map['enableDeOldify'] ?? enableDeOldify.value;
    modelType.value = map['modelType'] ?? modelType.value;
    modelDirectoryPath.value = map['modelDirectoryPath'];
  }

  @override
  String toConfigString() {
    return jsonEncode({
      'enableDeOldify': enableDeOldify.value,
      'modelType': modelType.value,
      'modelDirectoryPath': modelDirectoryPath.value,
    });
  }

  @override
  Future<void> doInitBean() async {}

  @override
  void doAfterBeanReady() {}

  Future<void> saveEnableDeOldify(bool value) async {
    log.debug('saveEnableDeOldify:$value');
    enableDeOldify.value = value;
    await saveBeanConfig();
  }

  Future<void> saveModelType(String value) async {
    log.debug('saveModelType:$value');
    modelType.value = value;
    await saveBeanConfig();
  }

  Future<void> saveModelDirectoryPath(String? value) async {
    log.debug('saveModelDirectoryPath:$value');
    modelDirectoryPath.value = value;
    await saveBeanConfig();
  }
}
