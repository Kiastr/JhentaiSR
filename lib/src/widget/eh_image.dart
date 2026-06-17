import 'package:animate_do/animate_do.dart';
import 'package:extended_image/extended_image.dart';
import 'package:flutter/foundation.dart';
import 'package:flutter/material.dart';
import 'package:get/get.dart';
import 'package:jhentai/src/config/ui_config.dart';
import 'package:jhentai/src/extension/widget_extension.dart';
import 'package:jhentai/src/model/gallery_image.dart';
import 'package:jhentai/src/setting/advanced_setting.dart';
import 'package:jhentai/src/setting/style_setting.dart';
import 'package:jhentai/src/setting/read_setting.dart';
import 'package:jhentai/src/utils/anime4k/anime4k_service.dart';
import 'package:jhentai/src/utils/deoldify/deoldify_service.dart';
import 'package:jhentai/src/setting/deoldify_setting.dart';
import 'dart:io' as io;

import '../service/gallery_download_service.dart';

typedef LoadingProgressWidgetBuilder = Widget Function(double);
typedef FailedWidgetBuilder = Widget Function(ExtendedImageState state);
typedef DownloadingWidgetBuilder = Widget Function();
typedef PausedWidgetBuilder = Widget Function();
typedef LoadingWidgetBuilder = Widget Function();
typedef CompletedWidgetBuilder = Widget? Function(ExtendedImageState state);

class EHImage extends StatefulWidget {
  final GalleryImage galleryImage;
  final bool autoLayout;
  final double? containerHeight;
  final double? containerWidth;
  final Color? containerColor;
  final BoxFit fit;
  final bool enableSlideOutPage;
  final BorderRadius borderRadius;
  final Object? heroTag;
  final bool clearMemoryCacheWhenDispose;
  final List<BoxShadow>? shadows;
  final bool forceFadeIn;
  final int? maxBytes;

  final LoadingProgressWidgetBuilder? loadingProgressWidgetBuilder;
  final FailedWidgetBuilder? failedWidgetBuilder;
  final DownloadingWidgetBuilder? downloadingWidgetBuilder;
  final PausedWidgetBuilder? pausedWidgetBuilder;
  final LoadingWidgetBuilder? loadingWidgetBuilder;
  final CompletedWidgetBuilder? completedWidgetBuilder;

  const EHImage({
    Key? key,
    required this.galleryImage,
    this.autoLayout = false,
    this.containerHeight,
    this.containerWidth,
    this.containerColor,
    this.fit = BoxFit.contain,
    this.enableSlideOutPage = false,
    this.borderRadius = BorderRadius.zero,
    this.heroTag,
    this.clearMemoryCacheWhenDispose = false,
    this.shadows,
    this.forceFadeIn = false,
    this.maxBytes,
    this.loadingProgressWidgetBuilder,
    this.failedWidgetBuilder,
    this.downloadingWidgetBuilder,
    this.pausedWidgetBuilder,
    this.loadingWidgetBuilder,
    this.completedWidgetBuilder,
  }) : super(key: key);

  const EHImage.autoLayout({
    Key? key,
    required this.galleryImage,
    this.autoLayout = true,
    this.containerHeight,
    this.containerWidth,
    this.containerColor,
    this.fit = BoxFit.contain,
    this.enableSlideOutPage = false,
    this.borderRadius = BorderRadius.zero,
    this.heroTag,
    this.clearMemoryCacheWhenDispose = false,
    this.shadows,
    this.forceFadeIn = false,
    this.maxBytes,
    this.loadingProgressWidgetBuilder,
    this.failedWidgetBuilder,
    this.downloadingWidgetBuilder,
    this.pausedWidgetBuilder,
    this.loadingWidgetBuilder,
    this.completedWidgetBuilder,
  }) : super(key: key);

  @override
  State<EHImage> createState() => _EHImageState();
}

class _EHImageState extends State<EHImage> {
  Uint8List? _processedBytes;
  bool _isProcessing = false;

