#!/usr/bin/env python3
"""
DeOldify 上色脚本 - JHenTai 集成用

使用 onnxruntime 加载 DeOldify ONNX 模型，对黑白/灰度图片进行上色。
直接使用模型输出的 RGB 图像，与 DeOldify.net 行为一致。

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


def colorize_image(input_path: str, output_path: str, model_path: str, render_factor: int = 19) -> None:
    """
    对单张图片进行 DeOldify 上色。

    流程（与 DeOldify.net 一致）:
    1. 读取原图，转灰度
    2. 缩放到 256x256，归一化后送入 ONNX 模型
    3. 模型直接输出彩色 RGB 图像 (256x256)
    4. 将模型输出缩放回原始尺寸
    5. 保存
    """
    # 1. 读取原图
    original = Image.open(input_path).convert('RGB')
    orig_w, orig_h = original.size

    # 2. 准备模型输入: 灰度图 -> 256x256 -> 归一化到 [0, 1]
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

    # 3. 推理
    outputs = session.run(None, {input_name: input_data})
    output_data = outputs[0]

    # 处理输出格式: NCHW -> HWC
    if output_data.ndim == 4:
        if output_data.shape[1] in (1, 3):
            output_data = np.transpose(output_data[0], (1, 2, 0))
        else:
            output_data = output_data[0]

    output_data = np.squeeze(output_data)

    # 4. 将模型输出转换为 RGB uint8 图像
    if output_data.ndim == 3 and output_data.shape[-1] == 3:
        # 模型输出 3 通道 RGB，裁剪到 [0, 1] 后转 uint8
        model_rgb = np.clip(output_data, 0.0, 1.0)
        model_rgb_uint8 = (model_rgb * 255).astype(np.uint8)
    elif output_data.ndim == 2:
        # 单通道输出，转灰度 RGB
        model_rgb_uint8 = np.stack([output_data] * 3, axis=-1).astype(np.uint8)
    else:
        model_rgb = np.clip(output_data, 0.0, 1.0)
        model_rgb_uint8 = (model_rgb * 255).astype(np.uint8)

    # 5. 将 256x256 的上色结果缩放回原始尺寸
    colorized = Image.fromarray(model_rgb_uint8, mode='RGB')
    result = colorized.resize((orig_w, orig_h), Image.LANCZOS)
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
