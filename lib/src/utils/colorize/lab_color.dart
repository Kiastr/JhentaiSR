import 'dart:typed_data';
import 'dart:math' as math;

/// LAB 色彩空间转换工具
///
/// 匹配 OpenCV cv2.COLOR_BGR2Lab / cv2.COLOR_Lab2BGR 行为
/// 输入 BGR/RGB 浮点值范围 [0, 1]
/// 输出 LAB 值范围: L [0, 100], a [-127, 127], b [-127, 127]

const double _epsilon = 216.0 / 24389.0;
const double _kappa = 24389.0 / 27.0;
const double _xn = 0.95047;
const double _yn = 1.0;
const double _zn = 1.08883;

double _f(double t) {
  if (t > _epsilon) {
    return math.pow(t, 1.0 / 3.0) as double;
  } else {
    return (_kappa * t + 16.0) / 116.0;
  }
}

double _fInv(double t) {
  final double t3 = t * t * t;
  if (t3 > _epsilon) {
    return t3;
  } else {
    return (116.0 * t - 16.0) / _kappa;
  }
}

/// 将一个像素的 BGR 值 [0,1] 转换为 (L, a, b)
/// L 范围 [0, 100], a, b 范围 [-127, 127]
void bgrToLabPixel(double b, double g, double r, List<double> out) {
  double linearB, linearG, linearR;
  if (b <= 0.04045) {
    linearB = b / 12.92;
  } else {
    linearB = math.pow((b + 0.055) / 1.055, 2.4) as double;
  }
  if (g <= 0.04045) {
    linearG = g / 12.92;
  } else {
    linearG = math.pow((g + 0.055) / 1.055, 2.4) as double;
  }
  if (r <= 0.04045) {
    linearR = r / 12.92;
  } else {
    linearR = math.pow((r + 0.055) / 1.055, 2.4) as double;
  }

  final double x = 0.412453 * linearR + 0.357580 * linearG + 0.180423 * linearB;
  final double y = 0.212671 * linearR + 0.715160 * linearG + 0.072169 * linearB;
  final double z = 0.019334 * linearR + 0.119193 * linearG + 0.950227 * linearB;

  final double xn = x / _xn;
  final double yn = y / _yn;
  final double zn = z / _zn;

  final double fx = _f(xn);
  final double fy = _f(yn);
  final double fz = _f(zn);

  out[0] = 116.0 * fy - 16.0;
  out[1] = 500.0 * (fx - fy);
  out[2] = 200.0 * (fy - fz);
}

/// 将一个像素的 LAB 值转换为 BGR [0, 1]
void labToBgrPixel(double l, double a, double b, List<double> out) {
  final double fy = (l + 16.0) / 116.0;
  final double fx = a / 500.0 + fy;
  final double fz = fy - b / 200.0;

  final double xn = _fInv(fx);
  final double yn = _fInv(fy);
  final double zn = _fInv(fz);

  final double x = xn * _xn;
  final double y = yn * _yn;
  final double z = zn * _zn;

  double linearR = 3.240479 * x - 1.537150 * y - 0.498535 * z;
  double linearG = -0.969256 * x + 1.875992 * y + 0.041556 * z;
  double linearB = 0.055648 * x - 0.204043 * y + 1.057311 * z;

  linearR = linearR.clamp(0.0, 1.0);
  linearG = linearG.clamp(0.0, 1.0);
  linearB = linearB.clamp(0.0, 1.0);

  double srgbR, srgbG, srgbB;
  if (linearR <= 0.0031308) {
    srgbR = 12.92 * linearR;
  } else {
    srgbR = 1.055 * math.pow(linearR, 1.0 / 2.4) as double - 0.055;
  }
  if (linearG <= 0.0031308) {
    srgbG = 12.92 * linearG;
  } else {
    srgbG = 1.055 * math.pow(linearG, 1.0 / 2.4) as double - 0.055;
  }
  if (linearB <= 0.0031308) {
    srgbB = 12.92 * linearB;
  } else {
    srgbB = 1.055 * math.pow(linearB, 1.0 / 2.4) as double - 0.055;
  }

  out[0] = srgbB.clamp(0.0, 1.0);
  out[1] = srgbG.clamp(0.0, 1.0);
  out[2] = srgbR.clamp(0.0, 1.0);
}

/// 从 RGB uint8 图像提取 L 通道 (Float32List, 范围 [0, 100])
/// 同时返回提取 ab 所需的完整 LAB 数据
void extractLabFromRgbUint8(
  Uint8List rgbaBytes,
  int width,
  int height,
  Float32List lOut,
  Float32List aOut,
  Float32List bOut,
) {
  final List<double> pixel = List<double>.filled(3, 0.0);
  for (int y = 0; y < height; y++) {
    for (int x = 0; x < width; x++) {
      final int idx = (y * width + x) * 4;
      final double r = rgbaBytes[idx] / 255.0;
      final double g = rgbaBytes[idx + 1] / 255.0;
      final double b = rgbaBytes[idx + 2] / 255.0;
      bgrToLabPixel(b, g, r, pixel);
      final int pi = y * width + x;
      lOut[pi] = pixel[0];
      aOut[pi] = pixel[1];
      bOut[pi] = pixel[2];
    }
  }
}

/// 从 LAB 平面数据合成 RGB uint8 图像
void composeLabToRgbUint8(
  Float32List lIn,
  Float32List aIn,
  Float32List bIn,
  int width,
  int height,
  Uint8List rgbaOut,
) {
  final List<double> pixel = List<double>.filled(3, 0.0);
  for (int y = 0; y < height; y++) {
    for (int x = 0; x < width; x++) {
      final int pi = y * width + x;
      labToBgrPixel(lIn[pi], aIn[pi], bIn[pi], pixel);
      final int idx = pi * 4;
      rgbaOut[idx] = (pixel[2] * 255.0).round().clamp(0, 255);
      rgbaOut[idx + 1] = (pixel[1] * 255.0).round().clamp(0, 255);
      rgbaOut[idx + 2] = (pixel[0] * 255.0).round().clamp(0, 255);
      rgbaOut[idx + 3] = 255;
    }
  }
}

/// 将 LAB 平面数据合成 BGR float32 [0, 1]
void composeLabPlanarToBgrFloat32(
  Float32List lIn,
  Float32List aIn,
  Float32List bIn,
  int width,
  int height,
  Float32List bgrOut,
) {
  final List<double> pixel = List<double>.filled(3, 0.0);
  for (int i = 0; i < width * height; i++) {
    labToBgrPixel(lIn[i], aIn[i], bIn[i], pixel);
    bgrOut[i * 3] = pixel[0];
    bgrOut[i * 3 + 1] = pixel[1];
    bgrOut[i * 3 + 2] = pixel[2];
  }
}
