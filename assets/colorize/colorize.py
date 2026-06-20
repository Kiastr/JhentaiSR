#!/usr/bin/env python3
"""
DeOldify 上色脚本 - JHenTai 集成用

使用 onnxruntime 加载 DeOldify ONNX 模型，对黑白/灰度图片进行上色。
实现与 deoldify-onnx 项目一致的处理流程。

依赖: onnxruntime, numpy, Pillow, opencv-python
用法: python colorize.py -i <input> -o <output> -m <model.onnx> [-r <render_factor>]
"""

import argparse
import sys
import os

import numpy as np
import cv2
from PIL import Image
import onnxruntime as ort


def colorize_image(input_path: str, output_path: str, model_path: str, render_factor: int = 8) -> None:
    """
    对单张图片进行 DeOldify 上色。

    流程（与 deoldify-onnx 官方实现一致）:
    1. 读取原图，提取原始 L 通道（保留亮度）
    2. 转灰度 RGB，缩放到推理尺寸，直接用 0-255 float 输入模型（不归一化）
    3. 模型输出彩色图像，转 uint8
    4. 缩放回原始尺寸，高斯模糊平滑色块
    5. 从模糊后的彩色图提取 AB 通道，与原始 L 合并
    """
    # 1. 读取原图 (PIL RGB -> cv2 BGR)
    original = Image.open(input_path).convert('RGB')
    orig_w, orig_h = original.size
    original_np = np.array(original)
    original_bgr = cv2.cvtColor(original_np, cv2.COLOR_RGB2BGR)

    # 提取 targetL：与官方 deoldify-onnx (color/deoldify.py) 一致，取 BGR 的 B 通道。
    # 注意：官方实现并未使用真正的 LAB 亮度，而是用 B 通道作为 targetL，
    # 与下方 LAB 合并的逻辑配合，才能得到官方那种偏暖、自然的上色风格。
    # 之前使用真正的 L 通道会导致最终结果整体偏蓝。
    target_l, _, _ = cv2.split(original_bgr)

    # 2. 准备模型输入: 灰度图 -> RGB(3通道相同) -> 缩放 -> 0-255 float
    gray = cv2.cvtColor(original_bgr, cv2.COLOR_BGR2GRAY)
    gray_rgb = cv2.cvtColor(gray, cv2.COLOR_GRAY2RGB)

    # 当前 ONNX 模型固定 256x256，忽略 render_factor
    input_image = cv2.resize(gray_rgb, (256, 256))
    input_data = input_image.astype(np.float32)
    input_data = input_data.transpose((2, 0, 1))  # HWC -> CHW
    input_data = np.expand_dims(input_data, axis=0).astype(np.float32)  # (1, 3, H, W)

    # 3. 推理
    session = ort.InferenceSession(model_path, providers=['CPUExecutionProvider'])
    input_name = session.get_inputs()[0].name
    colorized = session.run(None, {input_name: input_data})[0][0]

    # 4. 后处理：严格对齐官方 color/deoldify.py 的 colorize 方法
    colorized = colorized.transpose(1, 2, 0)  # CHW -> HWC
    # 与官方一致：把模型输出当作 BGR 转成 RGB，随后直接用 COLOR_BGR2LAB 转换。
    # 这里不要先做 RGB2BGR 转回，否则 AB 通道语义会与官方相反，导致偏蓝。
    colorized = cv2.cvtColor(colorized, cv2.COLOR_BGR2RGB).astype(np.uint8)
    colorized = cv2.resize(colorized, (orig_w, orig_h))
    colorized = cv2.GaussianBlur(colorized, (13, 13), 0)

    # 5. LAB 合并：官方用 targetL(B 通道) + 模型颜色的 AB
    colorized_lab = cv2.cvtColor(colorized, cv2.COLOR_BGR2LAB)
    _, a, b = cv2.split(colorized_lab)
    result_lab = cv2.merge((target_l, a, b))
    result_bgr = cv2.cvtColor(result_lab, cv2.COLOR_LAB2BGR)

    # 6. 保存
    result = Image.fromarray(cv2.cvtColor(result_bgr, cv2.COLOR_BGR2RGB))
    result.save(output_path)


def main():
    parser = argparse.ArgumentParser(description='DeOldify image colorization')
    parser.add_argument('-i', '--input', required=True, help='Input image path')
    parser.add_argument('-o', '--output', required=True, help='Output image path')
    parser.add_argument('-m', '--model', required=True, help='ONNX model path')
    parser.add_argument('-r', '--render-factor', type=int, default=8, help='Render factor (default: 8, size = factor * 32)')
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
