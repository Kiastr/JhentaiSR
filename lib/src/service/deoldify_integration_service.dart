import 'dart:io';

import 'package:get/get.dart';
import 'package:jhentai/src/service/jh_service.dart';
import 'package:jhentai/src/utils/deoldify/deoldify_service.dart';

DeOldifyIntegrationService deOldifyIntegrationService = DeOldifyIntegrationService();

class DeOldifyIntegrationService extends GetxController with JHLifeCircleBeanErrorCatch implements JHLifeCircleBean {
  @override
  Future<void> doInitBean() async {
    Get.put(this, permanent: true);

    if (Platform.isWindows) {
      await DeOldifyService.instance.init();
    }
  }

  @override
  Future<void> doAfterBeanReady() async {}
}
