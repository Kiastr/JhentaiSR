import 'package:file_picker/file_picker.dart';
import 'package:flutter/material.dart';
import 'package:get/get.dart';
import 'package:jhentai/src/extension/widget_extension.dart';
import 'package:jhentai/src/setting/deoldify_setting.dart';
import 'package:jhentai/src/utils/deoldify/deoldify_service.dart';
import 'package:jhentai/src/utils/toast_util.dart';
import 'package:jhentai/src/utils/byte_util.dart';
import '../../../../service/log.dart';

class SettingDeOldifyPage extends StatefulWidget {
  const SettingDeOldifyPage({Key? key}) : super(key: key);

  @override
  State<SettingDeOldifyPage> createState() => _SettingDeOldifyPageState();
}

class _SettingDeOldifyPageState extends State<SettingDeOldifyPage> {
  String _cacheSize = '...';

  @override
  void initState() {
    super.initState();
    _loadCacheSize();
  }

  Future<void> _loadCacheSize() async {
    final size = await DeOldifyService.instance.getCacheSize();
    if (mounted) {
      setState(() {
        _cacheSize = byte2String(size.toDouble());
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        centerTitle: true,
        title: const Text('DeOldify'),
      ),
      body: Obx(
        () => ListView(
          padding: const EdgeInsets.only(top: 16),
          children: [
            _buildEnableDeOldify(),
            _buildModelType(),
            _buildModelDirectoryPath(),
            _buildClearCache(),
          ],
        ).withListTileTheme(context),
      ),
    );
  }

  Widget _buildEnableDeOldify() {
    return SwitchListTile(
      title: const Text('DeOldify'),
      value: deOldifySetting.enableDeOldify.value,
      onChanged: deOldifySetting.saveEnableDeOldify,
    );
  }

  Widget _buildModelType() {
    return ListTile(
      title: const Text('Model Type'),
      trailing: DropdownButton<String>(
        value: deOldifySetting.modelType.value,
        elevation: 4,
        onChanged: (String? newValue) => deOldifySetting.saveModelType(newValue!),
        items: const [
          DropdownMenuItem(child: Text('Stable'), value: 'stable'),
          DropdownMenuItem(child: Text('Artistic'), value: 'artistic'),
        ],
      ),
    );
  }

  Widget _buildModelDirectoryPath() {
    return ListTile(
      title: const Text('Model Directory Path'),
      subtitle: Text(deOldifySetting.modelDirectoryPath.value ?? ''),
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

        deOldifySetting.saveModelDirectoryPath(result);
      },
    );
  }

  Widget _buildClearCache() {
    return ListTile(
      title: const Text('Clear Cache'),
      subtitle: Text('longPress2Clear'.tr),
      trailing: Text(
        _cacheSize,
        style: TextStyle(
          color: Theme.of(context).colorScheme.secondary,
          fontWeight: FontWeight.w500,
        ),
      ),
      onLongPress: () async {
        await DeOldifyService.instance.clearCache();
        await _loadCacheSize();
        toast('clearSuccess'.tr, isCenter: false);
      },
    );
  }
}