  @override
  Widget build(BuildContext context) {
    Widget child;

    if (advancedSetting.inNoImageMode.isTrue) {
      child = const SizedBox();
    } else if (_processedBytes != null) {
      child = _buildMemoryImage(context);
    } else if (widget.galleryImage.path == null) {
      child = buildNetworkImage(context);
    } else {
      child = buildFileImage(context);
    }

    if (widget.heroTag != null && styleSetting.isInMobileLayout) {
      child = Hero(tag: widget.heroTag!, child: child);
    }

    if (widget.autoLayout) {
      return LayoutBuilder(
        builder: (_, constraints) => Container(
          height: constraints.maxHeight,
          width: constraints.maxWidth,
          decoration: BoxDecoration(color: widget.containerColor, borderRadius: widget.borderRadius),
          child: child,
        ),
      );
    }

    return Container(
      height: widget.containerHeight,
      width: widget.containerWidth,
      decoration: BoxDecoration(color: widget.containerColor, borderRadius: widget.borderRadius),
      child: child,
    );
  }

  Widget _buildMemoryImage(BuildContext context) {
    return ExtendedImage.memory(
      _processedBytes!,
      fit: widget.fit,
      height: widget.containerHeight,
      width: widget.containerWidth,
      enableSlideOutPage: widget.enableSlideOutPage,
      clearMemoryCacheWhenDispose: widget.clearMemoryCacheWhenDispose,
      loadStateChanged: (ExtendedImageState state) {
        if (state.extendedImageLoadState == LoadState.completed) {
          state.returnLoadStateChangedWidget = true;
          Widget child = widget.completedWidgetBuilder?.call(state) ?? _buildExtendedRawImage(state);
          if (widget.borderRadius != BorderRadius.zero) {
            child = ClipRRect(child: child, borderRadius: widget.borderRadius);
          }
          if (state.slidePageState != null) {
            child = ExtendedImageSlidePageHandler(child: child, extendedImageSlidePageState: state.slidePageState);
          }
          return Center(
            child: Container(
              decoration: BoxDecoration(boxShadow: widget.shadows, borderRadius: widget.borderRadius),
              child: child,
            ),
          );
        }
        return null;
      },
    );
  }

  Widget buildNetworkImage(BuildContext context) {
    return ExtendedImage.network(
      _replaceEXUrl(widget.galleryImage.url),
      fit: widget.fit,
      height: widget.containerHeight,
      width: widget.containerWidth,
      handleLoadingProgress: widget.loadingProgressWidgetBuilder != null,
      printError: kDebugMode,
      enableSlideOutPage: widget.enableSlideOutPage,
      clearMemoryCacheWhenDispose: widget.clearMemoryCacheWhenDispose,
      loadStateChanged: (ExtendedImageState state) {
        switch (state.extendedImageLoadState) {
          case LoadState.loading:
            return widget.loadingProgressWidgetBuilder != null
                ? widget.loadingProgressWidgetBuilder!.call(_computeLoadingProgress(state.loadingProgress, state.extendedImageInfo))
                : Center(child: UIConfig.loadingAnimation(context));
          case LoadState.failed:
            return widget.failedWidgetBuilder?.call(state) ??
                Center(
                  child: GestureDetector(child: const Icon(Icons.sentiment_very_dissatisfied), onTap: state.reLoadImage),
                );
          case LoadState.completed:
            if ((readSetting.enableAnime4K.isTrue && readSetting.enableAnime4KForNetwork.isTrue) ||
                (io.Platform.isWindows && deOldifySetting.enableDeOldify.isTrue)) {
              _triggerNetworkImageProcessing(state);
            }

            state.returnLoadStateChangedWidget = true;

            Widget child = widget.completedWidgetBuilder?.call(state) ?? _buildExtendedRawImage(state);

            if (widget.borderRadius != BorderRadius.zero) {
              child = ClipRRect(child: child, borderRadius: widget.borderRadius);
            }

            if (state.slidePageState != null) {
              child = ExtendedImageSlidePageHandler(child: child, extendedImageSlidePageState: state.slidePageState);
            }

            child = Center(
              child: Container(
                decoration: BoxDecoration(boxShadow: widget.shadows, borderRadius: widget.borderRadius),
                child: child,
              ),
            );

            return widget.forceFadeIn || !state.wasSynchronouslyLoaded ? child.fadeIn() : child;
        }
      },
      maxBytes: widget.maxBytes,
    );
  }

