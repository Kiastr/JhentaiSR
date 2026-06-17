DeOldify.NET 图像上色模块
========================

本目录包含 DeOldify.NET 的可执行文件，用于对黑白图片进行 AI 上色处理。

文件说明
--------

本目录应包含以下文件：
  - deoldify_stable.exe    Stable 模型版本（适合真实照片）
  - deoldify_artistic.exe  Artistic 模型版本（适合艺术/动漫风格）

这些 exe 文件已由 GitHub Actions 自动编译并包含在构建产物中。

模型文件
--------

模型文件较大（每个约 300MB），不包含在应用中。用户需要手动下载并放置在指定目录。

下载地址：
  https://github.com/ColorfulSoft/DeOldify.NET/releases/tag/Weights

需要下载的文件：
  - ColorizeStable_gen.model    (Stable 模型)
  - ColorizeArtistic_gen.model  (Artistic 模型)

使用方法
--------

1. 在应用中打开：高级设置 -> DeOldify
2. 开启 "DeOldify" 开关
3. 选择模型类型（Stable 或 Artistic）
4. 点击 "Model Directory Path" 选择包含模型文件的目录
5. 长按 "Clear Cache" 可清除上色缓存

目录结构示例
------------

用户指定的模型目录（例如 D:\DeOldify\models\）：
  D:\DeOldify\models\
  ├── ColorizeArtistic_gen.model
  └── ColorizeStable_gen.model

应用会自动在以下位置查找 deoldify exe：
  1. 应用目录/deoldify/deoldify_stable.exe (或 deoldify_artistic.exe)
  2. 模型目录/deoldify_stable.exe (或 deoldify_artistic.exe)
  3. 模型上级目录/deoldify_stable.exe (或 deoldify_artistic.exe)
  4. 应用目录/deoldify_stable.exe (或 deoldify_artistic.exe)

注意事项
--------

- DeOldify 功能仅在 Windows 平台上可用
- 处理图片时需要一定时间，请耐心等待
- 处理结果会缓存，同一图片不会重复处理
- 如果同时开启了 Anime4K 超分辨率，会先执行超分再执行上色
