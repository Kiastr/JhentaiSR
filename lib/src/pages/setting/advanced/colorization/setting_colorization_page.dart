import 'package:file_picker/file_picker.dart';
import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:get/get.dart';
import 'package:jhentai/src/extension/widget_extension.dart';
import 'package:jhentai/src/setting/preference_setting.dart';
import 'package:jhentai/src/utils/toast_util.dart';
import 'package:url_launcher/url_launcher_string.dart';

import '../../../../service/colorization_service.dart';
import '../../../../setting/colorization_setting.dart';
import '../../../../service/log.dart';
import '../../../../widget/loading_state_indicator.dart';

class SettingColorizationPage extends StatelessWidget {
  const SettingColorizationPage({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        centerTitle: true,
        title: Text('colorization'.tr),
        actions: [
          IconButton(
            icon: const Icon(Icons.help),
            onPressed: () => launchUrlString(
              preferenceSetting.locale.value.languageCode == 'zh'
                  ? 'https://github.com/ColorfulSoft/DeOldify.NET'
                  : 'https://github.com/ColorfulSoft/DeOldify.NET',
            ),
          )
        ],
      ),
      body: Obx(
        () => ListView(
          padding: const EdgeInsets.only(top: 16),
          children: [
            _buildInstruction(),
            _buildPythonPath(),
            _buildDownloadPythonEnv(),
            _buildModelDirectoryPath(),
            _buildModelType(),
            _buildRenderFactor(),
          ],
        ).withListTileTheme(context),
      ),
    );
  }

  Widget _buildInstruction() {
    return Padding(
      padding: const EdgeInsets.symmetric(vertical: 4, horizontal: 16),
      child: Text(
        'colorizationInstruction'.tr,
        style: TextStyle(
          fontSize: 13,
          fontWeight: FontWeight.bold,
          color: UIConfig.primaryColor(context),
        ),
      ),
    );
  }

  Widget _buildPythonPath() {
    return ListTile(
      title: Text('pythonPath'.tr),
      subtitle: Text(colorizationSetting.pythonPath.value ?? 'default'.tr),
      trailing: const Icon(Icons.keyboard_arrow_right),
      onTap: () async {
        FilePickerResult? result;
        try {
          result = await FilePicker.platform.pickFiles(
            type: FileType.custom,
            allowedExtensions: ['exe', 'py', ''],
          );
        } on Exception catch (e) {
          log.error('Pick python executable path failed', e);
          log.uploadError(e);
          toast('internalError'.tr);
        }

        if (result == null) {
          return;
        }

        colorizationSetting.savePythonPath(result.files.first.path);
      },
    );
  }

  Widget _buildDownloadPythonEnv() {
    return ListTile(
      title: Text('downloadPythonEnv'.tr),
      subtitle: GetBuilder<ColorizationService>(
        id: ColorizationService.pythonDownloadId,
        builder: (service) => service.pythonDownloadState == LoadingState.loading
            ? Text('${'downloading'.tr} ${service.pythonDownloadProgress}')
            : Text('downloadPythonEnvHint'.tr),
      ),
      trailing: GetBuilder<ColorizationService>(
        id: ColorizationService.pythonDownloadId,
        builder: (service) => service.pythonDownloadState == LoadingState.loading
            ? const CupertinoActivityIndicator()
            : const Icon(Icons.download),
      ),
      onTap: () {
        if (colorizationService.pythonDownloadState == LoadingState.loading) {
          return;
        }
        colorizationService.downloadPythonEnv();
      },
    );
  }

  Widget _buildModelDirectoryPath() {
    return ListTile(
      title: Text('modelDirectoryPath'.tr),
      subtitle: Text(colorizationSetting.modelDirectoryPath.value ?? ''),
      trailing: const Icon(Icons.keyboard_arrow_right),
      onTap: () async {
        String? result;
        try {
          result = await FilePicker.platform.getDirectoryPath();
        } on Exception catch (e) {
          log.error('Pick model directory path failed', e);
          log.uploadError(e);
          toast('internalError'.tr);
        }

        if (result == null) {
          return;
        }

        colorizationSetting.saveModelDirectoryPath(result);
      },
    );
  }

  Widget _buildModelType() {
    return ListTile(
      title: Text('modelType'.tr),
      subtitle: GetBuilder<ColorizationService>(
        id: ColorizationService.downloadId,
        builder: (service) => service.downloadState == LoadingState.loading
            ? Text('${'downloading'.tr} ${service.downloadProgress}')
            : service.downloadState == LoadingState.success
                ? Text('downloaded'.tr)
                : const SizedBox(),
      ),
      trailing: Row(
        mainAxisSize: MainAxisSize.min,
        children: [
          GetBuilder<ColorizationService>(
            id: ColorizationService.downloadId,
            builder: (service) => service.downloadState == LoadingState.loading
                ? IconButton(icon: const CupertinoActivityIndicator(), onPressed: () {}, enableFeedback: false)
                : IconButton(
                    icon: const Icon(Icons.download),
                    padding: EdgeInsets.zero,
                    onPressed: () {
                      if (service.downloadState == LoadingState.loading) {
                        return;
                      }
                      service.downloadModelFile(colorizationSetting.model.value);
                    },
                  ),
          ),
          const SizedBox(width: 8),
          DropdownButton<ColorizationModelType>(
            value: colorizationSetting.model.value,
            elevation: 4,
            onChanged: (ColorizationModelType? newValue) => colorizationSetting.saveModel(newValue!),
            items: ColorizationModelType.values
                .map((m) => DropdownMenuItem(child: Text(m.displayName), value: m))
                .toList(),
          )
        ],
      ),
    );
  }

  Widget _buildRenderFactor() {
    return ListTile(
      title: Text('renderFactor'.tr),
      subtitle: Text('renderFactorHint'.tr),
      trailing: DropdownButton<int>(
        value: colorizationSetting.renderFactor.value,
        elevation: 4,
        alignment: AlignmentDirectional.centerEnd,
        onChanged: (int? newValue) => colorizationSetting.saveRenderFactor(newValue!),
        items: const [
          DropdownMenuItem(child: Text('7'), value: 7),
          DropdownMenuItem(child: Text('11'), value: 11),
          DropdownMenuItem(child: Text('15'), value: 15),
          DropdownMenuItem(child: Text('19'), value: 19),
          DropdownMenuItem(child: Text('23'), value: 23),
          DropdownMenuItem(child: Text('27'), value: 27),
          DropdownMenuItem(child: Text('31'), value: 31),
          DropdownMenuItem(child: Text('35'), value: 35),
          DropdownMenuItem(child: Text('39'), value: 39),
        ],
      ),
    );
  }
}
