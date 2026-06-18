#!/usr/bin/env python3
"""
DeOldify 上色脚本 - JHenTai 集成用

使用 onnxruntime 加载 DeOldify ONNX 模型，对黑白/灰度图片进行上色。
保留原始亮度（L 通道）以保证清晰度，仅添加颜色信息。

依赖: onnxruntime, numpy, Pillow
用法: python colorize.py -i <input> -o <output> -m <model.onnx> [-r <render_factor>]
"""

import argparse
import sys
import os

import numpy as np
from PIL import Image
import onnxruntime as ort


# DeOldify 模型内部固定推理分辨率
INFERENCE_SIZE = 256


def rgb_to_lab_l(rgb: np.ndarray) -> np.ndarray:
    """
    从 RGB 图像提取 LAB 色彩空间的 L 通道（亮度）。
    输入: (H, W, 3) uint8 RGB
    输出: (H, W) float32, 范围 [0, 100]
    """
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)

    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 0.9503041 * rgb_linear[..., 2]

    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))

    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0

    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)

    L = 116.0 * fy - 16.0
    return L


def rgb_to_lab_a(rgb: np.ndarray) -> np.ndarray:
    """从 RGB 提取 LAB 的 a 通道"""
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    xn, yn = 0.95047, 1.0
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    return 500.0 * (fx - fy)


def rgb_to_lab_b(rgb: np.ndarray) -> np.ndarray:
    """从 RGB 提取 LAB 的 b 通道"""
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 0.9503041 * rgb_linear[..., 2]
    yn, zn = 1.0, 1.08883
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    return 200.0 * (fy - fz)