  Future<void> _triggerNetworkImageProcessing(ExtendedImageState state) async {
    if (_processedBytes != null || _isProcessing) return;

    final io.File? file = await getCachedImageFile(widget.galleryImage.url);
    if (file == null) return;

    _isProcessing = true;
    Uint8List? bytes = await file.readAsBytes();

    // 先执行 Anime4K 超分辨率处理
    if (readSetting.enableAnime4K.isTrue && readSetting.enableAnime4KForNetwork.isTrue) {
      final upscaleResult = await Anime4KService.instance.processImage(
        imageBytes: bytes,
        cacheKey: widget.galleryImage.url,
        scaleFactor: readSetting.anime4KScaleFactor.value,
        pushStrength: readSetting.anime4KPushStrength.value,
        pushGradStrength: readSetting.anime4KPushGradStrength.value,
      );
      if (upscaleResult != null) {
        bytes = upscaleResult;
      }
    }

    // 再执行 DeOldify 上色处理
    if (io.Platform.isWindows && deOldifySetting.enableDeOldify.isTrue) {
      final colorizeResult = await DeOldifyService.instance.processImage(
        imageBytes: bytes,
        cacheKey: widget.galleryImage.url,
        modelType: deOldifySetting.modelType.value,
      );
      if (colorizeResult != null) {
        bytes = colorizeResult;
      }
    }

    if (bytes != null && mounted) {
      setState(() {
        _processedBytes = bytes;
        _isProcessing = false;
      });
    } else {
      _isProcessing = false;
    }
  }

  Widget buildFileImage(BuildContext context) {
    if (widget.galleryImage.downloadStatus == DownloadStatus.paused) {
      return widget.pausedWidgetBuilder?.call() ?? const Center(child: CircularProgressIndicator());
    }

    if (widget.galleryImage.downloadStatus == DownloadStatus.downloading) {
      return widget.downloadingWidgetBuilder?.call() ?? const Center(child: CircularProgressIndicator());
    }

    String filePath = GalleryDownloadService.computeImageDownloadAbsolutePathFromRelativePath(widget.galleryImage.path!);

    return _buildRawFileImage(context, filePath);
  }

  Widget _buildRawFileImage(BuildContext context, String filePath) {
    return ExtendedImage.file(
      io.File(filePath),
      fit: widget.fit,
      height: widget.containerHeight,
      width: widget.containerWidth,
      enableLoadState: widget.loadingWidgetBuilder != null || widget.failedWidgetBuilder != null || widget.completedWidgetBuilder != null,
      enableSlideOutPage: widget.enableSlideOutPage,
      borderRadius: widget.borderRadius,
      shape: widget.borderRadius != BorderRadius.zero ? BoxShape.rectangle : BoxShape.rectangle,
      clearMemoryCacheWhenDispose: widget.clearMemoryCacheWhenDispose,
      loadStateChanged: (ExtendedImageState state) {
        switch (state.extendedImageLoadState) {
          case LoadState.loading:
            return widget.loadingWidgetBuilder != null ? widget.loadingWidgetBuilder!.call() : Center(child: UIConfig.loadingAnimation(context));
          case LoadState.failed:
            return widget.failedWidgetBuilder?.call(state) ??
                Center(
                  child: GestureDetector(child: const Icon(Icons.sentiment_very_dissatisfied), onTap: state.reLoadImage),
                );
          case LoadState.completed:
            if (readSetting.enableAnime4K.isTrue || (io.Platform.isWindows && deOldifySetting.enableDeOldify.isTrue)) {
              _triggerFileImageProcessing(filePath);
            }

            state.returnLoadStateChangedWidget = true;

            Widget child = widget.completedWidgetBuilder?.call(state) ?? _buildExtendedRawImage(state);

            if (widget.borderRadius != BorderRadius.zero) {
              child = ClipRRect(child: child, borderRadius: widget.borderRadius);
            }

            if (state.slidePageState != null) {
              child = ExtendedImageSlidePageHandler(child: child, extendedImageSlidePageState: state.slidePageState);
            }

            return FadeIn(
              child: Center(
                child: Container(
                  decoration: BoxDecoration(boxShadow: widget.shadows, borderRadius: widget.borderRadius),
                  child: child,
                ),
              ),
            );
        }
      },
      maxBytes: widget.maxBytes,
      filterQuality: FilterQuality.medium,
    );
  }