def lab_to_rgb(L: np.ndarray, a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """
    LAB -> RGB 转换。
    输入: L [0,100], a, b 任意范围, 形状 (H, W)
    输出: (H, W, 3) uint8 RGB
    """
    fy = (L + 16.0) / 116.0
    fx = a / 500.0 + fy
    fz = fy - b / 200.0

    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0

    fx3 = fx ** 3
    fz3 = fz ** 3

    xr = np.where(fx3 > eps, fx3, (116.0 * fx - 16.0) / k)
    zr = np.where(fz3 > eps, fz3, (116.0 * fz - 16.0) / k)
    yr = np.where(L > k * eps, ((L + 16.0) / 116.0) ** 3, L / k)

    xn, yn, zn = 0.95047, 1.0, 1.08883
    X = xr * xn
    Y = yr * yn
    Z = zr * zn

    r = 3.2404542 * X - 1.5371385 * Y - 0.4985314 * Z
    g = -0.9692660 * X + 1.8760108 * Y + 0.0415560 * Z
    b_b = 0.0556434 * X - 0.2040259 * Y + 1.0572252 * Z

    rgb = np.stack([r, g, b_b], axis=-1)
    rgb = np.clip(rgb, 0, 1)

    mask = rgb <= 0.0031308
    rgb_srgb = np.where(mask, 12.92 * rgb, 1.055 * np.power(np.maximum(rgb, 1e-12), 1.0 / 2.4) - 0.055)
    rgb_srgb = np.clip(rgb_srgb * 255.0, 0, 255).astype(np.uint8)
    return rgb_srgb


def colorize_image(input_path: str, output_path: str, model_path: str, render_factor: int = 19) -> None:
    """
    对单张图片进行 DeOldify 上色。

    流程:
    1. 读取原图 (RGB)，保存原始尺寸
    2. 提取原始 L 通道（在原始尺寸上）
    3. 将灰度图缩放到 256x256，归一化后送入 ONNX 模型
    4. 模型输出 3 通道上色结果 (1, 3, 256, 256)
    5. 将模型输出归一化到 [0, 255]，得到 256x256 的上色图像
    6. 从 256x256 上色结果中提取 AB 通道
    7. 将 AB 通道缩放回原始尺寸
    8. 用原始 L + 推理得到的 AB 重建彩色图像
    """
    # 1. 读取原图
    original = Image.open(input_path).convert('RGB')
    orig_w, orig_h = original.size
    original_np = np.array(original)

    # 2. 提取原始 L 通道（保留原图的亮度结构）
    orig_L = rgb_to_lab_l(original_np)

    # 3. 准备模型输入: 灰度图 -> 256x256 -> 归一化到 [0, 1]
    gray = original.convert('L')
    gray_resized = gray.resize((INFERENCE_SIZE, INFERENCE_SIZE), Image.BILINEAR)
    input_data = np.array(gray_resized, dtype=np.float32) / 255.0

    # 加载模型
    session = ort.InferenceSession(model_path, providers=['CPUExecutionProvider'])
    input_name = session.get_inputs()[0].name

    # 检查模型输入维度要求，构造 3 通道灰度输入 (1, 3, 256, 256)
    input_shape = session.get_inputs()[0].shape
    if len(input_shape) == 4 and input_shape[1] == 3:
        input_data = np.stack([input_data] * 3, axis=0)[np.newaxis, :, :, :]
    else:
        input_data = input_data[np.newaxis, np.newaxis, :, :]

    # 4. 推理
    outputs = session.run(None, {input_name: input_data})
    output_data = outputs[0]

    # 处理输出格式: NCHW -> HWC
    if output_data.ndim == 4:
        if output_data.shape[1] in (1, 3):
            output_data = np.transpose(output_data[0], (1, 2, 0))
        else:
            output_data = output_data[0]

    output_data = np.squeeze(output_data)

    # 5. 将模型输出归一化到有效 RGB 范围
    if output_data.ndim == 3 and output_data.shape[-1] == 3:
        # 模型输出 3 通道 - 将其归一化到 [0, 255] uint8
        # DeOldify ONNX 模型输出可能是超过 [0, 1] 范围的 float 值
        # 先裁剪到 [0, 1]，再乘以 255
        model_rgb_float = np.clip(output_data, 0.0, 1.0)
        model_rgb_uint8 = (model_rgb_float * 255).astype(np.uint8)

        # 6. 从 256x256 的上色结果中提取 AB 通道
        out_a = rgb_to_lab_a(model_rgb_uint8)
        out_b = rgb_to_lab_b(model_rgb_uint8)
    elif output_data.ndim == 3 and output_data.shape[-1] == 2:
        # 模型直接输出 AB 通道
        out_a = output_data[..., 0]
        out_b = output_data[..., 1]
    else:
        # 回退: 直接将输出作为上色结果，缩放到原始尺寸
        if output_data.max() <= 1.0:
            colorized_u8 = (np.clip(output_data, 0, 1) * 255).astype(np.uint8)
        else:
            colorized_u8 = np.clip(output_data, 0, 255).astype(np.uint8)
        result = Image.fromarray(colorized_u8).resize((orig_w, orig_h), Image.BILINEAR)
        result.save(output_path)
        return

    # 7. 将 AB 通道缩放回原始尺寸
    out_a_pil = Image.fromarray(out_a.astype(np.float32), mode='F')
    out_b_pil = Image.fromarray(out_b.astype(np.float32), mode='F')
    out_a_resized = out_a_pil.resize((orig_w, orig_h), Image.BILINEAR)
    out_b_resized = out_b_pil.resize((orig_w, orig_h), Image.BILINEAR)

    out_a_arr = np.array(out_a_resized)
    out_b_arr = np.array(out_b_resized)

    # 8. 用原始 L + 推理得到的 AB 重建彩色图像
    result_rgb = lab_to_rgb(orig_L, out_a_arr, out_b_arr)
    result = Image.fromarray(result_rgb)
    result.save(output_path)


def main():
    parser = argparse.ArgumentParser(description='DeOldify image colorization')
    parser.add_argument('-i', '--input', required=True, help='Input image path')
    parser.add_argument('-o', '--output', required=True, help='Output image path')
    parser.add_argument('-m', '--model', required=True, help='ONNX model path')
    parser.add_argument('-r', '--render-factor', type=int, default=19, help='Render factor (default: 19)')
    args = parser.parse_args()

    if not os.path.exists(args.input):
        print(f'Error: input file not found: {args.input}', file=sys.stderr)
        sys.exit(1)
    if not os.path.exists(args.model):
        print(f'Error: model file not found: {args.model}', file=sys.stderr)
        sys.exit(1)

    try:
        colorize_image(args.input, args.output, args.model, args.render_factor)
        print(f'Colorized image saved to {args.output}', file=sys.stderr)
    except Exception as e:
        print(f'Error: {e}', file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