  Future<void> _triggerFileImageProcessing(String filePath) async {
    if (_processedBytes != null || _isProcessing) return;

    _isProcessing = true;
    Uint8List? bytes;

    // 先执行 Anime4K 超分辨率处理
    if (readSetting.enableAnime4K.isTrue) {
      final upscaleResult = await Anime4KService.instance.processFile(
        filePath: filePath,
        scaleFactor: readSetting.anime4KScaleFactor.value,
        pushStrength: readSetting.anime4KPushStrength.value,
        pushGradStrength: readSetting.anime4KPushGradStrength.value,
      );
      if (upscaleResult != null) {
        bytes = upscaleResult;
      }
    }

    // 再执行 DeOldify 上色处理
    if (io.Platform.isWindows && deOldifySetting.enableDeOldify.isTrue) {
      if (bytes == null) {
        bytes = await io.File(filePath).readAsBytes();
      }
      final colorizeResult = await DeOldifyService.instance.processImage(
        imageBytes: bytes,
        cacheKey: filePath,
        modelType: deOldifySetting.modelType.value,
      );
      if (colorizeResult != null) {
        bytes = colorizeResult;
      }
    }

    if (bytes != null && mounted) {
      setState(() {
        _processedBytes = bytes;
        _isProcessing = false;
      });
    } else {
      _isProcessing = false;
    }
  }

  double _computeLoadingProgress(ImageChunkEvent? loadingProgress, ImageInfo? extendedImageInfo) {
    if (loadingProgress == null) {
      return 0.01;
    }

    int cur = loadingProgress.cumulativeBytesLoaded;
    int? total = extendedImageInfo?.sizeBytes;
    int? compressed = loadingProgress.expectedTotalBytes;
    return cur / (compressed ?? total ?? cur * 100);
  }

  /// replace image host: exhentai.org -> ehgt.org
  String _replaceEXUrl(String url) {
    Uri rawUri = Uri.parse(url);
    String host = rawUri.host;
    if (host != 's.exhentai.org') {
      return url;
    }

    Uri newUri = rawUri.replace(host: 'ehgt.org');
    return newUri.toString();
  }

  Widget _buildExtendedRawImage(ExtendedImageState state) {
    FittedSizes fittedSizes = applyBoxFit(
      widget.fit,
      Size(state.extendedImageInfo!.image.width.toDouble(), state.extendedImageInfo!.image.height.toDouble()),
      Size(widget.containerWidth ?? double.infinity, widget.containerHeight ?? double.infinity),
    );

    return ExtendedRawImage(
      image: state.extendedImageInfo?.image,
      height: fittedSizes.destination.height == 0 ? null : fittedSizes.destination.height,
      width: fittedSizes.destination.width == 0 ? null : fittedSizes.destination.width,
      scale: state.extendedImageInfo?.scale ?? 1.0,
      fit: widget.fit,
    );
  }
}
