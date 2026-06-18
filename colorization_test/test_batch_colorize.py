#!/usr/bin/env python#!/usr/bin/env python3
"""
批量上色测试：模拟 App#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 color#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/work#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI =#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iter#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in (#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f /#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) /#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y =#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 *#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 *#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 *#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.01933#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.11919#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.05722#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn =#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.088#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn,#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 2438#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y /#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0
    fz#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0
    fz = np.where(z / zn > eps, fz, (k * (z / zn)#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    L =#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    L = 116.0 * fy - 16.0
    return L


def rgb#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    L = 116.0 * fy - 16.0
    return L


def rgb_to_lab_a(rgb):
    rgb_f = rgb.astype(np.float32)#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    L = 116.0 * fy - 16.0
    return L


def rgb_to_lab_a(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.040#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    L = 116.0 * fy - 16.0
    return L


def rgb_to_lab_a(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    L = 116.0 * fy - 16.0
    return L


def rgb_to_lab_a(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.05#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    L = 116.0 * fy - 16.0
    return L


def rgb_to_lab_a(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.41245#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    L = 116.0 * fy - 16.0
    return L


def rgb_to_lab_a(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.35757#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    L = 116.0 * fy - 16.0
    return L


def rgb_to_lab_a(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.18043#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    L = 116.0 * fy - 16.0
    return L


def rgb_to_lab_a(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.21#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    L = 116.0 * fy - 16.0
    return L


def rgb_to_lab_a(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.71#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    L = 116.0 * fy - 16.0
    return L


def rgb_to_lab_a(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.07#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    L = 116.0 * fy - 16.0
    return L


def rgb_to_lab_a(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    L = 116.0 * fy - 16.0
    return L


def rgb_to_lab_a(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    L = 116.0 * fy - 16.0
    return L


def rgb_to_lab_a(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    L = 116.0 * fy - 16.0
    return L


def rgb_to_lab_a(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    L = 116.0 * fy - 16.0
    return L


def rgb_to_lab_a(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.9#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    L = 116.0 * fy - 16.0
    return L


def rgb_to_lab_a(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0,#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    L = 116.0 * fy - 16.0
    return L


def rgb_to_lab_a(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    L = 116.0 * fy - 16.0
    return L


def rgb_to_lab_a(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    L = 116.0 * fy - 16.0
    return L


def rgb_to_lab_a(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    L = 116.0 * fy - 16.0
    return L


def rgb_to_lab_a(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    L = 116.0 * fy - 16.0
    return L


def rgb_to_lab_a(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    L = 116.0 * fy - 16.0
    return L


def rgb_to_lab_a(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    L = 116.0 * fy - 16.0
    return L


def rgb_to_lab_a(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps,#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    L = 116.0 * fy - 16.0
    return L


def rgb_to_lab_a(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) /#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    L = 116.0 * fy - 16.0
    return L


def rgb_to_lab_a(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy =#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    L = 116.0 * fy - 16.0
    return L


def rgb_to_lab_a(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) +#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    L = 116.0 * fy - 16.0
    return L


def rgb_to_lab_a(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    return 500#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    L = 116.0 * fy - 16.0
    return L


def rgb_to_lab_a(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    return 500.0 * (fx - fy)


def#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    L = 116.0 * fy - 16.0
    return L


def rgb_to_lab_a(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    return 500.0 * (fx - fy)


def rgb_to_lab_b(rgb):
    rgb_f = rgb.astype(np.float32#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    L = 116.0 * fy - 16.0
    return L


def rgb_to_lab_a(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    return 500.0 * (fx - fy)


def rgb_to_lab_b(rgb):
    rgb_f = rgb.astype(np.float32)
    return 116.0
    mask = rgb_f <= 0.#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    L = 116.0 * fy - 16.0
    return L


def rgb_to_lab_a(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    return 500.0 * (fx - fy)


def rgb_to_lab_b(rgb):
    rgb_f = rgb.astype(np.float32)
    return 116.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f /#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    L = 116.0 * fy - 16.0
    return L


def rgb_to_lab_a(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    return 500.0 * (fx - fy)


def rgb_to_lab_b(rgb):
    rgb_f = rgb.astype(np.float32)
    return 116.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    L = 116.0 * fy - 16.0
    return L


def rgb_to_lab_a(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    return 500.0 * (fx - fy)


def rgb_to_lab_b(rgb):
    rgb_f = rgb.astype(np.float32)
    return 116.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.41#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    L = 116.0 * fy - 16.0
    return L


def rgb_to_lab_a(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    return 500.0 * (fx - fy)


def rgb_to_lab_b(rgb):
    rgb_f = rgb.astype(np.float32)
    return 116.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.35#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    L = 116.0 * fy - 16.0
    return L


def rgb_to_lab_a(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    return 500.0 * (fx - fy)


def rgb_to_lab_b(rgb):
    rgb_f = rgb.astype(np.float32)
    return 116.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.18#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    L = 116.0 * fy - 16.0
    return L


def rgb_to_lab_a(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    return 500.0 * (fx - fy)


def rgb_to_lab_b(rgb):
    rgb_f = rgb.astype(np.float32)
    return 116.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    L = 116.0 * fy - 16.0
    return L


def rgb_to_lab_a(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    return 500.0 * (fx - fy)


def rgb_to_lab_b(rgb):
    rgb_f = rgb.astype(np.float32)
    return 116.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    L = 116.0 * fy - 16.0
    return L


def rgb_to_lab_a(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    return 500.0 * (fx - fy)


def rgb_to_lab_b(rgb):
    rgb_f = rgb.astype(np.float32)
    return 116.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    L = 116.0 * fy - 16.0
    return L


def rgb_to_lab_a(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    return 500.0 * (fx - fy)


def rgb_to_lab_b(rgb):
    rgb_f = rgb.astype(np.float32)
    return 116.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    L = 116.0 * fy - 16.0
    return L


def rgb_to_lab_a(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    return 500.0 * (fx - fy)


def rgb_to_lab_b(rgb):
    rgb_f = rgb.astype(np.float32)
    return 116.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.019333#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    L = 116.0 * fy - 16.0
    return L


def rgb_to_lab_a(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    return 500.0 * (fx - fy)


def rgb_to_lab_b(rgb):
    rgb_f = rgb.astype(np.float32)
    return 116.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0]#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    L = 116.0 * fy - 16.0
    return L


def rgb_to_lab_a(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    return 500.0 * (fx - fy)


def rgb_to_lab_b(rgb):
    rgb_f = rgb.astype(np.float32)
    return 116.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1]#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    L = 116.0 * fy - 16.0
    return L


def rgb_to_lab_a(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    return 500.0 * (fx - fy)


def rgb_to_lab_b(rgb):
    rgb_f = rgb.astype(np.float32)
    return 116.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    L = 116.0 * fy - 16.0
    return L


def rgb_to_lab_a(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    return 500.0 * (fx - fy)


def rgb_to_lab_b(rgb):
    rgb_f = rgb.astype(np.float32)
    return 116.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    L = 116.0 * fy - 16.0
    return L


def rgb_to_lab_a(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    return 500.0 * (fx - fy)


def rgb_to_lab_b(rgb):
    rgb_f = rgb.astype(np.float32)
    return 116.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fy = np.cbrt(np#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    L = 116.0 * fy - 16.0
    return L


def rgb_to_lab_a(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    return 500.0 * (fx - fy)


def rgb_to_lab_b(rgb):
    rgb_f = rgb.astype(np.float32)
    return 116.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    L = 116.0 * fy - 16.0
    return L


def rgb_to_lab_a(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    return 500.0 * (fx - fy)


def rgb_to_lab_b(rgb):
    rgb_f = rgb.astype(np.float32)
    return 116.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    L = 116.0 * fy - 16.0
    return L


def rgb_to_lab_a(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    return 500.0 * (fx - fy)


def rgb_to_lab_b(rgb):
    rgb_f = rgb.astype(np.float32)
    return 116.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 2438#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    L = 116.0 * fy - 16.0
    return L


def rgb_to_lab_a(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    return 500.0 * (fx - fy)


def rgb_to_lab_b(rgb):
    rgb_f = rgb.astype(np.float32)
    return 116.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fy = np.where(y / yn > eps#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    L = 116.0 * fy - 16.0
    return L


def rgb_to_lab_a(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    return 500.0 * (fx - fy)


def rgb_to_lab_b(rgb):
    rgb_f = rgb.astype(np.float32)
    return 116.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) /#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    L = 116.0 * fy - 16.0
    return L


def rgb_to_lab_a(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    return 500.0 * (fx - fy)


def rgb_to_lab_b(rgb):
    rgb_f = rgb.astype(np.float32)
    return 116.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    fz#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    L = 116.0 * fy - 16.0
    return L


def rgb_to_lab_a(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    return 500.0 * (fx - fy)


def rgb_to_lab_b(rgb):
    rgb_f = rgb.astype(np.float32)
    return 116.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    fz = np.where(z / zn > eps, fz, (k * (z / zn)#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    L = 116.0 * fy - 16.0
    return L


def rgb_to_lab_a(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    return 500.0 * (fx - fy)


def rgb_to_lab_b(rgb):
    rgb_f = rgb.astype(np.float32)
    return 116.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 1#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    L = 116.0 * fy - 16.0
    return L


def rgb_to_lab_a(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    return 500.0 * (fx - fy)


def rgb_to_lab_b(rgb):
    rgb_f = rgb.astype(np.float32)
    return 116.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    return 200.0 * (fy - fz#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    L = 116.0 * fy - 16.0
    return L


def rgb_to_lab_a(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    return 500.0 * (fx - fy)


def rgb_to_lab_b(rgb):
    rgb_f = rgb.astype(np.float32)
    return 116.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    return 200.0 * (fy - fz)


def lab_to_rgb(L, a, b):
    fy = (L +#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    L = 116.0 * fy - 16.0
    return L


def rgb_to_lab_a(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    return 500.0 * (fx - fy)


def rgb_to_lab_b(rgb):
    rgb_f = rgb.astype(np.float32)
    return 116.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    return 200.0 * (fy - fz)


def lab_to_rgb(L, a, b):
    fy = (L + 16.0) / 11#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    L = 116.0 * fy - 16.0
    return L


def rgb_to_lab_a(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    return 500.0 * (fx - fy)


def rgb_to_lab_b(rgb):
    rgb_f = rgb.astype(np.float32)
    return 116.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    return 200.0 * (fy - fz)


def lab_to_rgb(L, a, b):
    fy = (L + 16.0) / 116.0
    fx = a / 500.0 + fy
    fz = fy - b / 200.0
    eps = 216.0 / 24389.#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    L = 116.0 * fy - 16.0
    return L


def rgb_to_lab_a(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    return 500.0 * (fx - fy)


def rgb_to_lab_b(rgb):
    rgb_f = rgb.astype(np.float32)
    return 116.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    return 200.0 * (fy - fz)


def lab_to_rgb(L, a, b):
    fy = (L + 16.0) / 116.0
    fx = a / 500.0 + fy
    fz = fy - b / 200.0
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    L = 116.0 * fy - 16.0
    return L


def rgb_to_lab_a(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    return 500.0 * (fx - fy)


def rgb_to_lab_b(rgb):
    rgb_f = rgb.astype(np.float32)
    return 116.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    return 200.0 * (fy - fz)


def lab_to_rgb(L, a, b):
    fy = (L + 16.0) / 116.0
    fx = a / 500.0 + fy
    fz = fy - b / 200.0
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx3 = fx ** 3
#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    L = 116.0 * fy - 16.0
    return L


def rgb_to_lab_a(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    return 500.0 * (fx - fy)


def rgb_to_lab_b(rgb):
    rgb_f = rgb.astype(np.float32)
    return 116.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    return 200.0 * (fy - fz)


def lab_to_rgb(L, a, b):
    fy = (L + 16.0) / 116.0
    fx = a / 500.0 + fy
    fz = fy - b / 200.0
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx3 = fx ** 3
    fz3 = fz ** 3
    xr = np.where(fx3 > eps#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    L = 116.0 * fy - 16.0
    return L


def rgb_to_lab_a(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    return 500.0 * (fx - fy)


def rgb_to_lab_b(rgb):
    rgb_f = rgb.astype(np.float32)
    return 116.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    return 200.0 * (fy - fz)


def lab_to_rgb(L, a, b):
    fy = (L + 16.0) / 116.0
    fx = a / 500.0 + fy
    fz = fy - b / 200.0
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx3 = fx ** 3
    fz3 = fz ** 3
    xr = np.where(fx3 > eps, fx3, (116.0#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    L = 116.0 * fy - 16.0
    return L


def rgb_to_lab_a(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    return 500.0 * (fx - fy)


def rgb_to_lab_b(rgb):
    rgb_f = rgb.astype(np.float32)
    return 116.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    return 200.0 * (fy - fz)


def lab_to_rgb(L, a, b):
    fy = (L + 16.0) / 116.0
    fx = a / 500.0 + fy
    fz = fy - b / 200.0
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx3 = fx ** 3
    fz3 = fz ** 3
    xr = np.where(fx3 > eps, fx3, (116.0 * fx - 16.0) / k)
    zr = np.where(f#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    L = 116.0 * fy - 16.0
    return L


def rgb_to_lab_a(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    return 500.0 * (fx - fy)


def rgb_to_lab_b(rgb):
    rgb_f = rgb.astype(np.float32)
    return 116.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    return 200.0 * (fy - fz)


def lab_to_rgb(L, a, b):
    fy = (L + 16.0) / 116.0
    fx = a / 500.0 + fy
    fz = fy - b / 200.0
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx3 = fx ** 3
    fz3 = fz ** 3
    xr = np.where(fx3 > eps, fx3, (116.0 * fx - 16.0) / k)
    zr = np.where(fz3 > eps, fz3, (116.0 * fz -#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    L = 116.0 * fy - 16.0
    return L


def rgb_to_lab_a(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    return 500.0 * (fx - fy)


def rgb_to_lab_b(rgb):
    rgb_f = rgb.astype(np.float32)
    return 116.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    return 200.0 * (fy - fz)


def lab_to_rgb(L, a, b):
    fy = (L + 16.0) / 116.0
    fx = a / 500.0 + fy
    fz = fy - b / 200.0
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx3 = fx ** 3
    fz3 = fz ** 3
    xr = np.where(fx3 > eps, fx3, (116.0 * fx - 16.0) / k)
    zr = np.where(fz3 > eps, fz3, (116.0 * fz - 16.0) / k)
#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    L = 116.0 * fy - 16.0
    return L


def rgb_to_lab_a(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    return 500.0 * (fx - fy)


def rgb_to_lab_b(rgb):
    rgb_f = rgb.astype(np.float32)
    return 116.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    return 200.0 * (fy - fz)


def lab_to_rgb(L, a, b):
    fy = (L + 16.0) / 116.0
    fx = a / 500.0 + fy
    fz = fy - b / 200.0
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx3 = fx ** 3
    fz3 = fz ** 3
    xr = np.where(fx3 > eps, fx3, (116.0 * fx - 16.0) / k)
    zr = np.where(fz3 > eps, fz3, (116.0 * fz - 16.0) / k)
    yr = np.where(L > k * eps, ((L + 16.0) /#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    L = 116.0 * fy - 16.0
    return L


def rgb_to_lab_a(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    return 500.0 * (fx - fy)


def rgb_to_lab_b(rgb):
    rgb_f = rgb.astype(np.float32)
    return 116.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    return 200.0 * (fy - fz)


def lab_to_rgb(L, a, b):
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
    xn,#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    L = 116.0 * fy - 16.0
    return L


def rgb_to_lab_a(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    return 500.0 * (fx - fy)


def rgb_to_lab_b(rgb):
    rgb_f = rgb.astype(np.float32)
    return 116.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    return 200.0 * (fy - fz)


def lab_to_rgb(L, a, b):
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
    xn, yn, zn = 0.950#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    L = 116.0 * fy - 16.0
    return L


def rgb_to_lab_a(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    return 500.0 * (fx - fy)


def rgb_to_lab_b(rgb):
    rgb_f = rgb.astype(np.float32)
    return 116.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    return 200.0 * (fy - fz)


def lab_to_rgb(L, a, b):
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
    X =#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    L = 116.0 * fy - 16.0
    return L


def rgb_to_lab_a(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    return 500.0 * (fx - fy)


def rgb_to_lab_b(rgb):
    rgb_f = rgb.astype(np.float32)
    return 116.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    return 200.0 * (fy - fz)


def lab_to_rgb(L, a, b):
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
#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    L = 116.0 * fy - 16.0
    return L


def rgb_to_lab_a(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    return 500.0 * (fx - fy)


def rgb_to_lab_b(rgb):
    rgb_f = rgb.astype(np.float32)
    return 116.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    return 200.0 * (fy - fz)


def lab_to_rgb(L, a, b):
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
    r = 3.2404542 * X - 1.5#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    L = 116.0 * fy - 16.0
    return L


def rgb_to_lab_a(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    return 500.0 * (fx - fy)


def rgb_to_lab_b(rgb):
    rgb_f = rgb.astype(np.float32)
    return 116.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    return 200.0 * (fy - fz)


def lab_to_rgb(L, a, b):
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
    r = 3.2404542 * X - 1.5371385 * Y -#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    L = 116.0 * fy - 16.0
    return L


def rgb_to_lab_a(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    return 500.0 * (fx - fy)


def rgb_to_lab_b(rgb):
    rgb_f = rgb.astype(np.float32)
    return 116.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    return 200.0 * (fy - fz)


def lab_to_rgb(L, a, b):
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
    g = -0.96#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    L = 116.0 * fy - 16.0
    return L


def rgb_to_lab_a(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    return 500.0 * (fx - fy)


def rgb_to_lab_b(rgb):
    rgb_f = rgb.astype(np.float32)
    return 116.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    return 200.0 * (fy - fz)


def lab_to_rgb(L, a, b):
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
    g = -0.9692660 * X + 1#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    L = 116.0 * fy - 16.0
    return L


def rgb_to_lab_a(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    return 500.0 * (fx - fy)


def rgb_to_lab_b(rgb):
    rgb_f = rgb.astype(np.float32)
    return 116.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    return 200.0 * (fy - fz)


def lab_to_rgb(L, a, b):
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
    g = -0.9692660 * X + 1.8760108 * Y + 0.041556#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    L = 116.0 * fy - 16.0
    return L


def rgb_to_lab_a(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    return 500.0 * (fx - fy)


def rgb_to_lab_b(rgb):
    rgb_f = rgb.astype(np.float32)
    return 116.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    return 200.0 * (fy - fz)


def lab_to_rgb(L, a, b):
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
    b = 0.0556434 * X -#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    L = 116.0 * fy - 16.0
    return L


def rgb_to_lab_a(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    return 500.0 * (fx - fy)


def rgb_to_lab_b(rgb):
    rgb_f = rgb.astype(np.float32)
    return 116.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    return 200.0 * (fy - fz)


def lab_to_rgb(L, a, b):
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
    b = 0.0556434 * X - 0.2040259 * Y + 1.0572#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    L = 116.0 * fy - 16.0
    return L


def rgb_to_lab_a(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    return 500.0 * (fx - fy)


def rgb_to_lab_b(rgb):
    rgb_f = rgb.astype(np.float32)
    return 116.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    return 200.0 * (fy - fz)


def lab_to_rgb(L, a, b):
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
    b = 0.0556434 * X - 0.2040259 * Y + 1.0572252 * Z
    rgb = np.stack([r, g, b], axis=-#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    L = 116.0 * fy - 16.0
    return L


def rgb_to_lab_a(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    return 500.0 * (fx - fy)


def rgb_to_lab_b(rgb):
    rgb_f = rgb.astype(np.float32)
    return 116.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    return 200.0 * (fy - fz)


def lab_to_rgb(L, a, b):
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
    b = 0.0556434 * X - 0.2040259 * Y + 1.0572252 * Z
    rgb = np.stack([r, g, b], axis=-1)
    rgb = np.clip(r#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    L = 116.0 * fy - 16.0
    return L


def rgb_to_lab_a(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    return 500.0 * (fx - fy)


def rgb_to_lab_b(rgb):
    rgb_f = rgb.astype(np.float32)
    return 116.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    return 200.0 * (fy - fz)


def lab_to_rgb(L, a, b):
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
    b = 0.0556434 * X - 0.2040259 * Y + 1.0572252 * Z
    rgb = np.stack([r, g, b], axis=-1)
    rgb = np.clip(rgb, 0, 1)
    mask = rgb <= 0.0031308
    rgb_srgb =#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    L = 116.0 * fy - 16.0
    return L


def rgb_to_lab_a(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    return 500.0 * (fx - fy)


def rgb_to_lab_b(rgb):
    rgb_f = rgb.astype(np.float32)
    return 116.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    return 200.0 * (fy - fz)


def lab_to_rgb(L, a, b):
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
    b = 0.0556434 * X - 0.2040259 * Y + 1.0572252 * Z
    rgb = np.stack([r, g, b], axis=-1)
    rgb = np.clip(rgb, 0, 1)
    mask = rgb <= 0.0031308
    rgb_srgb = np.where(mask, 12.92 * rgb, 1.055#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    L = 116.0 * fy - 16.0
    return L


def rgb_to_lab_a(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    return 500.0 * (fx - fy)


def rgb_to_lab_b(rgb):
    rgb_f = rgb.astype(np.float32)
    return 116.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    return 200.0 * (fy - fz)


def lab_to_rgb(L, a, b):
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
    b = 0.0556434 * X - 0.2040259 * Y + 1.0572252 * Z
    rgb = np.stack([r, g, b], axis=-1)
    rgb = np.clip(rgb, 0, 1)
    mask = rgb <= 0.0031308
    rgb_srgb = np.where(mask, 12.92 * rgb, 1.055 * np.power(np.maximum(rgb,#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    L = 116.0 * fy - 16.0
    return L


def rgb_to_lab_a(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    return 500.0 * (fx - fy)


def rgb_to_lab_b(rgb):
    rgb_f = rgb.astype(np.float32)
    return 116.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    return 200.0 * (fy - fz)


def lab_to_rgb(L, a, b):
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
    b = 0.0556434 * X - 0.2040259 * Y + 1.0572252 * Z
    rgb = np.stack([r, g, b], axis=-1)
    rgb = np.clip(rgb, 0, 1)
    mask = rgb <= 0.0031308
    rgb_srgb = np.where(mask, 12.92 * rgb, 1.055 * np.power(np.maximum(rgb, 1e-12), 1.0 / 2.4) - 0.055)
    rgb_srgb = np.clip(rgb_srgb * 255.0, 0, 255).astype(np.uint8)
    return rgb_srgb


def colorize_image_reuse(session, input_name, input_shape, input_path, output_path):
    original = Image.open(input_path).convert('RGB')#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    L = 116.0 * fy - 16.0
    return L


def rgb_to_lab_a(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    return 500.0 * (fx - fy)


def rgb_to_lab_b(rgb):
    rgb_f = rgb.astype(np.float32)
    return 116.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    return 200.0 * (fy - fz)


def lab_to_rgb(L, a, b):
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
    b = 0.0556434 * X - 0.2040259 * Y + 1.0572252 * Z
    rgb = np.stack([r, g, b], axis=-1)
    rgb = np.clip(rgb, 0, 1)
    mask = rgb <= 0.0031308
    rgb_srgb = np.where(mask, 12.92 * rgb, 1.055 * np.power(np.maximum(rgb, 1e-12), 1.0 / 2.4) - 0.055)
    rgb_srgb = np.clip(rgb_srgb * 255.0, 0, 255).astype(np.uint8)
    return rgb_srgb


def colorize_image_reuse(session, input_name, input_shape, input_path, output_path):
    original = Image.open(input_path).convert('RGB')
    orig_w, orig_h = original.size#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    L = 116.0 * fy - 16.0
    return L


def rgb_to_lab_a(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    return 500.0 * (fx - fy)


def rgb_to_lab_b(rgb):
    rgb_f = rgb.astype(np.float32)
    return 116.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    return 200.0 * (fy - fz)


def lab_to_rgb(L, a, b):
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
    b = 0.0556434 * X - 0.2040259 * Y + 1.0572252 * Z
    rgb = np.stack([r, g, b], axis=-1)
    rgb = np.clip(rgb, 0, 1)
    mask = rgb <= 0.0031308
    rgb_srgb = np.where(mask, 12.92 * rgb, 1.055 * np.power(np.maximum(rgb, 1e-12), 1.0 / 2.4) - 0.055)
    rgb_srgb = np.clip(rgb_srgb * 255.0, 0, 255).astype(np.uint8)
    return rgb_srgb


def colorize_image_reuse(session, input_name, input_shape, input_path, output_path):
    original = Image.open(input_path).convert('RGB')
    orig_w, orig_h = original.size
    original_np = np.array(original)
    orig_L = rgb_to_lab#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    L = 116.0 * fy - 16.0
    return L


def rgb_to_lab_a(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    return 500.0 * (fx - fy)


def rgb_to_lab_b(rgb):
    rgb_f = rgb.astype(np.float32)
    return 116.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    return 200.0 * (fy - fz)


def lab_to_rgb(L, a, b):
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
    b = 0.0556434 * X - 0.2040259 * Y + 1.0572252 * Z
    rgb = np.stack([r, g, b], axis=-1)
    rgb = np.clip(rgb, 0, 1)
    mask = rgb <= 0.0031308
    rgb_srgb = np.where(mask, 12.92 * rgb, 1.055 * np.power(np.maximum(rgb, 1e-12), 1.0 / 2.4) - 0.055)
    rgb_srgb = np.clip(rgb_srgb * 255.0, 0, 255).astype(np.uint8)
    return rgb_srgb


def colorize_image_reuse(session, input_name, input_shape, input_path, output_path):
    original = Image.open(input_path).convert('RGB')
    orig_w, orig_h = original.size
    original_np = np.array(original)
    orig_L = rgb_to_lab_l(original_np)
    gray = original.convert('L')
    gray_resized#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    L = 116.0 * fy - 16.0
    return L


def rgb_to_lab_a(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    return 500.0 * (fx - fy)


def rgb_to_lab_b(rgb):
    rgb_f = rgb.astype(np.float32)
    return 116.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    return 200.0 * (fy - fz)


def lab_to_rgb(L, a, b):
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
    b = 0.0556434 * X - 0.2040259 * Y + 1.0572252 * Z
    rgb = np.stack([r, g, b], axis=-1)
    rgb = np.clip(rgb, 0, 1)
    mask = rgb <= 0.0031308
    rgb_srgb = np.where(mask, 12.92 * rgb, 1.055 * np.power(np.maximum(rgb, 1e-12), 1.0 / 2.4) - 0.055)
    rgb_srgb = np.clip(rgb_srgb * 255.0, 0, 255).astype(np.uint8)
    return rgb_srgb


def colorize_image_reuse(session, input_name, input_shape, input_path, output_path):
    original = Image.open(input_path).convert('RGB')
    orig_w, orig_h = original.size
    original_np = np.array(original)
    orig_L = rgb_to_lab_l(original_np)
    gray = original.convert('L')
    gray_resized = gray.resize((INFERENCE_SIZE, INFERENCE_SIZE), Image.BILINEAR)#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    L = 116.0 * fy - 16.0
    return L


def rgb_to_lab_a(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    return 500.0 * (fx - fy)


def rgb_to_lab_b(rgb):
    rgb_f = rgb.astype(np.float32)
    return 116.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    return 200.0 * (fy - fz)


def lab_to_rgb(L, a, b):
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
    b = 0.0556434 * X - 0.2040259 * Y + 1.0572252 * Z
    rgb = np.stack([r, g, b], axis=-1)
    rgb = np.clip(rgb, 0, 1)
    mask = rgb <= 0.0031308
    rgb_srgb = np.where(mask, 12.92 * rgb, 1.055 * np.power(np.maximum(rgb, 1e-12), 1.0 / 2.4) - 0.055)
    rgb_srgb = np.clip(rgb_srgb * 255.0, 0, 255).astype(np.uint8)
    return rgb_srgb


def colorize_image_reuse(session, input_name, input_shape, input_path, output_path):
    original = Image.open(input_path).convert('RGB')
    orig_w, orig_h = original.size
    original_np = np.array(original)
    orig_L = rgb_to_lab_l(original_np)
    gray = original.convert('L')
    gray_resized = gray.resize((INFERENCE_SIZE, INFERENCE_SIZE), Image.BILINEAR)
    input_data = np.array(gray_resized, dtype=np.float32) /#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    L = 116.0 * fy - 16.0
    return L


def rgb_to_lab_a(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    return 500.0 * (fx - fy)


def rgb_to_lab_b(rgb):
    rgb_f = rgb.astype(np.float32)
    return 116.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    return 200.0 * (fy - fz)


def lab_to_rgb(L, a, b):
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
    b = 0.0556434 * X - 0.2040259 * Y + 1.0572252 * Z
    rgb = np.stack([r, g, b], axis=-1)
    rgb = np.clip(rgb, 0, 1)
    mask = rgb <= 0.0031308
    rgb_srgb = np.where(mask, 12.92 * rgb, 1.055 * np.power(np.maximum(rgb, 1e-12), 1.0 / 2.4) - 0.055)
    rgb_srgb = np.clip(rgb_srgb * 255.0, 0, 255).astype(np.uint8)
    return rgb_srgb


def colorize_image_reuse(session, input_name, input_shape, input_path, output_path):
    original = Image.open(input_path).convert('RGB')
    orig_w, orig_h = original.size
    original_np = np.array(original)
    orig_L = rgb_to_lab_l(original_np)
    gray = original.convert('L')
    gray_resized = gray.resize((INFERENCE_SIZE, INFERENCE_SIZE), Image.BILINEAR)
    input_data = np.array(gray_resized, dtype=np.float32) / 255.0
    if len(input_shape) == 4 and input_shape[1#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    L = 116.0 * fy - 16.0
    return L


def rgb_to_lab_a(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    return 500.0 * (fx - fy)


def rgb_to_lab_b(rgb):
    rgb_f = rgb.astype(np.float32)
    return 116.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    return 200.0 * (fy - fz)


def lab_to_rgb(L, a, b):
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
    b = 0.0556434 * X - 0.2040259 * Y + 1.0572252 * Z
    rgb = np.stack([r, g, b], axis=-1)
    rgb = np.clip(rgb, 0, 1)
    mask = rgb <= 0.0031308
    rgb_srgb = np.where(mask, 12.92 * rgb, 1.055 * np.power(np.maximum(rgb, 1e-12), 1.0 / 2.4) - 0.055)
    rgb_srgb = np.clip(rgb_srgb * 255.0, 0, 255).astype(np.uint8)
    return rgb_srgb


def colorize_image_reuse(session, input_name, input_shape, input_path, output_path):
    original = Image.open(input_path).convert('RGB')
    orig_w, orig_h = original.size
    original_np = np.array(original)
    orig_L = rgb_to_lab_l(original_np)
    gray = original.convert('L')
    gray_resized = gray.resize((INFERENCE_SIZE, INFERENCE_SIZE), Image.BILINEAR)
    input_data = np.array(gray_resized, dtype=np.float32) / 255.0
    if len(input_shape) == 4 and input_shape[1] == 3:
        input_data = np.stack([input_data] * 3,#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    L = 116.0 * fy - 16.0
    return L


def rgb_to_lab_a(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    return 500.0 * (fx - fy)


def rgb_to_lab_b(rgb):
    rgb_f = rgb.astype(np.float32)
    return 116.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    return 200.0 * (fy - fz)


def lab_to_rgb(L, a, b):
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
    b = 0.0556434 * X - 0.2040259 * Y + 1.0572252 * Z
    rgb = np.stack([r, g, b], axis=-1)
    rgb = np.clip(rgb, 0, 1)
    mask = rgb <= 0.0031308
    rgb_srgb = np.where(mask, 12.92 * rgb, 1.055 * np.power(np.maximum(rgb, 1e-12), 1.0 / 2.4) - 0.055)
    rgb_srgb = np.clip(rgb_srgb * 255.0, 0, 255).astype(np.uint8)
    return rgb_srgb


def colorize_image_reuse(session, input_name, input_shape, input_path, output_path):
    original = Image.open(input_path).convert('RGB')
    orig_w, orig_h = original.size
    original_np = np.array(original)
    orig_L = rgb_to_lab_l(original_np)
    gray = original.convert('L')
    gray_resized = gray.resize((INFERENCE_SIZE, INFERENCE_SIZE), Image.BILINEAR)
    input_data = np.array(gray_resized, dtype=np.float32) / 255.0
    if len(input_shape) == 4 and input_shape[1] == 3:
        input_data = np.stack([input_data] * 3, axis=0)[np.newaxis, :, :, :]
    else:
#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    L = 116.0 * fy - 16.0
    return L


def rgb_to_lab_a(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    return 500.0 * (fx - fy)


def rgb_to_lab_b(rgb):
    rgb_f = rgb.astype(np.float32)
    return 116.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    return 200.0 * (fy - fz)


def lab_to_rgb(L, a, b):
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
    b = 0.0556434 * X - 0.2040259 * Y + 1.0572252 * Z
    rgb = np.stack([r, g, b], axis=-1)
    rgb = np.clip(rgb, 0, 1)
    mask = rgb <= 0.0031308
    rgb_srgb = np.where(mask, 12.92 * rgb, 1.055 * np.power(np.maximum(rgb, 1e-12), 1.0 / 2.4) - 0.055)
    rgb_srgb = np.clip(rgb_srgb * 255.0, 0, 255).astype(np.uint8)
    return rgb_srgb


def colorize_image_reuse(session, input_name, input_shape, input_path, output_path):
    original = Image.open(input_path).convert('RGB')
    orig_w, orig_h = original.size
    original_np = np.array(original)
    orig_L = rgb_to_lab_l(original_np)
    gray = original.convert('L')
    gray_resized = gray.resize((INFERENCE_SIZE, INFERENCE_SIZE), Image.BILINEAR)
    input_data = np.array(gray_resized, dtype=np.float32) / 255.0
    if len(input_shape) == 4 and input_shape[1] == 3:
        input_data = np.stack([input_data] * 3, axis=0)[np.newaxis, :, :, :]
    else:
        input_data = input_data[np.newaxis, np.newaxis, :, :]
#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    L = 116.0 * fy - 16.0
    return L


def rgb_to_lab_a(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    return 500.0 * (fx - fy)


def rgb_to_lab_b(rgb):
    rgb_f = rgb.astype(np.float32)
    return 116.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    return 200.0 * (fy - fz)


def lab_to_rgb(L, a, b):
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
    b = 0.0556434 * X - 0.2040259 * Y + 1.0572252 * Z
    rgb = np.stack([r, g, b], axis=-1)
    rgb = np.clip(rgb, 0, 1)
    mask = rgb <= 0.0031308
    rgb_srgb = np.where(mask, 12.92 * rgb, 1.055 * np.power(np.maximum(rgb, 1e-12), 1.0 / 2.4) - 0.055)
    rgb_srgb = np.clip(rgb_srgb * 255.0, 0, 255).astype(np.uint8)
    return rgb_srgb


def colorize_image_reuse(session, input_name, input_shape, input_path, output_path):
    original = Image.open(input_path).convert('RGB')
    orig_w, orig_h = original.size
    original_np = np.array(original)
    orig_L = rgb_to_lab_l(original_np)
    gray = original.convert('L')
    gray_resized = gray.resize((INFERENCE_SIZE, INFERENCE_SIZE), Image.BILINEAR)
    input_data = np.array(gray_resized, dtype=np.float32) / 255.0
    if len(input_shape) == 4 and input_shape[1] == 3:
        input_data = np.stack([input_data] * 3, axis=0)[np.newaxis, :, :, :]
    else:
        input_data = input_data[np.newaxis, np.newaxis, :, :]
    outputs = session.run(None, {input_name: input_data})
    output_data = outputs#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    L = 116.0 * fy - 16.0
    return L


def rgb_to_lab_a(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    return 500.0 * (fx - fy)


def rgb_to_lab_b(rgb):
    rgb_f = rgb.astype(np.float32)
    return 116.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    return 200.0 * (fy - fz)


def lab_to_rgb(L, a, b):
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
    b = 0.0556434 * X - 0.2040259 * Y + 1.0572252 * Z
    rgb = np.stack([r, g, b], axis=-1)
    rgb = np.clip(rgb, 0, 1)
    mask = rgb <= 0.0031308
    rgb_srgb = np.where(mask, 12.92 * rgb, 1.055 * np.power(np.maximum(rgb, 1e-12), 1.0 / 2.4) - 0.055)
    rgb_srgb = np.clip(rgb_srgb * 255.0, 0, 255).astype(np.uint8)
    return rgb_srgb


def colorize_image_reuse(session, input_name, input_shape, input_path, output_path):
    original = Image.open(input_path).convert('RGB')
    orig_w, orig_h = original.size
    original_np = np.array(original)
    orig_L = rgb_to_lab_l(original_np)
    gray = original.convert('L')
    gray_resized = gray.resize((INFERENCE_SIZE, INFERENCE_SIZE), Image.BILINEAR)
    input_data = np.array(gray_resized, dtype=np.float32) / 255.0
    if len(input_shape) == 4 and input_shape[1] == 3:
        input_data = np.stack([input_data] * 3, axis=0)[np.newaxis, :, :, :]
    else:
        input_data = input_data[np.newaxis, np.newaxis, :, :]
    outputs = session.run(None, {input_name: input_data})
    output_data = outputs[0]
    if output_data.ndim == 4:
        if output_data.shape#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    L = 116.0 * fy - 16.0
    return L


def rgb_to_lab_a(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    return 500.0 * (fx - fy)


def rgb_to_lab_b(rgb):
    rgb_f = rgb.astype(np.float32)
    return 116.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    return 200.0 * (fy - fz)


def lab_to_rgb(L, a, b):
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
    b = 0.0556434 * X - 0.2040259 * Y + 1.0572252 * Z
    rgb = np.stack([r, g, b], axis=-1)
    rgb = np.clip(rgb, 0, 1)
    mask = rgb <= 0.0031308
    rgb_srgb = np.where(mask, 12.92 * rgb, 1.055 * np.power(np.maximum(rgb, 1e-12), 1.0 / 2.4) - 0.055)
    rgb_srgb = np.clip(rgb_srgb * 255.0, 0, 255).astype(np.uint8)
    return rgb_srgb


def colorize_image_reuse(session, input_name, input_shape, input_path, output_path):
    original = Image.open(input_path).convert('RGB')
    orig_w, orig_h = original.size
    original_np = np.array(original)
    orig_L = rgb_to_lab_l(original_np)
    gray = original.convert('L')
    gray_resized = gray.resize((INFERENCE_SIZE, INFERENCE_SIZE), Image.BILINEAR)
    input_data = np.array(gray_resized, dtype=np.float32) / 255.0
    if len(input_shape) == 4 and input_shape[1] == 3:
        input_data = np.stack([input_data] * 3, axis=0)[np.newaxis, :, :, :]
    else:
        input_data = input_data[np.newaxis, np.newaxis, :, :]
    outputs = session.run(None, {input_name: input_data})
    output_data = outputs[0]
    if output_data.ndim == 4:
        if output_data.shape[1] in (1, 3):
            output_data = np.transpose(output_data#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    L = 116.0 * fy - 16.0
    return L


def rgb_to_lab_a(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    return 500.0 * (fx - fy)


def rgb_to_lab_b(rgb):
    rgb_f = rgb.astype(np.float32)
    return 116.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    return 200.0 * (fy - fz)


def lab_to_rgb(L, a, b):
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
    b = 0.0556434 * X - 0.2040259 * Y + 1.0572252 * Z
    rgb = np.stack([r, g, b], axis=-1)
    rgb = np.clip(rgb, 0, 1)
    mask = rgb <= 0.0031308
    rgb_srgb = np.where(mask, 12.92 * rgb, 1.055 * np.power(np.maximum(rgb, 1e-12), 1.0 / 2.4) - 0.055)
    rgb_srgb = np.clip(rgb_srgb * 255.0, 0, 255).astype(np.uint8)
    return rgb_srgb


def colorize_image_reuse(session, input_name, input_shape, input_path, output_path):
    original = Image.open(input_path).convert('RGB')
    orig_w, orig_h = original.size
    original_np = np.array(original)
    orig_L = rgb_to_lab_l(original_np)
    gray = original.convert('L')
    gray_resized = gray.resize((INFERENCE_SIZE, INFERENCE_SIZE), Image.BILINEAR)
    input_data = np.array(gray_resized, dtype=np.float32) / 255.0
    if len(input_shape) == 4 and input_shape[1] == 3:
        input_data = np.stack([input_data] * 3, axis=0)[np.newaxis, :, :, :]
    else:
        input_data = input_data[np.newaxis, np.newaxis, :, :]
    outputs = session.run(None, {input_name: input_data})
    output_data = outputs[0]
    if output_data.ndim == 4:
        if output_data.shape[1] in (1, 3):
            output_data = np.transpose(output_data[0], (1, 2, 0))
        else:
            output_data#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    L = 116.0 * fy - 16.0
    return L


def rgb_to_lab_a(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    return 500.0 * (fx - fy)


def rgb_to_lab_b(rgb):
    rgb_f = rgb.astype(np.float32)
    return 116.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    return 200.0 * (fy - fz)


def lab_to_rgb(L, a, b):
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
    b = 0.0556434 * X - 0.2040259 * Y + 1.0572252 * Z
    rgb = np.stack([r, g, b], axis=-1)
    rgb = np.clip(rgb, 0, 1)
    mask = rgb <= 0.0031308
    rgb_srgb = np.where(mask, 12.92 * rgb, 1.055 * np.power(np.maximum(rgb, 1e-12), 1.0 / 2.4) - 0.055)
    rgb_srgb = np.clip(rgb_srgb * 255.0, 0, 255).astype(np.uint8)
    return rgb_srgb


def colorize_image_reuse(session, input_name, input_shape, input_path, output_path):
    original = Image.open(input_path).convert('RGB')
    orig_w, orig_h = original.size
    original_np = np.array(original)
    orig_L = rgb_to_lab_l(original_np)
    gray = original.convert('L')
    gray_resized = gray.resize((INFERENCE_SIZE, INFERENCE_SIZE), Image.BILINEAR)
    input_data = np.array(gray_resized, dtype=np.float32) / 255.0
    if len(input_shape) == 4 and input_shape[1] == 3:
        input_data = np.stack([input_data] * 3, axis=0)[np.newaxis, :, :, :]
    else:
        input_data = input_data[np.newaxis, np.newaxis, :, :]
    outputs = session.run(None, {input_name: input_data})
    output_data = outputs[0]
    if output_data.ndim == 4:
        if output_data.shape[1] in (1, 3):
            output_data = np.transpose(output_data[0], (1, 2, 0))
        else:
            output_data = output_data[0]
    output_data = np.squeeze(output_data)
    if#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    L = 116.0 * fy - 16.0
    return L


def rgb_to_lab_a(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    return 500.0 * (fx - fy)


def rgb_to_lab_b(rgb):
    rgb_f = rgb.astype(np.float32)
    return 116.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    return 200.0 * (fy - fz)


def lab_to_rgb(L, a, b):
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
    b = 0.0556434 * X - 0.2040259 * Y + 1.0572252 * Z
    rgb = np.stack([r, g, b], axis=-1)
    rgb = np.clip(rgb, 0, 1)
    mask = rgb <= 0.0031308
    rgb_srgb = np.where(mask, 12.92 * rgb, 1.055 * np.power(np.maximum(rgb, 1e-12), 1.0 / 2.4) - 0.055)
    rgb_srgb = np.clip(rgb_srgb * 255.0, 0, 255).astype(np.uint8)
    return rgb_srgb


def colorize_image_reuse(session, input_name, input_shape, input_path, output_path):
    original = Image.open(input_path).convert('RGB')
    orig_w, orig_h = original.size
    original_np = np.array(original)
    orig_L = rgb_to_lab_l(original_np)
    gray = original.convert('L')
    gray_resized = gray.resize((INFERENCE_SIZE, INFERENCE_SIZE), Image.BILINEAR)
    input_data = np.array(gray_resized, dtype=np.float32) / 255.0
    if len(input_shape) == 4 and input_shape[1] == 3:
        input_data = np.stack([input_data] * 3, axis=0)[np.newaxis, :, :, :]
    else:
        input_data = input_data[np.newaxis, np.newaxis, :, :]
    outputs = session.run(None, {input_name: input_data})
    output_data = outputs[0]
    if output_data.ndim == 4:
        if output_data.shape[1] in (1, 3):
            output_data = np.transpose(output_data[0], (1, 2, 0))
        else:
            output_data = output_data[0]
    output_data = np.squeeze(output_data)
    if output_data.ndim == 2:
        colorized = np.stack([output_data] *#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    L = 116.0 * fy - 16.0
    return L


def rgb_to_lab_a(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    return 500.0 * (fx - fy)


def rgb_to_lab_b(rgb):
    rgb_f = rgb.astype(np.float32)
    return 116.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    return 200.0 * (fy - fz)


def lab_to_rgb(L, a, b):
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
    b = 0.0556434 * X - 0.2040259 * Y + 1.0572252 * Z
    rgb = np.stack([r, g, b], axis=-1)
    rgb = np.clip(rgb, 0, 1)
    mask = rgb <= 0.0031308
    rgb_srgb = np.where(mask, 12.92 * rgb, 1.055 * np.power(np.maximum(rgb, 1e-12), 1.0 / 2.4) - 0.055)
    rgb_srgb = np.clip(rgb_srgb * 255.0, 0, 255).astype(np.uint8)
    return rgb_srgb


def colorize_image_reuse(session, input_name, input_shape, input_path, output_path):
    original = Image.open(input_path).convert('RGB')
    orig_w, orig_h = original.size
    original_np = np.array(original)
    orig_L = rgb_to_lab_l(original_np)
    gray = original.convert('L')
    gray_resized = gray.resize((INFERENCE_SIZE, INFERENCE_SIZE), Image.BILINEAR)
    input_data = np.array(gray_resized, dtype=np.float32) / 255.0
    if len(input_shape) == 4 and input_shape[1] == 3:
        input_data = np.stack([input_data] * 3, axis=0)[np.newaxis, :, :, :]
    else:
        input_data = input_data[np.newaxis, np.newaxis, :, :]
    outputs = session.run(None, {input_name: input_data})
    output_data = outputs[0]
    if output_data.ndim == 4:
        if output_data.shape[1] in (1, 3):
            output_data = np.transpose(output_data[0], (1, 2, 0))
        else:
            output_data = output_data[0]
    output_data = np.squeeze(output_data)
    if output_data.ndim == 2:
        colorized = np.stack([output_data] * 3, axis=-1)
    elif output_data.shape[-1] == 3:#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    L = 116.0 * fy - 16.0
    return L


def rgb_to_lab_a(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    return 500.0 * (fx - fy)


def rgb_to_lab_b(rgb):
    rgb_f = rgb.astype(np.float32)
    return 116.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    return 200.0 * (fy - fz)


def lab_to_rgb(L, a, b):
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
    b = 0.0556434 * X - 0.2040259 * Y + 1.0572252 * Z
    rgb = np.stack([r, g, b], axis=-1)
    rgb = np.clip(rgb, 0, 1)
    mask = rgb <= 0.0031308
    rgb_srgb = np.where(mask, 12.92 * rgb, 1.055 * np.power(np.maximum(rgb, 1e-12), 1.0 / 2.4) - 0.055)
    rgb_srgb = np.clip(rgb_srgb * 255.0, 0, 255).astype(np.uint8)
    return rgb_srgb


def colorize_image_reuse(session, input_name, input_shape, input_path, output_path):
    original = Image.open(input_path).convert('RGB')
    orig_w, orig_h = original.size
    original_np = np.array(original)
    orig_L = rgb_to_lab_l(original_np)
    gray = original.convert('L')
    gray_resized = gray.resize((INFERENCE_SIZE, INFERENCE_SIZE), Image.BILINEAR)
    input_data = np.array(gray_resized, dtype=np.float32) / 255.0
    if len(input_shape) == 4 and input_shape[1] == 3:
        input_data = np.stack([input_data] * 3, axis=0)[np.newaxis, :, :, :]
    else:
        input_data = input_data[np.newaxis, np.newaxis, :, :]
    outputs = session.run(None, {input_name: input_data})
    output_data = outputs[0]
    if output_data.ndim == 4:
        if output_data.shape[1] in (1, 3):
            output_data = np.transpose(output_data[0], (1, 2, 0))
        else:
            output_data = output_data[0]
    output_data = np.squeeze(output_data)
    if output_data.ndim == 2:
        colorized = np.stack([output_data] * 3, axis=-1)
    elif output_data.shape[-1] == 3:
        colorized = output_data
    elif output_data.shape[-1] == 2:#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    L = 116.0 * fy - 16.0
    return L


def rgb_to_lab_a(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    return 500.0 * (fx - fy)


def rgb_to_lab_b(rgb):
    rgb_f = rgb.astype(np.float32)
    return 116.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    return 200.0 * (fy - fz)


def lab_to_rgb(L, a, b):
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
    b = 0.0556434 * X - 0.2040259 * Y + 1.0572252 * Z
    rgb = np.stack([r, g, b], axis=-1)
    rgb = np.clip(rgb, 0, 1)
    mask = rgb <= 0.0031308
    rgb_srgb = np.where(mask, 12.92 * rgb, 1.055 * np.power(np.maximum(rgb, 1e-12), 1.0 / 2.4) - 0.055)
    rgb_srgb = np.clip(rgb_srgb * 255.0, 0, 255).astype(np.uint8)
    return rgb_srgb


def colorize_image_reuse(session, input_name, input_shape, input_path, output_path):
    original = Image.open(input_path).convert('RGB')
    orig_w, orig_h = original.size
    original_np = np.array(original)
    orig_L = rgb_to_lab_l(original_np)
    gray = original.convert('L')
    gray_resized = gray.resize((INFERENCE_SIZE, INFERENCE_SIZE), Image.BILINEAR)
    input_data = np.array(gray_resized, dtype=np.float32) / 255.0
    if len(input_shape) == 4 and input_shape[1] == 3:
        input_data = np.stack([input_data] * 3, axis=0)[np.newaxis, :, :, :]
    else:
        input_data = input_data[np.newaxis, np.newaxis, :, :]
    outputs = session.run(None, {input_name: input_data})
    output_data = outputs[0]
    if output_data.ndim == 4:
        if output_data.shape[1] in (1, 3):
            output_data = np.transpose(output_data[0], (1, 2, 0))
        else:
            output_data = output_data[0]
    output_data = np.squeeze(output_data)
    if output_data.ndim == 2:
        colorized = np.stack([output_data] * 3, axis=-1)
    elif output_data.shape[-1] == 3:
        colorized = output_data
    elif output_data.shape[-1] == 2:
        pass
    else:
        colorized = output_data[..., :3]
#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    L = 116.0 * fy - 16.0
    return L


def rgb_to_lab_a(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    return 500.0 * (fx - fy)


def rgb_to_lab_b(rgb):
    rgb_f = rgb.astype(np.float32)
    return 116.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    return 200.0 * (fy - fz)


def lab_to_rgb(L, a, b):
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
    b = 0.0556434 * X - 0.2040259 * Y + 1.0572252 * Z
    rgb = np.stack([r, g, b], axis=-1)
    rgb = np.clip(rgb, 0, 1)
    mask = rgb <= 0.0031308
    rgb_srgb = np.where(mask, 12.92 * rgb, 1.055 * np.power(np.maximum(rgb, 1e-12), 1.0 / 2.4) - 0.055)
    rgb_srgb = np.clip(rgb_srgb * 255.0, 0, 255).astype(np.uint8)
    return rgb_srgb


def colorize_image_reuse(session, input_name, input_shape, input_path, output_path):
    original = Image.open(input_path).convert('RGB')
    orig_w, orig_h = original.size
    original_np = np.array(original)
    orig_L = rgb_to_lab_l(original_np)
    gray = original.convert('L')
    gray_resized = gray.resize((INFERENCE_SIZE, INFERENCE_SIZE), Image.BILINEAR)
    input_data = np.array(gray_resized, dtype=np.float32) / 255.0
    if len(input_shape) == 4 and input_shape[1] == 3:
        input_data = np.stack([input_data] * 3, axis=0)[np.newaxis, :, :, :]
    else:
        input_data = input_data[np.newaxis, np.newaxis, :, :]
    outputs = session.run(None, {input_name: input_data})
    output_data = outputs[0]
    if output_data.ndim == 4:
        if output_data.shape[1] in (1, 3):
            output_data = np.transpose(output_data[0], (1, 2, 0))
        else:
            output_data = output_data[0]
    output_data = np.squeeze(output_data)
    if output_data.ndim == 2:
        colorized = np.stack([output_data] * 3, axis=-1)
    elif output_data.shape[-1] == 3:
        colorized = output_data
    elif output_data.shape[-1] == 2:
        pass
    else:
        colorized = output_data[..., :3]
    if output_data.ndim == 3 and output_data.shape[-1] == 3:#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    L = 116.0 * fy - 16.0
    return L


def rgb_to_lab_a(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    return 500.0 * (fx - fy)


def rgb_to_lab_b(rgb):
    rgb_f = rgb.astype(np.float32)
    return 116.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    return 200.0 * (fy - fz)


def lab_to_rgb(L, a, b):
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
    b = 0.0556434 * X - 0.2040259 * Y + 1.0572252 * Z
    rgb = np.stack([r, g, b], axis=-1)
    rgb = np.clip(rgb, 0, 1)
    mask = rgb <= 0.0031308
    rgb_srgb = np.where(mask, 12.92 * rgb, 1.055 * np.power(np.maximum(rgb, 1e-12), 1.0 / 2.4) - 0.055)
    rgb_srgb = np.clip(rgb_srgb * 255.0, 0, 255).astype(np.uint8)
    return rgb_srgb


def colorize_image_reuse(session, input_name, input_shape, input_path, output_path):
    original = Image.open(input_path).convert('RGB')
    orig_w, orig_h = original.size
    original_np = np.array(original)
    orig_L = rgb_to_lab_l(original_np)
    gray = original.convert('L')
    gray_resized = gray.resize((INFERENCE_SIZE, INFERENCE_SIZE), Image.BILINEAR)
    input_data = np.array(gray_resized, dtype=np.float32) / 255.0
    if len(input_shape) == 4 and input_shape[1] == 3:
        input_data = np.stack([input_data] * 3, axis=0)[np.newaxis, :, :, :]
    else:
        input_data = input_data[np.newaxis, np.newaxis, :, :]
    outputs = session.run(None, {input_name: input_data})
    output_data = outputs[0]
    if output_data.ndim == 4:
        if output_data.shape[1] in (1, 3):
            output_data = np.transpose(output_data[0], (1, 2, 0))
        else:
            output_data = output_data[0]
    output_data = np.squeeze(output_data)
    if output_data.ndim == 2:
        colorized = np.stack([output_data] * 3, axis=-1)
    elif output_data.shape[-1] == 3:
        colorized = output_data
    elif output_data.shape[-1] == 2:
        pass
    else:
        colorized = output_data[..., :3]
    if output_data.ndim == 3 and output_data.shape[-1] == 3:
        out_a = rgb_to_lab_a(colorized)
        out_b = rgb_to#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    L = 116.0 * fy - 16.0
    return L


def rgb_to_lab_a(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    return 500.0 * (fx - fy)


def rgb_to_lab_b(rgb):
    rgb_f = rgb.astype(np.float32)
    return 116.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    return 200.0 * (fy - fz)


def lab_to_rgb(L, a, b):
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
    b = 0.0556434 * X - 0.2040259 * Y + 1.0572252 * Z
    rgb = np.stack([r, g, b], axis=-1)
    rgb = np.clip(rgb, 0, 1)
    mask = rgb <= 0.0031308
    rgb_srgb = np.where(mask, 12.92 * rgb, 1.055 * np.power(np.maximum(rgb, 1e-12), 1.0 / 2.4) - 0.055)
    rgb_srgb = np.clip(rgb_srgb * 255.0, 0, 255).astype(np.uint8)
    return rgb_srgb


def colorize_image_reuse(session, input_name, input_shape, input_path, output_path):
    original = Image.open(input_path).convert('RGB')
    orig_w, orig_h = original.size
    original_np = np.array(original)
    orig_L = rgb_to_lab_l(original_np)
    gray = original.convert('L')
    gray_resized = gray.resize((INFERENCE_SIZE, INFERENCE_SIZE), Image.BILINEAR)
    input_data = np.array(gray_resized, dtype=np.float32) / 255.0
    if len(input_shape) == 4 and input_shape[1] == 3:
        input_data = np.stack([input_data] * 3, axis=0)[np.newaxis, :, :, :]
    else:
        input_data = input_data[np.newaxis, np.newaxis, :, :]
    outputs = session.run(None, {input_name: input_data})
    output_data = outputs[0]
    if output_data.ndim == 4:
        if output_data.shape[1] in (1, 3):
            output_data = np.transpose(output_data[0], (1, 2, 0))
        else:
            output_data = output_data[0]
    output_data = np.squeeze(output_data)
    if output_data.ndim == 2:
        colorized = np.stack([output_data] * 3, axis=-1)
    elif output_data.shape[-1] == 3:
        colorized = output_data
    elif output_data.shape[-1] == 2:
        pass
    else:
        colorized = output_data[..., :3]
    if output_data.ndim == 3 and output_data.shape[-1] == 3:
        out_a = rgb_to_lab_a(colorized)
        out_b = rgb_to_lab_b(colorized)
    elif output#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    L = 116.0 * fy - 16.0
    return L


def rgb_to_lab_a(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    return 500.0 * (fx - fy)


def rgb_to_lab_b(rgb):
    rgb_f = rgb.astype(np.float32)
    return 116.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    return 200.0 * (fy - fz)


def lab_to_rgb(L, a, b):
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
    b = 0.0556434 * X - 0.2040259 * Y + 1.0572252 * Z
    rgb = np.stack([r, g, b], axis=-1)
    rgb = np.clip(rgb, 0, 1)
    mask = rgb <= 0.0031308
    rgb_srgb = np.where(mask, 12.92 * rgb, 1.055 * np.power(np.maximum(rgb, 1e-12), 1.0 / 2.4) - 0.055)
    rgb_srgb = np.clip(rgb_srgb * 255.0, 0, 255).astype(np.uint8)
    return rgb_srgb


def colorize_image_reuse(session, input_name, input_shape, input_path, output_path):
    original = Image.open(input_path).convert('RGB')
    orig_w, orig_h = original.size
    original_np = np.array(original)
    orig_L = rgb_to_lab_l(original_np)
    gray = original.convert('L')
    gray_resized = gray.resize((INFERENCE_SIZE, INFERENCE_SIZE), Image.BILINEAR)
    input_data = np.array(gray_resized, dtype=np.float32) / 255.0
    if len(input_shape) == 4 and input_shape[1] == 3:
        input_data = np.stack([input_data] * 3, axis=0)[np.newaxis, :, :, :]
    else:
        input_data = input_data[np.newaxis, np.newaxis, :, :]
    outputs = session.run(None, {input_name: input_data})
    output_data = outputs[0]
    if output_data.ndim == 4:
        if output_data.shape[1] in (1, 3):
            output_data = np.transpose(output_data[0], (1, 2, 0))
        else:
            output_data = output_data[0]
    output_data = np.squeeze(output_data)
    if output_data.ndim == 2:
        colorized = np.stack([output_data] * 3, axis=-1)
    elif output_data.shape[-1] == 3:
        colorized = output_data
    elif output_data.shape[-1] == 2:
        pass
    else:
        colorized = output_data[..., :3]
    if output_data.ndim == 3 and output_data.shape[-1] == 3:
        out_a = rgb_to_lab_a(colorized)
        out_b = rgb_to_lab_b(colorized)
    elif output_data.ndim == 3 and output_data.shape[-1] == 2:
        out#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    L = 116.0 * fy - 16.0
    return L


def rgb_to_lab_a(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    return 500.0 * (fx - fy)


def rgb_to_lab_b(rgb):
    rgb_f = rgb.astype(np.float32)
    return 116.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    return 200.0 * (fy - fz)


def lab_to_rgb(L, a, b):
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
    b = 0.0556434 * X - 0.2040259 * Y + 1.0572252 * Z
    rgb = np.stack([r, g, b], axis=-1)
    rgb = np.clip(rgb, 0, 1)
    mask = rgb <= 0.0031308
    rgb_srgb = np.where(mask, 12.92 * rgb, 1.055 * np.power(np.maximum(rgb, 1e-12), 1.0 / 2.4) - 0.055)
    rgb_srgb = np.clip(rgb_srgb * 255.0, 0, 255).astype(np.uint8)
    return rgb_srgb


def colorize_image_reuse(session, input_name, input_shape, input_path, output_path):
    original = Image.open(input_path).convert('RGB')
    orig_w, orig_h = original.size
    original_np = np.array(original)
    orig_L = rgb_to_lab_l(original_np)
    gray = original.convert('L')
    gray_resized = gray.resize((INFERENCE_SIZE, INFERENCE_SIZE), Image.BILINEAR)
    input_data = np.array(gray_resized, dtype=np.float32) / 255.0
    if len(input_shape) == 4 and input_shape[1] == 3:
        input_data = np.stack([input_data] * 3, axis=0)[np.newaxis, :, :, :]
    else:
        input_data = input_data[np.newaxis, np.newaxis, :, :]
    outputs = session.run(None, {input_name: input_data})
    output_data = outputs[0]
    if output_data.ndim == 4:
        if output_data.shape[1] in (1, 3):
            output_data = np.transpose(output_data[0], (1, 2, 0))
        else:
            output_data = output_data[0]
    output_data = np.squeeze(output_data)
    if output_data.ndim == 2:
        colorized = np.stack([output_data] * 3, axis=-1)
    elif output_data.shape[-1] == 3:
        colorized = output_data
    elif output_data.shape[-1] == 2:
        pass
    else:
        colorized = output_data[..., :3]
    if output_data.ndim == 3 and output_data.shape[-1] == 3:
        out_a = rgb_to_lab_a(colorized)
        out_b = rgb_to_lab_b(colorized)
    elif output_data.ndim == 3 and output_data.shape[-1] == 2:
        out_a = output_data[..., 0]
#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    L = 116.0 * fy - 16.0
    return L


def rgb_to_lab_a(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    return 500.0 * (fx - fy)


def rgb_to_lab_b(rgb):
    rgb_f = rgb.astype(np.float32)
    return 116.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    return 200.0 * (fy - fz)


def lab_to_rgb(L, a, b):
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
    b = 0.0556434 * X - 0.2040259 * Y + 1.0572252 * Z
    rgb = np.stack([r, g, b], axis=-1)
    rgb = np.clip(rgb, 0, 1)
    mask = rgb <= 0.0031308
    rgb_srgb = np.where(mask, 12.92 * rgb, 1.055 * np.power(np.maximum(rgb, 1e-12), 1.0 / 2.4) - 0.055)
    rgb_srgb = np.clip(rgb_srgb * 255.0, 0, 255).astype(np.uint8)
    return rgb_srgb


def colorize_image_reuse(session, input_name, input_shape, input_path, output_path):
    original = Image.open(input_path).convert('RGB')
    orig_w, orig_h = original.size
    original_np = np.array(original)
    orig_L = rgb_to_lab_l(original_np)
    gray = original.convert('L')
    gray_resized = gray.resize((INFERENCE_SIZE, INFERENCE_SIZE), Image.BILINEAR)
    input_data = np.array(gray_resized, dtype=np.float32) / 255.0
    if len(input_shape) == 4 and input_shape[1] == 3:
        input_data = np.stack([input_data] * 3, axis=0)[np.newaxis, :, :, :]
    else:
        input_data = input_data[np.newaxis, np.newaxis, :, :]
    outputs = session.run(None, {input_name: input_data})
    output_data = outputs[0]
    if output_data.ndim == 4:
        if output_data.shape[1] in (1, 3):
            output_data = np.transpose(output_data[0], (1, 2, 0))
        else:
            output_data = output_data[0]
    output_data = np.squeeze(output_data)
    if output_data.ndim == 2:
        colorized = np.stack([output_data] * 3, axis=-1)
    elif output_data.shape[-1] == 3:
        colorized = output_data
    elif output_data.shape[-1] == 2:
        pass
    else:
        colorized = output_data[..., :3]
    if output_data.ndim == 3 and output_data.shape[-1] == 3:
        out_a = rgb_to_lab_a(colorized)
        out_b = rgb_to_lab_b(colorized)
    elif output_data.ndim == 3 and output_data.shape[-1] == 2:
        out_a = output_data[..., 0]
        out_b = output_data[..., 1#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    L = 116.0 * fy - 16.0
    return L


def rgb_to_lab_a(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    return 500.0 * (fx - fy)


def rgb_to_lab_b(rgb):
    rgb_f = rgb.astype(np.float32)
    return 116.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    return 200.0 * (fy - fz)


def lab_to_rgb(L, a, b):
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
    b = 0.0556434 * X - 0.2040259 * Y + 1.0572252 * Z
    rgb = np.stack([r, g, b], axis=-1)
    rgb = np.clip(rgb, 0, 1)
    mask = rgb <= 0.0031308
    rgb_srgb = np.where(mask, 12.92 * rgb, 1.055 * np.power(np.maximum(rgb, 1e-12), 1.0 / 2.4) - 0.055)
    rgb_srgb = np.clip(rgb_srgb * 255.0, 0, 255).astype(np.uint8)
    return rgb_srgb


def colorize_image_reuse(session, input_name, input_shape, input_path, output_path):
    original = Image.open(input_path).convert('RGB')
    orig_w, orig_h = original.size
    original_np = np.array(original)
    orig_L = rgb_to_lab_l(original_np)
    gray = original.convert('L')
    gray_resized = gray.resize((INFERENCE_SIZE, INFERENCE_SIZE), Image.BILINEAR)
    input_data = np.array(gray_resized, dtype=np.float32) / 255.0
    if len(input_shape) == 4 and input_shape[1] == 3:
        input_data = np.stack([input_data] * 3, axis=0)[np.newaxis, :, :, :]
    else:
        input_data = input_data[np.newaxis, np.newaxis, :, :]
    outputs = session.run(None, {input_name: input_data})
    output_data = outputs[0]
    if output_data.ndim == 4:
        if output_data.shape[1] in (1, 3):
            output_data = np.transpose(output_data[0], (1, 2, 0))
        else:
            output_data = output_data[0]
    output_data = np.squeeze(output_data)
    if output_data.ndim == 2:
        colorized = np.stack([output_data] * 3, axis=-1)
    elif output_data.shape[-1] == 3:
        colorized = output_data
    elif output_data.shape[-1] == 2:
        pass
    else:
        colorized = output_data[..., :3]
    if output_data.ndim == 3 and output_data.shape[-1] == 3:
        out_a = rgb_to_lab_a(colorized)
        out_b = rgb_to_lab_b(colorized)
    elif output_data.ndim == 3 and output_data.shape[-1] == 2:
        out_a = output_data[..., 0]
        out_b = output_data[..., 1]
    else:
        if colorized.max() <= 1.0:
#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    L = 116.0 * fy - 16.0
    return L


def rgb_to_lab_a(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    return 500.0 * (fx - fy)


def rgb_to_lab_b(rgb):
    rgb_f = rgb.astype(np.float32)
    return 116.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    return 200.0 * (fy - fz)


def lab_to_rgb(L, a, b):
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
    b = 0.0556434 * X - 0.2040259 * Y + 1.0572252 * Z
    rgb = np.stack([r, g, b], axis=-1)
    rgb = np.clip(rgb, 0, 1)
    mask = rgb <= 0.0031308
    rgb_srgb = np.where(mask, 12.92 * rgb, 1.055 * np.power(np.maximum(rgb, 1e-12), 1.0 / 2.4) - 0.055)
    rgb_srgb = np.clip(rgb_srgb * 255.0, 0, 255).astype(np.uint8)
    return rgb_srgb


def colorize_image_reuse(session, input_name, input_shape, input_path, output_path):
    original = Image.open(input_path).convert('RGB')
    orig_w, orig_h = original.size
    original_np = np.array(original)
    orig_L = rgb_to_lab_l(original_np)
    gray = original.convert('L')
    gray_resized = gray.resize((INFERENCE_SIZE, INFERENCE_SIZE), Image.BILINEAR)
    input_data = np.array(gray_resized, dtype=np.float32) / 255.0
    if len(input_shape) == 4 and input_shape[1] == 3:
        input_data = np.stack([input_data] * 3, axis=0)[np.newaxis, :, :, :]
    else:
        input_data = input_data[np.newaxis, np.newaxis, :, :]
    outputs = session.run(None, {input_name: input_data})
    output_data = outputs[0]
    if output_data.ndim == 4:
        if output_data.shape[1] in (1, 3):
            output_data = np.transpose(output_data[0], (1, 2, 0))
        else:
            output_data = output_data[0]
    output_data = np.squeeze(output_data)
    if output_data.ndim == 2:
        colorized = np.stack([output_data] * 3, axis=-1)
    elif output_data.shape[-1] == 3:
        colorized = output_data
    elif output_data.shape[-1] == 2:
        pass
    else:
        colorized = output_data[..., :3]
    if output_data.ndim == 3 and output_data.shape[-1] == 3:
        out_a = rgb_to_lab_a(colorized)
        out_b = rgb_to_lab_b(colorized)
    elif output_data.ndim == 3 and output_data.shape[-1] == 2:
        out_a = output_data[..., 0]
        out_b = output_data[..., 1]
    else:
        if colorized.max() <= 1.0:
            colorized = (colorized * 25#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    L = 116.0 * fy - 16.0
    return L


def rgb_to_lab_a(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    return 500.0 * (fx - fy)


def rgb_to_lab_b(rgb):
    rgb_f = rgb.astype(np.float32)
    return 116.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    return 200.0 * (fy - fz)


def lab_to_rgb(L, a, b):
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
    b = 0.0556434 * X - 0.2040259 * Y + 1.0572252 * Z
    rgb = np.stack([r, g, b], axis=-1)
    rgb = np.clip(rgb, 0, 1)
    mask = rgb <= 0.0031308
    rgb_srgb = np.where(mask, 12.92 * rgb, 1.055 * np.power(np.maximum(rgb, 1e-12), 1.0 / 2.4) - 0.055)
    rgb_srgb = np.clip(rgb_srgb * 255.0, 0, 255).astype(np.uint8)
    return rgb_srgb


def colorize_image_reuse(session, input_name, input_shape, input_path, output_path):
    original = Image.open(input_path).convert('RGB')
    orig_w, orig_h = original.size
    original_np = np.array(original)
    orig_L = rgb_to_lab_l(original_np)
    gray = original.convert('L')
    gray_resized = gray.resize((INFERENCE_SIZE, INFERENCE_SIZE), Image.BILINEAR)
    input_data = np.array(gray_resized, dtype=np.float32) / 255.0
    if len(input_shape) == 4 and input_shape[1] == 3:
        input_data = np.stack([input_data] * 3, axis=0)[np.newaxis, :, :, :]
    else:
        input_data = input_data[np.newaxis, np.newaxis, :, :]
    outputs = session.run(None, {input_name: input_data})
    output_data = outputs[0]
    if output_data.ndim == 4:
        if output_data.shape[1] in (1, 3):
            output_data = np.transpose(output_data[0], (1, 2, 0))
        else:
            output_data = output_data[0]
    output_data = np.squeeze(output_data)
    if output_data.ndim == 2:
        colorized = np.stack([output_data] * 3, axis=-1)
    elif output_data.shape[-1] == 3:
        colorized = output_data
    elif output_data.shape[-1] == 2:
        pass
    else:
        colorized = output_data[..., :3]
    if output_data.ndim == 3 and output_data.shape[-1] == 3:
        out_a = rgb_to_lab_a(colorized)
        out_b = rgb_to_lab_b(colorized)
    elif output_data.ndim == 3 and output_data.shape[-1] == 2:
        out_a = output_data[..., 0]
        out_b = output_data[..., 1]
    else:
        if colorized.max() <= 1.0:
            colorized = (colorized * 255).astype(np.uint8)
#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    L = 116.0 * fy - 16.0
    return L


def rgb_to_lab_a(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    return 500.0 * (fx - fy)


def rgb_to_lab_b(rgb):
    rgb_f = rgb.astype(np.float32)
    return 116.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    return 200.0 * (fy - fz)


def lab_to_rgb(L, a, b):
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
    b = 0.0556434 * X - 0.2040259 * Y + 1.0572252 * Z
    rgb = np.stack([r, g, b], axis=-1)
    rgb = np.clip(rgb, 0, 1)
    mask = rgb <= 0.0031308
    rgb_srgb = np.where(mask, 12.92 * rgb, 1.055 * np.power(np.maximum(rgb, 1e-12), 1.0 / 2.4) - 0.055)
    rgb_srgb = np.clip(rgb_srgb * 255.0, 0, 255).astype(np.uint8)
    return rgb_srgb


def colorize_image_reuse(session, input_name, input_shape, input_path, output_path):
    original = Image.open(input_path).convert('RGB')
    orig_w, orig_h = original.size
    original_np = np.array(original)
    orig_L = rgb_to_lab_l(original_np)
    gray = original.convert('L')
    gray_resized = gray.resize((INFERENCE_SIZE, INFERENCE_SIZE), Image.BILINEAR)
    input_data = np.array(gray_resized, dtype=np.float32) / 255.0
    if len(input_shape) == 4 and input_shape[1] == 3:
        input_data = np.stack([input_data] * 3, axis=0)[np.newaxis, :, :, :]
    else:
        input_data = input_data[np.newaxis, np.newaxis, :, :]
    outputs = session.run(None, {input_name: input_data})
    output_data = outputs[0]
    if output_data.ndim == 4:
        if output_data.shape[1] in (1, 3):
            output_data = np.transpose(output_data[0], (1, 2, 0))
        else:
            output_data = output_data[0]
    output_data = np.squeeze(output_data)
    if output_data.ndim == 2:
        colorized = np.stack([output_data] * 3, axis=-1)
    elif output_data.shape[-1] == 3:
        colorized = output_data
    elif output_data.shape[-1] == 2:
        pass
    else:
        colorized = output_data[..., :3]
    if output_data.ndim == 3 and output_data.shape[-1] == 3:
        out_a = rgb_to_lab_a(colorized)
        out_b = rgb_to_lab_b(colorized)
    elif output_data.ndim == 3 and output_data.shape[-1] == 2:
        out_a = output_data[..., 0]
        out_b = output_data[..., 1]
    else:
        if colorized.max() <= 1.0:
            colorized = (colorized * 255).astype(np.uint8)
        result = Image.fromarray(colorized).resize((#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    L = 116.0 * fy - 16.0
    return L


def rgb_to_lab_a(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    return 500.0 * (fx - fy)


def rgb_to_lab_b(rgb):
    rgb_f = rgb.astype(np.float32)
    return 116.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    return 200.0 * (fy - fz)


def lab_to_rgb(L, a, b):
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
    b = 0.0556434 * X - 0.2040259 * Y + 1.0572252 * Z
    rgb = np.stack([r, g, b], axis=-1)
    rgb = np.clip(rgb, 0, 1)
    mask = rgb <= 0.0031308
    rgb_srgb = np.where(mask, 12.92 * rgb, 1.055 * np.power(np.maximum(rgb, 1e-12), 1.0 / 2.4) - 0.055)
    rgb_srgb = np.clip(rgb_srgb * 255.0, 0, 255).astype(np.uint8)
    return rgb_srgb


def colorize_image_reuse(session, input_name, input_shape, input_path, output_path):
    original = Image.open(input_path).convert('RGB')
    orig_w, orig_h = original.size
    original_np = np.array(original)
    orig_L = rgb_to_lab_l(original_np)
    gray = original.convert('L')
    gray_resized = gray.resize((INFERENCE_SIZE, INFERENCE_SIZE), Image.BILINEAR)
    input_data = np.array(gray_resized, dtype=np.float32) / 255.0
    if len(input_shape) == 4 and input_shape[1] == 3:
        input_data = np.stack([input_data] * 3, axis=0)[np.newaxis, :, :, :]
    else:
        input_data = input_data[np.newaxis, np.newaxis, :, :]
    outputs = session.run(None, {input_name: input_data})
    output_data = outputs[0]
    if output_data.ndim == 4:
        if output_data.shape[1] in (1, 3):
            output_data = np.transpose(output_data[0], (1, 2, 0))
        else:
            output_data = output_data[0]
    output_data = np.squeeze(output_data)
    if output_data.ndim == 2:
        colorized = np.stack([output_data] * 3, axis=-1)
    elif output_data.shape[-1] == 3:
        colorized = output_data
    elif output_data.shape[-1] == 2:
        pass
    else:
        colorized = output_data[..., :3]
    if output_data.ndim == 3 and output_data.shape[-1] == 3:
        out_a = rgb_to_lab_a(colorized)
        out_b = rgb_to_lab_b(colorized)
    elif output_data.ndim == 3 and output_data.shape[-1] == 2:
        out_a = output_data[..., 0]
        out_b = output_data[..., 1]
    else:
        if colorized.max() <= 1.0:
            colorized = (colorized * 255).astype(np.uint8)
        result = Image.fromarray(colorized).resize((orig_w, orig_h), Image.BILINE#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    L = 116.0 * fy - 16.0
    return L


def rgb_to_lab_a(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    return 500.0 * (fx - fy)


def rgb_to_lab_b(rgb):
    rgb_f = rgb.astype(np.float32)
    return 116.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    return 200.0 * (fy - fz)


def lab_to_rgb(L, a, b):
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
    b = 0.0556434 * X - 0.2040259 * Y + 1.0572252 * Z
    rgb = np.stack([r, g, b], axis=-1)
    rgb = np.clip(rgb, 0, 1)
    mask = rgb <= 0.0031308
    rgb_srgb = np.where(mask, 12.92 * rgb, 1.055 * np.power(np.maximum(rgb, 1e-12), 1.0 / 2.4) - 0.055)
    rgb_srgb = np.clip(rgb_srgb * 255.0, 0, 255).astype(np.uint8)
    return rgb_srgb


def colorize_image_reuse(session, input_name, input_shape, input_path, output_path):
    original = Image.open(input_path).convert('RGB')
    orig_w, orig_h = original.size
    original_np = np.array(original)
    orig_L = rgb_to_lab_l(original_np)
    gray = original.convert('L')
    gray_resized = gray.resize((INFERENCE_SIZE, INFERENCE_SIZE), Image.BILINEAR)
    input_data = np.array(gray_resized, dtype=np.float32) / 255.0
    if len(input_shape) == 4 and input_shape[1] == 3:
        input_data = np.stack([input_data] * 3, axis=0)[np.newaxis, :, :, :]
    else:
        input_data = input_data[np.newaxis, np.newaxis, :, :]
    outputs = session.run(None, {input_name: input_data})
    output_data = outputs[0]
    if output_data.ndim == 4:
        if output_data.shape[1] in (1, 3):
            output_data = np.transpose(output_data[0], (1, 2, 0))
        else:
            output_data = output_data[0]
    output_data = np.squeeze(output_data)
    if output_data.ndim == 2:
        colorized = np.stack([output_data] * 3, axis=-1)
    elif output_data.shape[-1] == 3:
        colorized = output_data
    elif output_data.shape[-1] == 2:
        pass
    else:
        colorized = output_data[..., :3]
    if output_data.ndim == 3 and output_data.shape[-1] == 3:
        out_a = rgb_to_lab_a(colorized)
        out_b = rgb_to_lab_b(colorized)
    elif output_data.ndim == 3 and output_data.shape[-1] == 2:
        out_a = output_data[..., 0]
        out_b = output_data[..., 1]
    else:
        if colorized.max() <= 1.0:
            colorized = (colorized * 255).astype(np.uint8)
        result = Image.fromarray(colorized).resize((orig_w, orig_h), Image.BILINEAR)
        result.save(output_path)
#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    L = 116.0 * fy - 16.0
    return L


def rgb_to_lab_a(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    return 500.0 * (fx - fy)


def rgb_to_lab_b(rgb):
    rgb_f = rgb.astype(np.float32)
    return 116.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    return 200.0 * (fy - fz)


def lab_to_rgb(L, a, b):
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
    b = 0.0556434 * X - 0.2040259 * Y + 1.0572252 * Z
    rgb = np.stack([r, g, b], axis=-1)
    rgb = np.clip(rgb, 0, 1)
    mask = rgb <= 0.0031308
    rgb_srgb = np.where(mask, 12.92 * rgb, 1.055 * np.power(np.maximum(rgb, 1e-12), 1.0 / 2.4) - 0.055)
    rgb_srgb = np.clip(rgb_srgb * 255.0, 0, 255).astype(np.uint8)
    return rgb_srgb


def colorize_image_reuse(session, input_name, input_shape, input_path, output_path):
    original = Image.open(input_path).convert('RGB')
    orig_w, orig_h = original.size
    original_np = np.array(original)
    orig_L = rgb_to_lab_l(original_np)
    gray = original.convert('L')
    gray_resized = gray.resize((INFERENCE_SIZE, INFERENCE_SIZE), Image.BILINEAR)
    input_data = np.array(gray_resized, dtype=np.float32) / 255.0
    if len(input_shape) == 4 and input_shape[1] == 3:
        input_data = np.stack([input_data] * 3, axis=0)[np.newaxis, :, :, :]
    else:
        input_data = input_data[np.newaxis, np.newaxis, :, :]
    outputs = session.run(None, {input_name: input_data})
    output_data = outputs[0]
    if output_data.ndim == 4:
        if output_data.shape[1] in (1, 3):
            output_data = np.transpose(output_data[0], (1, 2, 0))
        else:
            output_data = output_data[0]
    output_data = np.squeeze(output_data)
    if output_data.ndim == 2:
        colorized = np.stack([output_data] * 3, axis=-1)
    elif output_data.shape[-1] == 3:
        colorized = output_data
    elif output_data.shape[-1] == 2:
        pass
    else:
        colorized = output_data[..., :3]
    if output_data.ndim == 3 and output_data.shape[-1] == 3:
        out_a = rgb_to_lab_a(colorized)
        out_b = rgb_to_lab_b(colorized)
    elif output_data.ndim == 3 and output_data.shape[-1] == 2:
        out_a = output_data[..., 0]
        out_b = output_data[..., 1]
    else:
        if colorized.max() <= 1.0:
            colorized = (colorized * 255).astype(np.uint8)
        result = Image.fromarray(colorized).resize((orig_w, orig_h), Image.BILINEAR)
        result.save(output_path)
        return
    out_a_pil = Image.fromarray(out_a.astype(np.float32#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    L = 116.0 * fy - 16.0
    return L


def rgb_to_lab_a(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    return 500.0 * (fx - fy)


def rgb_to_lab_b(rgb):
    rgb_f = rgb.astype(np.float32)
    return 116.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    return 200.0 * (fy - fz)


def lab_to_rgb(L, a, b):
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
    b = 0.0556434 * X - 0.2040259 * Y + 1.0572252 * Z
    rgb = np.stack([r, g, b], axis=-1)
    rgb = np.clip(rgb, 0, 1)
    mask = rgb <= 0.0031308
    rgb_srgb = np.where(mask, 12.92 * rgb, 1.055 * np.power(np.maximum(rgb, 1e-12), 1.0 / 2.4) - 0.055)
    rgb_srgb = np.clip(rgb_srgb * 255.0, 0, 255).astype(np.uint8)
    return rgb_srgb


def colorize_image_reuse(session, input_name, input_shape, input_path, output_path):
    original = Image.open(input_path).convert('RGB')
    orig_w, orig_h = original.size
    original_np = np.array(original)
    orig_L = rgb_to_lab_l(original_np)
    gray = original.convert('L')
    gray_resized = gray.resize((INFERENCE_SIZE, INFERENCE_SIZE), Image.BILINEAR)
    input_data = np.array(gray_resized, dtype=np.float32) / 255.0
    if len(input_shape) == 4 and input_shape[1] == 3:
        input_data = np.stack([input_data] * 3, axis=0)[np.newaxis, :, :, :]
    else:
        input_data = input_data[np.newaxis, np.newaxis, :, :]
    outputs = session.run(None, {input_name: input_data})
    output_data = outputs[0]
    if output_data.ndim == 4:
        if output_data.shape[1] in (1, 3):
            output_data = np.transpose(output_data[0], (1, 2, 0))
        else:
            output_data = output_data[0]
    output_data = np.squeeze(output_data)
    if output_data.ndim == 2:
        colorized = np.stack([output_data] * 3, axis=-1)
    elif output_data.shape[-1] == 3:
        colorized = output_data
    elif output_data.shape[-1] == 2:
        pass
    else:
        colorized = output_data[..., :3]
    if output_data.ndim == 3 and output_data.shape[-1] == 3:
        out_a = rgb_to_lab_a(colorized)
        out_b = rgb_to_lab_b(colorized)
    elif output_data.ndim == 3 and output_data.shape[-1] == 2:
        out_a = output_data[..., 0]
        out_b = output_data[..., 1]
    else:
        if colorized.max() <= 1.0:
            colorized = (colorized * 255).astype(np.uint8)
        result = Image.fromarray(colorized).resize((orig_w, orig_h), Image.BILINEAR)
        result.save(output_path)
        return
    out_a_pil = Image.fromarray(out_a.astype(np.float32), mode='F')
    out_b_pil = Image.fromarray(out_b.astype(np#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    L = 116.0 * fy - 16.0
    return L


def rgb_to_lab_a(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    return 500.0 * (fx - fy)


def rgb_to_lab_b(rgb):
    rgb_f = rgb.astype(np.float32)
    return 116.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    return 200.0 * (fy - fz)


def lab_to_rgb(L, a, b):
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
    b = 0.0556434 * X - 0.2040259 * Y + 1.0572252 * Z
    rgb = np.stack([r, g, b], axis=-1)
    rgb = np.clip(rgb, 0, 1)
    mask = rgb <= 0.0031308
    rgb_srgb = np.where(mask, 12.92 * rgb, 1.055 * np.power(np.maximum(rgb, 1e-12), 1.0 / 2.4) - 0.055)
    rgb_srgb = np.clip(rgb_srgb * 255.0, 0, 255).astype(np.uint8)
    return rgb_srgb


def colorize_image_reuse(session, input_name, input_shape, input_path, output_path):
    original = Image.open(input_path).convert('RGB')
    orig_w, orig_h = original.size
    original_np = np.array(original)
    orig_L = rgb_to_lab_l(original_np)
    gray = original.convert('L')
    gray_resized = gray.resize((INFERENCE_SIZE, INFERENCE_SIZE), Image.BILINEAR)
    input_data = np.array(gray_resized, dtype=np.float32) / 255.0
    if len(input_shape) == 4 and input_shape[1] == 3:
        input_data = np.stack([input_data] * 3, axis=0)[np.newaxis, :, :, :]
    else:
        input_data = input_data[np.newaxis, np.newaxis, :, :]
    outputs = session.run(None, {input_name: input_data})
    output_data = outputs[0]
    if output_data.ndim == 4:
        if output_data.shape[1] in (1, 3):
            output_data = np.transpose(output_data[0], (1, 2, 0))
        else:
            output_data = output_data[0]
    output_data = np.squeeze(output_data)
    if output_data.ndim == 2:
        colorized = np.stack([output_data] * 3, axis=-1)
    elif output_data.shape[-1] == 3:
        colorized = output_data
    elif output_data.shape[-1] == 2:
        pass
    else:
        colorized = output_data[..., :3]
    if output_data.ndim == 3 and output_data.shape[-1] == 3:
        out_a = rgb_to_lab_a(colorized)
        out_b = rgb_to_lab_b(colorized)
    elif output_data.ndim == 3 and output_data.shape[-1] == 2:
        out_a = output_data[..., 0]
        out_b = output_data[..., 1]
    else:
        if colorized.max() <= 1.0:
            colorized = (colorized * 255).astype(np.uint8)
        result = Image.fromarray(colorized).resize((orig_w, orig_h), Image.BILINEAR)
        result.save(output_path)
        return
    out_a_pil = Image.fromarray(out_a.astype(np.float32), mode='F')
    out_b_pil = Image.fromarray(out_b.astype(np.float32), mode='F')
    out_a_resized = out_a_pil.resize#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    L = 116.0 * fy - 16.0
    return L


def rgb_to_lab_a(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    return 500.0 * (fx - fy)


def rgb_to_lab_b(rgb):
    rgb_f = rgb.astype(np.float32)
    return 116.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    return 200.0 * (fy - fz)


def lab_to_rgb(L, a, b):
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
    b = 0.0556434 * X - 0.2040259 * Y + 1.0572252 * Z
    rgb = np.stack([r, g, b], axis=-1)
    rgb = np.clip(rgb, 0, 1)
    mask = rgb <= 0.0031308
    rgb_srgb = np.where(mask, 12.92 * rgb, 1.055 * np.power(np.maximum(rgb, 1e-12), 1.0 / 2.4) - 0.055)
    rgb_srgb = np.clip(rgb_srgb * 255.0, 0, 255).astype(np.uint8)
    return rgb_srgb


def colorize_image_reuse(session, input_name, input_shape, input_path, output_path):
    original = Image.open(input_path).convert('RGB')
    orig_w, orig_h = original.size
    original_np = np.array(original)
    orig_L = rgb_to_lab_l(original_np)
    gray = original.convert('L')
    gray_resized = gray.resize((INFERENCE_SIZE, INFERENCE_SIZE), Image.BILINEAR)
    input_data = np.array(gray_resized, dtype=np.float32) / 255.0
    if len(input_shape) == 4 and input_shape[1] == 3:
        input_data = np.stack([input_data] * 3, axis=0)[np.newaxis, :, :, :]
    else:
        input_data = input_data[np.newaxis, np.newaxis, :, :]
    outputs = session.run(None, {input_name: input_data})
    output_data = outputs[0]
    if output_data.ndim == 4:
        if output_data.shape[1] in (1, 3):
            output_data = np.transpose(output_data[0], (1, 2, 0))
        else:
            output_data = output_data[0]
    output_data = np.squeeze(output_data)
    if output_data.ndim == 2:
        colorized = np.stack([output_data] * 3, axis=-1)
    elif output_data.shape[-1] == 3:
        colorized = output_data
    elif output_data.shape[-1] == 2:
        pass
    else:
        colorized = output_data[..., :3]
    if output_data.ndim == 3 and output_data.shape[-1] == 3:
        out_a = rgb_to_lab_a(colorized)
        out_b = rgb_to_lab_b(colorized)
    elif output_data.ndim == 3 and output_data.shape[-1] == 2:
        out_a = output_data[..., 0]
        out_b = output_data[..., 1]
    else:
        if colorized.max() <= 1.0:
            colorized = (colorized * 255).astype(np.uint8)
        result = Image.fromarray(colorized).resize((orig_w, orig_h), Image.BILINEAR)
        result.save(output_path)
        return
    out_a_pil = Image.fromarray(out_a.astype(np.float32), mode='F')
    out_b_pil = Image.fromarray(out_b.astype(np.float32), mode='F')
    out_a_resized = out_a_pil.resize((orig_w, orig_h), Image.BIL#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    L = 116.0 * fy - 16.0
    return L


def rgb_to_lab_a(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    return 500.0 * (fx - fy)


def rgb_to_lab_b(rgb):
    rgb_f = rgb.astype(np.float32)
    return 116.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    return 200.0 * (fy - fz)


def lab_to_rgb(L, a, b):
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
    b = 0.0556434 * X - 0.2040259 * Y + 1.0572252 * Z
    rgb = np.stack([r, g, b], axis=-1)
    rgb = np.clip(rgb, 0, 1)
    mask = rgb <= 0.0031308
    rgb_srgb = np.where(mask, 12.92 * rgb, 1.055 * np.power(np.maximum(rgb, 1e-12), 1.0 / 2.4) - 0.055)
    rgb_srgb = np.clip(rgb_srgb * 255.0, 0, 255).astype(np.uint8)
    return rgb_srgb


def colorize_image_reuse(session, input_name, input_shape, input_path, output_path):
    original = Image.open(input_path).convert('RGB')
    orig_w, orig_h = original.size
    original_np = np.array(original)
    orig_L = rgb_to_lab_l(original_np)
    gray = original.convert('L')
    gray_resized = gray.resize((INFERENCE_SIZE, INFERENCE_SIZE), Image.BILINEAR)
    input_data = np.array(gray_resized, dtype=np.float32) / 255.0
    if len(input_shape) == 4 and input_shape[1] == 3:
        input_data = np.stack([input_data] * 3, axis=0)[np.newaxis, :, :, :]
    else:
        input_data = input_data[np.newaxis, np.newaxis, :, :]
    outputs = session.run(None, {input_name: input_data})
    output_data = outputs[0]
    if output_data.ndim == 4:
        if output_data.shape[1] in (1, 3):
            output_data = np.transpose(output_data[0], (1, 2, 0))
        else:
            output_data = output_data[0]
    output_data = np.squeeze(output_data)
    if output_data.ndim == 2:
        colorized = np.stack([output_data] * 3, axis=-1)
    elif output_data.shape[-1] == 3:
        colorized = output_data
    elif output_data.shape[-1] == 2:
        pass
    else:
        colorized = output_data[..., :3]
    if output_data.ndim == 3 and output_data.shape[-1] == 3:
        out_a = rgb_to_lab_a(colorized)
        out_b = rgb_to_lab_b(colorized)
    elif output_data.ndim == 3 and output_data.shape[-1] == 2:
        out_a = output_data[..., 0]
        out_b = output_data[..., 1]
    else:
        if colorized.max() <= 1.0:
            colorized = (colorized * 255).astype(np.uint8)
        result = Image.fromarray(colorized).resize((orig_w, orig_h), Image.BILINEAR)
        result.save(output_path)
        return
    out_a_pil = Image.fromarray(out_a.astype(np.float32), mode='F')
    out_b_pil = Image.fromarray(out_b.astype(np.float32), mode='F')
    out_a_resized = out_a_pil.resize((orig_w, orig_h), Image.BILINEAR)
    out_b_resized =#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    L = 116.0 * fy - 16.0
    return L


def rgb_to_lab_a(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    return 500.0 * (fx - fy)


def rgb_to_lab_b(rgb):
    rgb_f = rgb.astype(np.float32)
    return 116.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    return 200.0 * (fy - fz)


def lab_to_rgb(L, a, b):
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
    b = 0.0556434 * X - 0.2040259 * Y + 1.0572252 * Z
    rgb = np.stack([r, g, b], axis=-1)
    rgb = np.clip(rgb, 0, 1)
    mask = rgb <= 0.0031308
    rgb_srgb = np.where(mask, 12.92 * rgb, 1.055 * np.power(np.maximum(rgb, 1e-12), 1.0 / 2.4) - 0.055)
    rgb_srgb = np.clip(rgb_srgb * 255.0, 0, 255).astype(np.uint8)
    return rgb_srgb


def colorize_image_reuse(session, input_name, input_shape, input_path, output_path):
    original = Image.open(input_path).convert('RGB')
    orig_w, orig_h = original.size
    original_np = np.array(original)
    orig_L = rgb_to_lab_l(original_np)
    gray = original.convert('L')
    gray_resized = gray.resize((INFERENCE_SIZE, INFERENCE_SIZE), Image.BILINEAR)
    input_data = np.array(gray_resized, dtype=np.float32) / 255.0
    if len(input_shape) == 4 and input_shape[1] == 3:
        input_data = np.stack([input_data] * 3, axis=0)[np.newaxis, :, :, :]
    else:
        input_data = input_data[np.newaxis, np.newaxis, :, :]
    outputs = session.run(None, {input_name: input_data})
    output_data = outputs[0]
    if output_data.ndim == 4:
        if output_data.shape[1] in (1, 3):
            output_data = np.transpose(output_data[0], (1, 2, 0))
        else:
            output_data = output_data[0]
    output_data = np.squeeze(output_data)
    if output_data.ndim == 2:
        colorized = np.stack([output_data] * 3, axis=-1)
    elif output_data.shape[-1] == 3:
        colorized = output_data
    elif output_data.shape[-1] == 2:
        pass
    else:
        colorized = output_data[..., :3]
    if output_data.ndim == 3 and output_data.shape[-1] == 3:
        out_a = rgb_to_lab_a(colorized)
        out_b = rgb_to_lab_b(colorized)
    elif output_data.ndim == 3 and output_data.shape[-1] == 2:
        out_a = output_data[..., 0]
        out_b = output_data[..., 1]
    else:
        if colorized.max() <= 1.0:
            colorized = (colorized * 255).astype(np.uint8)
        result = Image.fromarray(colorized).resize((orig_w, orig_h), Image.BILINEAR)
        result.save(output_path)
        return
    out_a_pil = Image.fromarray(out_a.astype(np.float32), mode='F')
    out_b_pil = Image.fromarray(out_b.astype(np.float32), mode='F')
    out_a_resized = out_a_pil.resize((orig_w, orig_h), Image.BILINEAR)
    out_b_resized = out_b_pil.resize((orig_w, orig_h), Image.BILINEAR)
#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    L = 116.0 * fy - 16.0
    return L


def rgb_to_lab_a(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    return 500.0 * (fx - fy)


def rgb_to_lab_b(rgb):
    rgb_f = rgb.astype(np.float32)
    return 116.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    return 200.0 * (fy - fz)


def lab_to_rgb(L, a, b):
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
    b = 0.0556434 * X - 0.2040259 * Y + 1.0572252 * Z
    rgb = np.stack([r, g, b], axis=-1)
    rgb = np.clip(rgb, 0, 1)
    mask = rgb <= 0.0031308
    rgb_srgb = np.where(mask, 12.92 * rgb, 1.055 * np.power(np.maximum(rgb, 1e-12), 1.0 / 2.4) - 0.055)
    rgb_srgb = np.clip(rgb_srgb * 255.0, 0, 255).astype(np.uint8)
    return rgb_srgb


def colorize_image_reuse(session, input_name, input_shape, input_path, output_path):
    original = Image.open(input_path).convert('RGB')
    orig_w, orig_h = original.size
    original_np = np.array(original)
    orig_L = rgb_to_lab_l(original_np)
    gray = original.convert('L')
    gray_resized = gray.resize((INFERENCE_SIZE, INFERENCE_SIZE), Image.BILINEAR)
    input_data = np.array(gray_resized, dtype=np.float32) / 255.0
    if len(input_shape) == 4 and input_shape[1] == 3:
        input_data = np.stack([input_data] * 3, axis=0)[np.newaxis, :, :, :]
    else:
        input_data = input_data[np.newaxis, np.newaxis, :, :]
    outputs = session.run(None, {input_name: input_data})
    output_data = outputs[0]
    if output_data.ndim == 4:
        if output_data.shape[1] in (1, 3):
            output_data = np.transpose(output_data[0], (1, 2, 0))
        else:
            output_data = output_data[0]
    output_data = np.squeeze(output_data)
    if output_data.ndim == 2:
        colorized = np.stack([output_data] * 3, axis=-1)
    elif output_data.shape[-1] == 3:
        colorized = output_data
    elif output_data.shape[-1] == 2:
        pass
    else:
        colorized = output_data[..., :3]
    if output_data.ndim == 3 and output_data.shape[-1] == 3:
        out_a = rgb_to_lab_a(colorized)
        out_b = rgb_to_lab_b(colorized)
    elif output_data.ndim == 3 and output_data.shape[-1] == 2:
        out_a = output_data[..., 0]
        out_b = output_data[..., 1]
    else:
        if colorized.max() <= 1.0:
            colorized = (colorized * 255).astype(np.uint8)
        result = Image.fromarray(colorized).resize((orig_w, orig_h), Image.BILINEAR)
        result.save(output_path)
        return
    out_a_pil = Image.fromarray(out_a.astype(np.float32), mode='F')
    out_b_pil = Image.fromarray(out_b.astype(np.float32), mode='F')
    out_a_resized = out_a_pil.resize((orig_w, orig_h), Image.BILINEAR)
    out_b_resized = out_b_pil.resize((orig_w, orig_h), Image.BILINEAR)
    out_a_arr = np.array(out_a_resized#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    L = 116.0 * fy - 16.0
    return L


def rgb_to_lab_a(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    return 500.0 * (fx - fy)


def rgb_to_lab_b(rgb):
    rgb_f = rgb.astype(np.float32)
    return 116.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    return 200.0 * (fy - fz)


def lab_to_rgb(L, a, b):
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
    b = 0.0556434 * X - 0.2040259 * Y + 1.0572252 * Z
    rgb = np.stack([r, g, b], axis=-1)
    rgb = np.clip(rgb, 0, 1)
    mask = rgb <= 0.0031308
    rgb_srgb = np.where(mask, 12.92 * rgb, 1.055 * np.power(np.maximum(rgb, 1e-12), 1.0 / 2.4) - 0.055)
    rgb_srgb = np.clip(rgb_srgb * 255.0, 0, 255).astype(np.uint8)
    return rgb_srgb


def colorize_image_reuse(session, input_name, input_shape, input_path, output_path):
    original = Image.open(input_path).convert('RGB')
    orig_w, orig_h = original.size
    original_np = np.array(original)
    orig_L = rgb_to_lab_l(original_np)
    gray = original.convert('L')
    gray_resized = gray.resize((INFERENCE_SIZE, INFERENCE_SIZE), Image.BILINEAR)
    input_data = np.array(gray_resized, dtype=np.float32) / 255.0
    if len(input_shape) == 4 and input_shape[1] == 3:
        input_data = np.stack([input_data] * 3, axis=0)[np.newaxis, :, :, :]
    else:
        input_data = input_data[np.newaxis, np.newaxis, :, :]
    outputs = session.run(None, {input_name: input_data})
    output_data = outputs[0]
    if output_data.ndim == 4:
        if output_data.shape[1] in (1, 3):
            output_data = np.transpose(output_data[0], (1, 2, 0))
        else:
            output_data = output_data[0]
    output_data = np.squeeze(output_data)
    if output_data.ndim == 2:
        colorized = np.stack([output_data] * 3, axis=-1)
    elif output_data.shape[-1] == 3:
        colorized = output_data
    elif output_data.shape[-1] == 2:
        pass
    else:
        colorized = output_data[..., :3]
    if output_data.ndim == 3 and output_data.shape[-1] == 3:
        out_a = rgb_to_lab_a(colorized)
        out_b = rgb_to_lab_b(colorized)
    elif output_data.ndim == 3 and output_data.shape[-1] == 2:
        out_a = output_data[..., 0]
        out_b = output_data[..., 1]
    else:
        if colorized.max() <= 1.0:
            colorized = (colorized * 255).astype(np.uint8)
        result = Image.fromarray(colorized).resize((orig_w, orig_h), Image.BILINEAR)
        result.save(output_path)
        return
    out_a_pil = Image.fromarray(out_a.astype(np.float32), mode='F')
    out_b_pil = Image.fromarray(out_b.astype(np.float32), mode='F')
    out_a_resized = out_a_pil.resize((orig_w, orig_h), Image.BILINEAR)
    out_b_resized = out_b_pil.resize((orig_w, orig_h), Image.BILINEAR)
    out_a_arr = np.array(out_a_resized)
    out_b_arr = np.array(out#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    L = 116.0 * fy - 16.0
    return L


def rgb_to_lab_a(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    return 500.0 * (fx - fy)


def rgb_to_lab_b(rgb):
    rgb_f = rgb.astype(np.float32)
    return 116.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    return 200.0 * (fy - fz)


def lab_to_rgb(L, a, b):
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
    b = 0.0556434 * X - 0.2040259 * Y + 1.0572252 * Z
    rgb = np.stack([r, g, b], axis=-1)
    rgb = np.clip(rgb, 0, 1)
    mask = rgb <= 0.0031308
    rgb_srgb = np.where(mask, 12.92 * rgb, 1.055 * np.power(np.maximum(rgb, 1e-12), 1.0 / 2.4) - 0.055)
    rgb_srgb = np.clip(rgb_srgb * 255.0, 0, 255).astype(np.uint8)
    return rgb_srgb


def colorize_image_reuse(session, input_name, input_shape, input_path, output_path):
    original = Image.open(input_path).convert('RGB')
    orig_w, orig_h = original.size
    original_np = np.array(original)
    orig_L = rgb_to_lab_l(original_np)
    gray = original.convert('L')
    gray_resized = gray.resize((INFERENCE_SIZE, INFERENCE_SIZE), Image.BILINEAR)
    input_data = np.array(gray_resized, dtype=np.float32) / 255.0
    if len(input_shape) == 4 and input_shape[1] == 3:
        input_data = np.stack([input_data] * 3, axis=0)[np.newaxis, :, :, :]
    else:
        input_data = input_data[np.newaxis, np.newaxis, :, :]
    outputs = session.run(None, {input_name: input_data})
    output_data = outputs[0]
    if output_data.ndim == 4:
        if output_data.shape[1] in (1, 3):
            output_data = np.transpose(output_data[0], (1, 2, 0))
        else:
            output_data = output_data[0]
    output_data = np.squeeze(output_data)
    if output_data.ndim == 2:
        colorized = np.stack([output_data] * 3, axis=-1)
    elif output_data.shape[-1] == 3:
        colorized = output_data
    elif output_data.shape[-1] == 2:
        pass
    else:
        colorized = output_data[..., :3]
    if output_data.ndim == 3 and output_data.shape[-1] == 3:
        out_a = rgb_to_lab_a(colorized)
        out_b = rgb_to_lab_b(colorized)
    elif output_data.ndim == 3 and output_data.shape[-1] == 2:
        out_a = output_data[..., 0]
        out_b = output_data[..., 1]
    else:
        if colorized.max() <= 1.0:
            colorized = (colorized * 255).astype(np.uint8)
        result = Image.fromarray(colorized).resize((orig_w, orig_h), Image.BILINEAR)
        result.save(output_path)
        return
    out_a_pil = Image.fromarray(out_a.astype(np.float32), mode='F')
    out_b_pil = Image.fromarray(out_b.astype(np.float32), mode='F')
    out_a_resized = out_a_pil.resize((orig_w, orig_h), Image.BILINEAR)
    out_b_resized = out_b_pil.resize((orig_w, orig_h), Image.BILINEAR)
    out_a_arr = np.array(out_a_resized)
    out_b_arr = np.array(out_b_resized)
    result_rgb = lab_to_rgb(orig_L, out_a#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    L = 116.0 * fy - 16.0
    return L


def rgb_to_lab_a(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    return 500.0 * (fx - fy)


def rgb_to_lab_b(rgb):
    rgb_f = rgb.astype(np.float32)
    return 116.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    return 200.0 * (fy - fz)


def lab_to_rgb(L, a, b):
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
    b = 0.0556434 * X - 0.2040259 * Y + 1.0572252 * Z
    rgb = np.stack([r, g, b], axis=-1)
    rgb = np.clip(rgb, 0, 1)
    mask = rgb <= 0.0031308
    rgb_srgb = np.where(mask, 12.92 * rgb, 1.055 * np.power(np.maximum(rgb, 1e-12), 1.0 / 2.4) - 0.055)
    rgb_srgb = np.clip(rgb_srgb * 255.0, 0, 255).astype(np.uint8)
    return rgb_srgb


def colorize_image_reuse(session, input_name, input_shape, input_path, output_path):
    original = Image.open(input_path).convert('RGB')
    orig_w, orig_h = original.size
    original_np = np.array(original)
    orig_L = rgb_to_lab_l(original_np)
    gray = original.convert('L')
    gray_resized = gray.resize((INFERENCE_SIZE, INFERENCE_SIZE), Image.BILINEAR)
    input_data = np.array(gray_resized, dtype=np.float32) / 255.0
    if len(input_shape) == 4 and input_shape[1] == 3:
        input_data = np.stack([input_data] * 3, axis=0)[np.newaxis, :, :, :]
    else:
        input_data = input_data[np.newaxis, np.newaxis, :, :]
    outputs = session.run(None, {input_name: input_data})
    output_data = outputs[0]
    if output_data.ndim == 4:
        if output_data.shape[1] in (1, 3):
            output_data = np.transpose(output_data[0], (1, 2, 0))
        else:
            output_data = output_data[0]
    output_data = np.squeeze(output_data)
    if output_data.ndim == 2:
        colorized = np.stack([output_data] * 3, axis=-1)
    elif output_data.shape[-1] == 3:
        colorized = output_data
    elif output_data.shape[-1] == 2:
        pass
    else:
        colorized = output_data[..., :3]
    if output_data.ndim == 3 and output_data.shape[-1] == 3:
        out_a = rgb_to_lab_a(colorized)
        out_b = rgb_to_lab_b(colorized)
    elif output_data.ndim == 3 and output_data.shape[-1] == 2:
        out_a = output_data[..., 0]
        out_b = output_data[..., 1]
    else:
        if colorized.max() <= 1.0:
            colorized = (colorized * 255).astype(np.uint8)
        result = Image.fromarray(colorized).resize((orig_w, orig_h), Image.BILINEAR)
        result.save(output_path)
        return
    out_a_pil = Image.fromarray(out_a.astype(np.float32), mode='F')
    out_b_pil = Image.fromarray(out_b.astype(np.float32), mode='F')
    out_a_resized = out_a_pil.resize((orig_w, orig_h), Image.BILINEAR)
    out_b_resized = out_b_pil.resize((orig_w, orig_h), Image.BILINEAR)
    out_a_arr = np.array(out_a_resized)
    out_b_arr = np.array(out_b_resized)
    result_rgb = lab_to_rgb(orig_L, out_a_arr, out_b_arr)
    result = Image.fromarray(result_rgb)
    result#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    L = 116.0 * fy - 16.0
    return L


def rgb_to_lab_a(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    return 500.0 * (fx - fy)


def rgb_to_lab_b(rgb):
    rgb_f = rgb.astype(np.float32)
    return 116.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    return 200.0 * (fy - fz)


def lab_to_rgb(L, a, b):
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
    b = 0.0556434 * X - 0.2040259 * Y + 1.0572252 * Z
    rgb = np.stack([r, g, b], axis=-1)
    rgb = np.clip(rgb, 0, 1)
    mask = rgb <= 0.0031308
    rgb_srgb = np.where(mask, 12.92 * rgb, 1.055 * np.power(np.maximum(rgb, 1e-12), 1.0 / 2.4) - 0.055)
    rgb_srgb = np.clip(rgb_srgb * 255.0, 0, 255).astype(np.uint8)
    return rgb_srgb


def colorize_image_reuse(session, input_name, input_shape, input_path, output_path):
    original = Image.open(input_path).convert('RGB')
    orig_w, orig_h = original.size
    original_np = np.array(original)
    orig_L = rgb_to_lab_l(original_np)
    gray = original.convert('L')
    gray_resized = gray.resize((INFERENCE_SIZE, INFERENCE_SIZE), Image.BILINEAR)
    input_data = np.array(gray_resized, dtype=np.float32) / 255.0
    if len(input_shape) == 4 and input_shape[1] == 3:
        input_data = np.stack([input_data] * 3, axis=0)[np.newaxis, :, :, :]
    else:
        input_data = input_data[np.newaxis, np.newaxis, :, :]
    outputs = session.run(None, {input_name: input_data})
    output_data = outputs[0]
    if output_data.ndim == 4:
        if output_data.shape[1] in (1, 3):
            output_data = np.transpose(output_data[0], (1, 2, 0))
        else:
            output_data = output_data[0]
    output_data = np.squeeze(output_data)
    if output_data.ndim == 2:
        colorized = np.stack([output_data] * 3, axis=-1)
    elif output_data.shape[-1] == 3:
        colorized = output_data
    elif output_data.shape[-1] == 2:
        pass
    else:
        colorized = output_data[..., :3]
    if output_data.ndim == 3 and output_data.shape[-1] == 3:
        out_a = rgb_to_lab_a(colorized)
        out_b = rgb_to_lab_b(colorized)
    elif output_data.ndim == 3 and output_data.shape[-1] == 2:
        out_a = output_data[..., 0]
        out_b = output_data[..., 1]
    else:
        if colorized.max() <= 1.0:
            colorized = (colorized * 255).astype(np.uint8)
        result = Image.fromarray(colorized).resize((orig_w, orig_h), Image.BILINEAR)
        result.save(output_path)
        return
    out_a_pil = Image.fromarray(out_a.astype(np.float32), mode='F')
    out_b_pil = Image.fromarray(out_b.astype(np.float32), mode='F')
    out_a_resized = out_a_pil.resize((orig_w, orig_h), Image.BILINEAR)
    out_b_resized = out_b_pil.resize((orig_w, orig_h), Image.BILINEAR)
    out_a_arr = np.array(out_a_resized)
    out_b_arr = np.array(out_b_resized)
    result_rgb = lab_to_rgb(orig_L, out_a_arr, out_b_arr)
    result = Image.fromarray(result_rgb)
    result.save(output_path)


def test_cli_mode(images):
    print("\n===#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    L = 116.0 * fy - 16.0
    return L


def rgb_to_lab_a(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    return 500.0 * (fx - fy)


def rgb_to_lab_b(rgb):
    rgb_f = rgb.astype(np.float32)
    return 116.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    return 200.0 * (fy - fz)


def lab_to_rgb(L, a, b):
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
    b = 0.0556434 * X - 0.2040259 * Y + 1.0572252 * Z
    rgb = np.stack([r, g, b], axis=-1)
    rgb = np.clip(rgb, 0, 1)
    mask = rgb <= 0.0031308
    rgb_srgb = np.where(mask, 12.92 * rgb, 1.055 * np.power(np.maximum(rgb, 1e-12), 1.0 / 2.4) - 0.055)
    rgb_srgb = np.clip(rgb_srgb * 255.0, 0, 255).astype(np.uint8)
    return rgb_srgb


def colorize_image_reuse(session, input_name, input_shape, input_path, output_path):
    original = Image.open(input_path).convert('RGB')
    orig_w, orig_h = original.size
    original_np = np.array(original)
    orig_L = rgb_to_lab_l(original_np)
    gray = original.convert('L')
    gray_resized = gray.resize((INFERENCE_SIZE, INFERENCE_SIZE), Image.BILINEAR)
    input_data = np.array(gray_resized, dtype=np.float32) / 255.0
    if len(input_shape) == 4 and input_shape[1] == 3:
        input_data = np.stack([input_data] * 3, axis=0)[np.newaxis, :, :, :]
    else:
        input_data = input_data[np.newaxis, np.newaxis, :, :]
    outputs = session.run(None, {input_name: input_data})
    output_data = outputs[0]
    if output_data.ndim == 4:
        if output_data.shape[1] in (1, 3):
            output_data = np.transpose(output_data[0], (1, 2, 0))
        else:
            output_data = output_data[0]
    output_data = np.squeeze(output_data)
    if output_data.ndim == 2:
        colorized = np.stack([output_data] * 3, axis=-1)
    elif output_data.shape[-1] == 3:
        colorized = output_data
    elif output_data.shape[-1] == 2:
        pass
    else:
        colorized = output_data[..., :3]
    if output_data.ndim == 3 and output_data.shape[-1] == 3:
        out_a = rgb_to_lab_a(colorized)
        out_b = rgb_to_lab_b(colorized)
    elif output_data.ndim == 3 and output_data.shape[-1] == 2:
        out_a = output_data[..., 0]
        out_b = output_data[..., 1]
    else:
        if colorized.max() <= 1.0:
            colorized = (colorized * 255).astype(np.uint8)
        result = Image.fromarray(colorized).resize((orig_w, orig_h), Image.BILINEAR)
        result.save(output_path)
        return
    out_a_pil = Image.fromarray(out_a.astype(np.float32), mode='F')
    out_b_pil = Image.fromarray(out_b.astype(np.float32), mode='F')
    out_a_resized = out_a_pil.resize((orig_w, orig_h), Image.BILINEAR)
    out_b_resized = out_b_pil.resize((orig_w, orig_h), Image.BILINEAR)
    out_a_arr = np.array(out_a_resized)
    out_b_arr = np.array(out_b_resized)
    result_rgb = lab_to_rgb(orig_L, out_a_arr, out_b_arr)
    result = Image.fromarray(result_rgb)
    result.save(output_path)


def test_cli_mode(images):
    print("\n=== 方式1: CLI 调用（每次子进程，每次重新加载模型）===")
#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    L = 116.0 * fy - 16.0
    return L


def rgb_to_lab_a(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    return 500.0 * (fx - fy)


def rgb_to_lab_b(rgb):
    rgb_f = rgb.astype(np.float32)
    return 116.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    return 200.0 * (fy - fz)


def lab_to_rgb(L, a, b):
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
    b = 0.0556434 * X - 0.2040259 * Y + 1.0572252 * Z
    rgb = np.stack([r, g, b], axis=-1)
    rgb = np.clip(rgb, 0, 1)
    mask = rgb <= 0.0031308
    rgb_srgb = np.where(mask, 12.92 * rgb, 1.055 * np.power(np.maximum(rgb, 1e-12), 1.0 / 2.4) - 0.055)
    rgb_srgb = np.clip(rgb_srgb * 255.0, 0, 255).astype(np.uint8)
    return rgb_srgb


def colorize_image_reuse(session, input_name, input_shape, input_path, output_path):
    original = Image.open(input_path).convert('RGB')
    orig_w, orig_h = original.size
    original_np = np.array(original)
    orig_L = rgb_to_lab_l(original_np)
    gray = original.convert('L')
    gray_resized = gray.resize((INFERENCE_SIZE, INFERENCE_SIZE), Image.BILINEAR)
    input_data = np.array(gray_resized, dtype=np.float32) / 255.0
    if len(input_shape) == 4 and input_shape[1] == 3:
        input_data = np.stack([input_data] * 3, axis=0)[np.newaxis, :, :, :]
    else:
        input_data = input_data[np.newaxis, np.newaxis, :, :]
    outputs = session.run(None, {input_name: input_data})
    output_data = outputs[0]
    if output_data.ndim == 4:
        if output_data.shape[1] in (1, 3):
            output_data = np.transpose(output_data[0], (1, 2, 0))
        else:
            output_data = output_data[0]
    output_data = np.squeeze(output_data)
    if output_data.ndim == 2:
        colorized = np.stack([output_data] * 3, axis=-1)
    elif output_data.shape[-1] == 3:
        colorized = output_data
    elif output_data.shape[-1] == 2:
        pass
    else:
        colorized = output_data[..., :3]
    if output_data.ndim == 3 and output_data.shape[-1] == 3:
        out_a = rgb_to_lab_a(colorized)
        out_b = rgb_to_lab_b(colorized)
    elif output_data.ndim == 3 and output_data.shape[-1] == 2:
        out_a = output_data[..., 0]
        out_b = output_data[..., 1]
    else:
        if colorized.max() <= 1.0:
            colorized = (colorized * 255).astype(np.uint8)
        result = Image.fromarray(colorized).resize((orig_w, orig_h), Image.BILINEAR)
        result.save(output_path)
        return
    out_a_pil = Image.fromarray(out_a.astype(np.float32), mode='F')
    out_b_pil = Image.fromarray(out_b.astype(np.float32), mode='F')
    out_a_resized = out_a_pil.resize((orig_w, orig_h), Image.BILINEAR)
    out_b_resized = out_b_pil.resize((orig_w, orig_h), Image.BILINEAR)
    out_a_arr = np.array(out_a_resized)
    out_b_arr = np.array(out_b_resized)
    result_rgb = lab_to_rgb(orig_L, out_a_arr, out_b_arr)
    result = Image.fromarray(result_rgb)
    result.save(output_path)


def test_cli_mode(images):
    print("\n=== 方式1: CLI 调用（每次子进程，每次重新加载模型）===")
    print(f"图片数量: {len(images)}")
    os.makedirs(#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    L = 116.0 * fy - 16.0
    return L


def rgb_to_lab_a(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    return 500.0 * (fx - fy)


def rgb_to_lab_b(rgb):
    rgb_f = rgb.astype(np.float32)
    return 116.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    return 200.0 * (fy - fz)


def lab_to_rgb(L, a, b):
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
    b = 0.0556434 * X - 0.2040259 * Y + 1.0572252 * Z
    rgb = np.stack([r, g, b], axis=-1)
    rgb = np.clip(rgb, 0, 1)
    mask = rgb <= 0.0031308
    rgb_srgb = np.where(mask, 12.92 * rgb, 1.055 * np.power(np.maximum(rgb, 1e-12), 1.0 / 2.4) - 0.055)
    rgb_srgb = np.clip(rgb_srgb * 255.0, 0, 255).astype(np.uint8)
    return rgb_srgb


def colorize_image_reuse(session, input_name, input_shape, input_path, output_path):
    original = Image.open(input_path).convert('RGB')
    orig_w, orig_h = original.size
    original_np = np.array(original)
    orig_L = rgb_to_lab_l(original_np)
    gray = original.convert('L')
    gray_resized = gray.resize((INFERENCE_SIZE, INFERENCE_SIZE), Image.BILINEAR)
    input_data = np.array(gray_resized, dtype=np.float32) / 255.0
    if len(input_shape) == 4 and input_shape[1] == 3:
        input_data = np.stack([input_data] * 3, axis=0)[np.newaxis, :, :, :]
    else:
        input_data = input_data[np.newaxis, np.newaxis, :, :]
    outputs = session.run(None, {input_name: input_data})
    output_data = outputs[0]
    if output_data.ndim == 4:
        if output_data.shape[1] in (1, 3):
            output_data = np.transpose(output_data[0], (1, 2, 0))
        else:
            output_data = output_data[0]
    output_data = np.squeeze(output_data)
    if output_data.ndim == 2:
        colorized = np.stack([output_data] * 3, axis=-1)
    elif output_data.shape[-1] == 3:
        colorized = output_data
    elif output_data.shape[-1] == 2:
        pass
    else:
        colorized = output_data[..., :3]
    if output_data.ndim == 3 and output_data.shape[-1] == 3:
        out_a = rgb_to_lab_a(colorized)
        out_b = rgb_to_lab_b(colorized)
    elif output_data.ndim == 3 and output_data.shape[-1] == 2:
        out_a = output_data[..., 0]
        out_b = output_data[..., 1]
    else:
        if colorized.max() <= 1.0:
            colorized = (colorized * 255).astype(np.uint8)
        result = Image.fromarray(colorized).resize((orig_w, orig_h), Image.BILINEAR)
        result.save(output_path)
        return
    out_a_pil = Image.fromarray(out_a.astype(np.float32), mode='F')
    out_b_pil = Image.fromarray(out_b.astype(np.float32), mode='F')
    out_a_resized = out_a_pil.resize((orig_w, orig_h), Image.BILINEAR)
    out_b_resized = out_b_pil.resize((orig_w, orig_h), Image.BILINEAR)
    out_a_arr = np.array(out_a_resized)
    out_b_arr = np.array(out_b_resized)
    result_rgb = lab_to_rgb(orig_L, out_a_arr, out_b_arr)
    result = Image.fromarray(result_rgb)
    result.save(output_path)


def test_cli_mode(images):
    print("\n=== 方式1: CLI 调用（每次子进程，每次重新加载模型）===")
    print(f"图片数量: {len(images)}")
    os.makedirs(OUTPUT_DIR_CLI, exist_ok=True)

    per_image_times = []
    total#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    L = 116.0 * fy - 16.0
    return L


def rgb_to_lab_a(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    return 500.0 * (fx - fy)


def rgb_to_lab_b(rgb):
    rgb_f = rgb.astype(np.float32)
    return 116.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    return 200.0 * (fy - fz)


def lab_to_rgb(L, a, b):
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
    b = 0.0556434 * X - 0.2040259 * Y + 1.0572252 * Z
    rgb = np.stack([r, g, b], axis=-1)
    rgb = np.clip(rgb, 0, 1)
    mask = rgb <= 0.0031308
    rgb_srgb = np.where(mask, 12.92 * rgb, 1.055 * np.power(np.maximum(rgb, 1e-12), 1.0 / 2.4) - 0.055)
    rgb_srgb = np.clip(rgb_srgb * 255.0, 0, 255).astype(np.uint8)
    return rgb_srgb


def colorize_image_reuse(session, input_name, input_shape, input_path, output_path):
    original = Image.open(input_path).convert('RGB')
    orig_w, orig_h = original.size
    original_np = np.array(original)
    orig_L = rgb_to_lab_l(original_np)
    gray = original.convert('L')
    gray_resized = gray.resize((INFERENCE_SIZE, INFERENCE_SIZE), Image.BILINEAR)
    input_data = np.array(gray_resized, dtype=np.float32) / 255.0
    if len(input_shape) == 4 and input_shape[1] == 3:
        input_data = np.stack([input_data] * 3, axis=0)[np.newaxis, :, :, :]
    else:
        input_data = input_data[np.newaxis, np.newaxis, :, :]
    outputs = session.run(None, {input_name: input_data})
    output_data = outputs[0]
    if output_data.ndim == 4:
        if output_data.shape[1] in (1, 3):
            output_data = np.transpose(output_data[0], (1, 2, 0))
        else:
            output_data = output_data[0]
    output_data = np.squeeze(output_data)
    if output_data.ndim == 2:
        colorized = np.stack([output_data] * 3, axis=-1)
    elif output_data.shape[-1] == 3:
        colorized = output_data
    elif output_data.shape[-1] == 2:
        pass
    else:
        colorized = output_data[..., :3]
    if output_data.ndim == 3 and output_data.shape[-1] == 3:
        out_a = rgb_to_lab_a(colorized)
        out_b = rgb_to_lab_b(colorized)
    elif output_data.ndim == 3 and output_data.shape[-1] == 2:
        out_a = output_data[..., 0]
        out_b = output_data[..., 1]
    else:
        if colorized.max() <= 1.0:
            colorized = (colorized * 255).astype(np.uint8)
        result = Image.fromarray(colorized).resize((orig_w, orig_h), Image.BILINEAR)
        result.save(output_path)
        return
    out_a_pil = Image.fromarray(out_a.astype(np.float32), mode='F')
    out_b_pil = Image.fromarray(out_b.astype(np.float32), mode='F')
    out_a_resized = out_a_pil.resize((orig_w, orig_h), Image.BILINEAR)
    out_b_resized = out_b_pil.resize((orig_w, orig_h), Image.BILINEAR)
    out_a_arr = np.array(out_a_resized)
    out_b_arr = np.array(out_b_resized)
    result_rgb = lab_to_rgb(orig_L, out_a_arr, out_b_arr)
    result = Image.fromarray(result_rgb)
    result.save(output_path)


def test_cli_mode(images):
    print("\n=== 方式1: CLI 调用（每次子进程，每次重新加载模型）===")
    print(f"图片数量: {len(images)}")
    os.makedirs(OUTPUT_DIR_CLI, exist_ok=True)

    per_image_times = []
    total_start = time.time()

    for i, img_path in enumerate(images):
        out#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    L = 116.0 * fy - 16.0
    return L


def rgb_to_lab_a(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    return 500.0 * (fx - fy)


def rgb_to_lab_b(rgb):
    rgb_f = rgb.astype(np.float32)
    return 116.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    return 200.0 * (fy - fz)


def lab_to_rgb(L, a, b):
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
    b = 0.0556434 * X - 0.2040259 * Y + 1.0572252 * Z
    rgb = np.stack([r, g, b], axis=-1)
    rgb = np.clip(rgb, 0, 1)
    mask = rgb <= 0.0031308
    rgb_srgb = np.where(mask, 12.92 * rgb, 1.055 * np.power(np.maximum(rgb, 1e-12), 1.0 / 2.4) - 0.055)
    rgb_srgb = np.clip(rgb_srgb * 255.0, 0, 255).astype(np.uint8)
    return rgb_srgb


def colorize_image_reuse(session, input_name, input_shape, input_path, output_path):
    original = Image.open(input_path).convert('RGB')
    orig_w, orig_h = original.size
    original_np = np.array(original)
    orig_L = rgb_to_lab_l(original_np)
    gray = original.convert('L')
    gray_resized = gray.resize((INFERENCE_SIZE, INFERENCE_SIZE), Image.BILINEAR)
    input_data = np.array(gray_resized, dtype=np.float32) / 255.0
    if len(input_shape) == 4 and input_shape[1] == 3:
        input_data = np.stack([input_data] * 3, axis=0)[np.newaxis, :, :, :]
    else:
        input_data = input_data[np.newaxis, np.newaxis, :, :]
    outputs = session.run(None, {input_name: input_data})
    output_data = outputs[0]
    if output_data.ndim == 4:
        if output_data.shape[1] in (1, 3):
            output_data = np.transpose(output_data[0], (1, 2, 0))
        else:
            output_data = output_data[0]
    output_data = np.squeeze(output_data)
    if output_data.ndim == 2:
        colorized = np.stack([output_data] * 3, axis=-1)
    elif output_data.shape[-1] == 3:
        colorized = output_data
    elif output_data.shape[-1] == 2:
        pass
    else:
        colorized = output_data[..., :3]
    if output_data.ndim == 3 and output_data.shape[-1] == 3:
        out_a = rgb_to_lab_a(colorized)
        out_b = rgb_to_lab_b(colorized)
    elif output_data.ndim == 3 and output_data.shape[-1] == 2:
        out_a = output_data[..., 0]
        out_b = output_data[..., 1]
    else:
        if colorized.max() <= 1.0:
            colorized = (colorized * 255).astype(np.uint8)
        result = Image.fromarray(colorized).resize((orig_w, orig_h), Image.BILINEAR)
        result.save(output_path)
        return
    out_a_pil = Image.fromarray(out_a.astype(np.float32), mode='F')
    out_b_pil = Image.fromarray(out_b.astype(np.float32), mode='F')
    out_a_resized = out_a_pil.resize((orig_w, orig_h), Image.BILINEAR)
    out_b_resized = out_b_pil.resize((orig_w, orig_h), Image.BILINEAR)
    out_a_arr = np.array(out_a_resized)
    out_b_arr = np.array(out_b_resized)
    result_rgb = lab_to_rgb(orig_L, out_a_arr, out_b_arr)
    result = Image.fromarray(result_rgb)
    result.save(output_path)


def test_cli_mode(images):
    print("\n=== 方式1: CLI 调用（每次子进程，每次重新加载模型）===")
    print(f"图片数量: {len(images)}")
    os.makedirs(OUTPUT_DIR_CLI, exist_ok=True)

    per_image_times = []
    total_start = time.time()

    for i, img_path in enumerate(images):
        out_path = os.path.join(OUTPUT_DIR_C#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    L = 116.0 * fy - 16.0
    return L


def rgb_to_lab_a(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    return 500.0 * (fx - fy)


def rgb_to_lab_b(rgb):
    rgb_f = rgb.astype(np.float32)
    return 116.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    return 200.0 * (fy - fz)


def lab_to_rgb(L, a, b):
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
    b = 0.0556434 * X - 0.2040259 * Y + 1.0572252 * Z
    rgb = np.stack([r, g, b], axis=-1)
    rgb = np.clip(rgb, 0, 1)
    mask = rgb <= 0.0031308
    rgb_srgb = np.where(mask, 12.92 * rgb, 1.055 * np.power(np.maximum(rgb, 1e-12), 1.0 / 2.4) - 0.055)
    rgb_srgb = np.clip(rgb_srgb * 255.0, 0, 255).astype(np.uint8)
    return rgb_srgb


def colorize_image_reuse(session, input_name, input_shape, input_path, output_path):
    original = Image.open(input_path).convert('RGB')
    orig_w, orig_h = original.size
    original_np = np.array(original)
    orig_L = rgb_to_lab_l(original_np)
    gray = original.convert('L')
    gray_resized = gray.resize((INFERENCE_SIZE, INFERENCE_SIZE), Image.BILINEAR)
    input_data = np.array(gray_resized, dtype=np.float32) / 255.0
    if len(input_shape) == 4 and input_shape[1] == 3:
        input_data = np.stack([input_data] * 3, axis=0)[np.newaxis, :, :, :]
    else:
        input_data = input_data[np.newaxis, np.newaxis, :, :]
    outputs = session.run(None, {input_name: input_data})
    output_data = outputs[0]
    if output_data.ndim == 4:
        if output_data.shape[1] in (1, 3):
            output_data = np.transpose(output_data[0], (1, 2, 0))
        else:
            output_data = output_data[0]
    output_data = np.squeeze(output_data)
    if output_data.ndim == 2:
        colorized = np.stack([output_data] * 3, axis=-1)
    elif output_data.shape[-1] == 3:
        colorized = output_data
    elif output_data.shape[-1] == 2:
        pass
    else:
        colorized = output_data[..., :3]
    if output_data.ndim == 3 and output_data.shape[-1] == 3:
        out_a = rgb_to_lab_a(colorized)
        out_b = rgb_to_lab_b(colorized)
    elif output_data.ndim == 3 and output_data.shape[-1] == 2:
        out_a = output_data[..., 0]
        out_b = output_data[..., 1]
    else:
        if colorized.max() <= 1.0:
            colorized = (colorized * 255).astype(np.uint8)
        result = Image.fromarray(colorized).resize((orig_w, orig_h), Image.BILINEAR)
        result.save(output_path)
        return
    out_a_pil = Image.fromarray(out_a.astype(np.float32), mode='F')
    out_b_pil = Image.fromarray(out_b.astype(np.float32), mode='F')
    out_a_resized = out_a_pil.resize((orig_w, orig_h), Image.BILINEAR)
    out_b_resized = out_b_pil.resize((orig_w, orig_h), Image.BILINEAR)
    out_a_arr = np.array(out_a_resized)
    out_b_arr = np.array(out_b_resized)
    result_rgb = lab_to_rgb(orig_L, out_a_arr, out_b_arr)
    result = Image.fromarray(result_rgb)
    result.save(output_path)


def test_cli_mode(images):
    print("\n=== 方式1: CLI 调用（每次子进程，每次重新加载模型）===")
    print(f"图片数量: {len(images)}")
    os.makedirs(OUTPUT_DIR_CLI, exist_ok=True)

    per_image_times = []
    total_start = time.time()

    for i, img_path in enumerate(images):
        out_path = os.path.join(OUTPUT_DIR_CLI, img_path.name)
        t0 = time.time()
        result = subprocess.run#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    L = 116.0 * fy - 16.0
    return L


def rgb_to_lab_a(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    return 500.0 * (fx - fy)


def rgb_to_lab_b(rgb):
    rgb_f = rgb.astype(np.float32)
    return 116.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    return 200.0 * (fy - fz)


def lab_to_rgb(L, a, b):
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
    b = 0.0556434 * X - 0.2040259 * Y + 1.0572252 * Z
    rgb = np.stack([r, g, b], axis=-1)
    rgb = np.clip(rgb, 0, 1)
    mask = rgb <= 0.0031308
    rgb_srgb = np.where(mask, 12.92 * rgb, 1.055 * np.power(np.maximum(rgb, 1e-12), 1.0 / 2.4) - 0.055)
    rgb_srgb = np.clip(rgb_srgb * 255.0, 0, 255).astype(np.uint8)
    return rgb_srgb


def colorize_image_reuse(session, input_name, input_shape, input_path, output_path):
    original = Image.open(input_path).convert('RGB')
    orig_w, orig_h = original.size
    original_np = np.array(original)
    orig_L = rgb_to_lab_l(original_np)
    gray = original.convert('L')
    gray_resized = gray.resize((INFERENCE_SIZE, INFERENCE_SIZE), Image.BILINEAR)
    input_data = np.array(gray_resized, dtype=np.float32) / 255.0
    if len(input_shape) == 4 and input_shape[1] == 3:
        input_data = np.stack([input_data] * 3, axis=0)[np.newaxis, :, :, :]
    else:
        input_data = input_data[np.newaxis, np.newaxis, :, :]
    outputs = session.run(None, {input_name: input_data})
    output_data = outputs[0]
    if output_data.ndim == 4:
        if output_data.shape[1] in (1, 3):
            output_data = np.transpose(output_data[0], (1, 2, 0))
        else:
            output_data = output_data[0]
    output_data = np.squeeze(output_data)
    if output_data.ndim == 2:
        colorized = np.stack([output_data] * 3, axis=-1)
    elif output_data.shape[-1] == 3:
        colorized = output_data
    elif output_data.shape[-1] == 2:
        pass
    else:
        colorized = output_data[..., :3]
    if output_data.ndim == 3 and output_data.shape[-1] == 3:
        out_a = rgb_to_lab_a(colorized)
        out_b = rgb_to_lab_b(colorized)
    elif output_data.ndim == 3 and output_data.shape[-1] == 2:
        out_a = output_data[..., 0]
        out_b = output_data[..., 1]
    else:
        if colorized.max() <= 1.0:
            colorized = (colorized * 255).astype(np.uint8)
        result = Image.fromarray(colorized).resize((orig_w, orig_h), Image.BILINEAR)
        result.save(output_path)
        return
    out_a_pil = Image.fromarray(out_a.astype(np.float32), mode='F')
    out_b_pil = Image.fromarray(out_b.astype(np.float32), mode='F')
    out_a_resized = out_a_pil.resize((orig_w, orig_h), Image.BILINEAR)
    out_b_resized = out_b_pil.resize((orig_w, orig_h), Image.BILINEAR)
    out_a_arr = np.array(out_a_resized)
    out_b_arr = np.array(out_b_resized)
    result_rgb = lab_to_rgb(orig_L, out_a_arr, out_b_arr)
    result = Image.fromarray(result_rgb)
    result.save(output_path)


def test_cli_mode(images):
    print("\n=== 方式1: CLI 调用（每次子进程，每次重新加载模型）===")
    print(f"图片数量: {len(images)}")
    os.makedirs(OUTPUT_DIR_CLI, exist_ok=True)

    per_image_times = []
    total_start = time.time()

    for i, img_path in enumerate(images):
        out_path = os.path.join(OUTPUT_DIR_CLI, img_path.name)
        t0 = time.time()
        result = subprocess.run(
            [sys.executable, COLORIZE#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    L = 116.0 * fy - 16.0
    return L


def rgb_to_lab_a(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    return 500.0 * (fx - fy)


def rgb_to_lab_b(rgb):
    rgb_f = rgb.astype(np.float32)
    return 116.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    return 200.0 * (fy - fz)


def lab_to_rgb(L, a, b):
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
    b = 0.0556434 * X - 0.2040259 * Y + 1.0572252 * Z
    rgb = np.stack([r, g, b], axis=-1)
    rgb = np.clip(rgb, 0, 1)
    mask = rgb <= 0.0031308
    rgb_srgb = np.where(mask, 12.92 * rgb, 1.055 * np.power(np.maximum(rgb, 1e-12), 1.0 / 2.4) - 0.055)
    rgb_srgb = np.clip(rgb_srgb * 255.0, 0, 255).astype(np.uint8)
    return rgb_srgb


def colorize_image_reuse(session, input_name, input_shape, input_path, output_path):
    original = Image.open(input_path).convert('RGB')
    orig_w, orig_h = original.size
    original_np = np.array(original)
    orig_L = rgb_to_lab_l(original_np)
    gray = original.convert('L')
    gray_resized = gray.resize((INFERENCE_SIZE, INFERENCE_SIZE), Image.BILINEAR)
    input_data = np.array(gray_resized, dtype=np.float32) / 255.0
    if len(input_shape) == 4 and input_shape[1] == 3:
        input_data = np.stack([input_data] * 3, axis=0)[np.newaxis, :, :, :]
    else:
        input_data = input_data[np.newaxis, np.newaxis, :, :]
    outputs = session.run(None, {input_name: input_data})
    output_data = outputs[0]
    if output_data.ndim == 4:
        if output_data.shape[1] in (1, 3):
            output_data = np.transpose(output_data[0], (1, 2, 0))
        else:
            output_data = output_data[0]
    output_data = np.squeeze(output_data)
    if output_data.ndim == 2:
        colorized = np.stack([output_data] * 3, axis=-1)
    elif output_data.shape[-1] == 3:
        colorized = output_data
    elif output_data.shape[-1] == 2:
        pass
    else:
        colorized = output_data[..., :3]
    if output_data.ndim == 3 and output_data.shape[-1] == 3:
        out_a = rgb_to_lab_a(colorized)
        out_b = rgb_to_lab_b(colorized)
    elif output_data.ndim == 3 and output_data.shape[-1] == 2:
        out_a = output_data[..., 0]
        out_b = output_data[..., 1]
    else:
        if colorized.max() <= 1.0:
            colorized = (colorized * 255).astype(np.uint8)
        result = Image.fromarray(colorized).resize((orig_w, orig_h), Image.BILINEAR)
        result.save(output_path)
        return
    out_a_pil = Image.fromarray(out_a.astype(np.float32), mode='F')
    out_b_pil = Image.fromarray(out_b.astype(np.float32), mode='F')
    out_a_resized = out_a_pil.resize((orig_w, orig_h), Image.BILINEAR)
    out_b_resized = out_b_pil.resize((orig_w, orig_h), Image.BILINEAR)
    out_a_arr = np.array(out_a_resized)
    out_b_arr = np.array(out_b_resized)
    result_rgb = lab_to_rgb(orig_L, out_a_arr, out_b_arr)
    result = Image.fromarray(result_rgb)
    result.save(output_path)


def test_cli_mode(images):
    print("\n=== 方式1: CLI 调用（每次子进程，每次重新加载模型）===")
    print(f"图片数量: {len(images)}")
    os.makedirs(OUTPUT_DIR_CLI, exist_ok=True)

    per_image_times = []
    total_start = time.time()

    for i, img_path in enumerate(images):
        out_path = os.path.join(OUTPUT_DIR_CLI, img_path.name)
        t0 = time.time()
        result = subprocess.run(
            [sys.executable, COLORIZE_PY, '-i', str(img_path), '-o', out_path, '-m', MODEL#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    L = 116.0 * fy - 16.0
    return L


def rgb_to_lab_a(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    return 500.0 * (fx - fy)


def rgb_to_lab_b(rgb):
    rgb_f = rgb.astype(np.float32)
    return 116.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    return 200.0 * (fy - fz)


def lab_to_rgb(L, a, b):
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
    b = 0.0556434 * X - 0.2040259 * Y + 1.0572252 * Z
    rgb = np.stack([r, g, b], axis=-1)
    rgb = np.clip(rgb, 0, 1)
    mask = rgb <= 0.0031308
    rgb_srgb = np.where(mask, 12.92 * rgb, 1.055 * np.power(np.maximum(rgb, 1e-12), 1.0 / 2.4) - 0.055)
    rgb_srgb = np.clip(rgb_srgb * 255.0, 0, 255).astype(np.uint8)
    return rgb_srgb


def colorize_image_reuse(session, input_name, input_shape, input_path, output_path):
    original = Image.open(input_path).convert('RGB')
    orig_w, orig_h = original.size
    original_np = np.array(original)
    orig_L = rgb_to_lab_l(original_np)
    gray = original.convert('L')
    gray_resized = gray.resize((INFERENCE_SIZE, INFERENCE_SIZE), Image.BILINEAR)
    input_data = np.array(gray_resized, dtype=np.float32) / 255.0
    if len(input_shape) == 4 and input_shape[1] == 3:
        input_data = np.stack([input_data] * 3, axis=0)[np.newaxis, :, :, :]
    else:
        input_data = input_data[np.newaxis, np.newaxis, :, :]
    outputs = session.run(None, {input_name: input_data})
    output_data = outputs[0]
    if output_data.ndim == 4:
        if output_data.shape[1] in (1, 3):
            output_data = np.transpose(output_data[0], (1, 2, 0))
        else:
            output_data = output_data[0]
    output_data = np.squeeze(output_data)
    if output_data.ndim == 2:
        colorized = np.stack([output_data] * 3, axis=-1)
    elif output_data.shape[-1] == 3:
        colorized = output_data
    elif output_data.shape[-1] == 2:
        pass
    else:
        colorized = output_data[..., :3]
    if output_data.ndim == 3 and output_data.shape[-1] == 3:
        out_a = rgb_to_lab_a(colorized)
        out_b = rgb_to_lab_b(colorized)
    elif output_data.ndim == 3 and output_data.shape[-1] == 2:
        out_a = output_data[..., 0]
        out_b = output_data[..., 1]
    else:
        if colorized.max() <= 1.0:
            colorized = (colorized * 255).astype(np.uint8)
        result = Image.fromarray(colorized).resize((orig_w, orig_h), Image.BILINEAR)
        result.save(output_path)
        return
    out_a_pil = Image.fromarray(out_a.astype(np.float32), mode='F')
    out_b_pil = Image.fromarray(out_b.astype(np.float32), mode='F')
    out_a_resized = out_a_pil.resize((orig_w, orig_h), Image.BILINEAR)
    out_b_resized = out_b_pil.resize((orig_w, orig_h), Image.BILINEAR)
    out_a_arr = np.array(out_a_resized)
    out_b_arr = np.array(out_b_resized)
    result_rgb = lab_to_rgb(orig_L, out_a_arr, out_b_arr)
    result = Image.fromarray(result_rgb)
    result.save(output_path)


def test_cli_mode(images):
    print("\n=== 方式1: CLI 调用（每次子进程，每次重新加载模型）===")
    print(f"图片数量: {len(images)}")
    os.makedirs(OUTPUT_DIR_CLI, exist_ok=True)

    per_image_times = []
    total_start = time.time()

    for i, img_path in enumerate(images):
        out_path = os.path.join(OUTPUT_DIR_CLI, img_path.name)
        t0 = time.time()
        result = subprocess.run(
            [sys.executable, COLORIZE_PY, '-i', str(img_path), '-o', out_path, '-m', MODEL_PATH, '-r', '19'],
            capture_output=True, text=True
        )#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    L = 116.0 * fy - 16.0
    return L


def rgb_to_lab_a(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    return 500.0 * (fx - fy)


def rgb_to_lab_b(rgb):
    rgb_f = rgb.astype(np.float32)
    return 116.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    return 200.0 * (fy - fz)


def lab_to_rgb(L, a, b):
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
    b = 0.0556434 * X - 0.2040259 * Y + 1.0572252 * Z
    rgb = np.stack([r, g, b], axis=-1)
    rgb = np.clip(rgb, 0, 1)
    mask = rgb <= 0.0031308
    rgb_srgb = np.where(mask, 12.92 * rgb, 1.055 * np.power(np.maximum(rgb, 1e-12), 1.0 / 2.4) - 0.055)
    rgb_srgb = np.clip(rgb_srgb * 255.0, 0, 255).astype(np.uint8)
    return rgb_srgb


def colorize_image_reuse(session, input_name, input_shape, input_path, output_path):
    original = Image.open(input_path).convert('RGB')
    orig_w, orig_h = original.size
    original_np = np.array(original)
    orig_L = rgb_to_lab_l(original_np)
    gray = original.convert('L')
    gray_resized = gray.resize((INFERENCE_SIZE, INFERENCE_SIZE), Image.BILINEAR)
    input_data = np.array(gray_resized, dtype=np.float32) / 255.0
    if len(input_shape) == 4 and input_shape[1] == 3:
        input_data = np.stack([input_data] * 3, axis=0)[np.newaxis, :, :, :]
    else:
        input_data = input_data[np.newaxis, np.newaxis, :, :]
    outputs = session.run(None, {input_name: input_data})
    output_data = outputs[0]
    if output_data.ndim == 4:
        if output_data.shape[1] in (1, 3):
            output_data = np.transpose(output_data[0], (1, 2, 0))
        else:
            output_data = output_data[0]
    output_data = np.squeeze(output_data)
    if output_data.ndim == 2:
        colorized = np.stack([output_data] * 3, axis=-1)
    elif output_data.shape[-1] == 3:
        colorized = output_data
    elif output_data.shape[-1] == 2:
        pass
    else:
        colorized = output_data[..., :3]
    if output_data.ndim == 3 and output_data.shape[-1] == 3:
        out_a = rgb_to_lab_a(colorized)
        out_b = rgb_to_lab_b(colorized)
    elif output_data.ndim == 3 and output_data.shape[-1] == 2:
        out_a = output_data[..., 0]
        out_b = output_data[..., 1]
    else:
        if colorized.max() <= 1.0:
            colorized = (colorized * 255).astype(np.uint8)
        result = Image.fromarray(colorized).resize((orig_w, orig_h), Image.BILINEAR)
        result.save(output_path)
        return
    out_a_pil = Image.fromarray(out_a.astype(np.float32), mode='F')
    out_b_pil = Image.fromarray(out_b.astype(np.float32), mode='F')
    out_a_resized = out_a_pil.resize((orig_w, orig_h), Image.BILINEAR)
    out_b_resized = out_b_pil.resize((orig_w, orig_h), Image.BILINEAR)
    out_a_arr = np.array(out_a_resized)
    out_b_arr = np.array(out_b_resized)
    result_rgb = lab_to_rgb(orig_L, out_a_arr, out_b_arr)
    result = Image.fromarray(result_rgb)
    result.save(output_path)


def test_cli_mode(images):
    print("\n=== 方式1: CLI 调用（每次子进程，每次重新加载模型）===")
    print(f"图片数量: {len(images)}")
    os.makedirs(OUTPUT_DIR_CLI, exist_ok=True)

    per_image_times = []
    total_start = time.time()

    for i, img_path in enumerate(images):
        out_path = os.path.join(OUTPUT_DIR_CLI, img_path.name)
        t0 = time.time()
        result = subprocess.run(
            [sys.executable, COLORIZE_PY, '-i', str(img_path), '-o', out_path, '-m', MODEL_PATH, '-r', '19'],
            capture_output=True, text=True
        )
        t1 = time.time()
#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    L = 116.0 * fy - 16.0
    return L


def rgb_to_lab_a(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    return 500.0 * (fx - fy)


def rgb_to_lab_b(rgb):
    rgb_f = rgb.astype(np.float32)
    return 116.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    return 200.0 * (fy - fz)


def lab_to_rgb(L, a, b):
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
    b = 0.0556434 * X - 0.2040259 * Y + 1.0572252 * Z
    rgb = np.stack([r, g, b], axis=-1)
    rgb = np.clip(rgb, 0, 1)
    mask = rgb <= 0.0031308
    rgb_srgb = np.where(mask, 12.92 * rgb, 1.055 * np.power(np.maximum(rgb, 1e-12), 1.0 / 2.4) - 0.055)
    rgb_srgb = np.clip(rgb_srgb * 255.0, 0, 255).astype(np.uint8)
    return rgb_srgb


def colorize_image_reuse(session, input_name, input_shape, input_path, output_path):
    original = Image.open(input_path).convert('RGB')
    orig_w, orig_h = original.size
    original_np = np.array(original)
    orig_L = rgb_to_lab_l(original_np)
    gray = original.convert('L')
    gray_resized = gray.resize((INFERENCE_SIZE, INFERENCE_SIZE), Image.BILINEAR)
    input_data = np.array(gray_resized, dtype=np.float32) / 255.0
    if len(input_shape) == 4 and input_shape[1] == 3:
        input_data = np.stack([input_data] * 3, axis=0)[np.newaxis, :, :, :]
    else:
        input_data = input_data[np.newaxis, np.newaxis, :, :]
    outputs = session.run(None, {input_name: input_data})
    output_data = outputs[0]
    if output_data.ndim == 4:
        if output_data.shape[1] in (1, 3):
            output_data = np.transpose(output_data[0], (1, 2, 0))
        else:
            output_data = output_data[0]
    output_data = np.squeeze(output_data)
    if output_data.ndim == 2:
        colorized = np.stack([output_data] * 3, axis=-1)
    elif output_data.shape[-1] == 3:
        colorized = output_data
    elif output_data.shape[-1] == 2:
        pass
    else:
        colorized = output_data[..., :3]
    if output_data.ndim == 3 and output_data.shape[-1] == 3:
        out_a = rgb_to_lab_a(colorized)
        out_b = rgb_to_lab_b(colorized)
    elif output_data.ndim == 3 and output_data.shape[-1] == 2:
        out_a = output_data[..., 0]
        out_b = output_data[..., 1]
    else:
        if colorized.max() <= 1.0:
            colorized = (colorized * 255).astype(np.uint8)
        result = Image.fromarray(colorized).resize((orig_w, orig_h), Image.BILINEAR)
        result.save(output_path)
        return
    out_a_pil = Image.fromarray(out_a.astype(np.float32), mode='F')
    out_b_pil = Image.fromarray(out_b.astype(np.float32), mode='F')
    out_a_resized = out_a_pil.resize((orig_w, orig_h), Image.BILINEAR)
    out_b_resized = out_b_pil.resize((orig_w, orig_h), Image.BILINEAR)
    out_a_arr = np.array(out_a_resized)
    out_b_arr = np.array(out_b_resized)
    result_rgb = lab_to_rgb(orig_L, out_a_arr, out_b_arr)
    result = Image.fromarray(result_rgb)
    result.save(output_path)


def test_cli_mode(images):
    print("\n=== 方式1: CLI 调用（每次子进程，每次重新加载模型）===")
    print(f"图片数量: {len(images)}")
    os.makedirs(OUTPUT_DIR_CLI, exist_ok=True)

    per_image_times = []
    total_start = time.time()

    for i, img_path in enumerate(images):
        out_path = os.path.join(OUTPUT_DIR_CLI, img_path.name)
        t0 = time.time()
        result = subprocess.run(
            [sys.executable, COLORIZE_PY, '-i', str(img_path), '-o', out_path, '-m', MODEL_PATH, '-r', '19'],
            capture_output=True, text=True
        )
        t1 = time.time()
        elapsed = t1 - t0
        per#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    L = 116.0 * fy - 16.0
    return L


def rgb_to_lab_a(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    return 500.0 * (fx - fy)


def rgb_to_lab_b(rgb):
    rgb_f = rgb.astype(np.float32)
    return 116.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    return 200.0 * (fy - fz)


def lab_to_rgb(L, a, b):
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
    b = 0.0556434 * X - 0.2040259 * Y + 1.0572252 * Z
    rgb = np.stack([r, g, b], axis=-1)
    rgb = np.clip(rgb, 0, 1)
    mask = rgb <= 0.0031308
    rgb_srgb = np.where(mask, 12.92 * rgb, 1.055 * np.power(np.maximum(rgb, 1e-12), 1.0 / 2.4) - 0.055)
    rgb_srgb = np.clip(rgb_srgb * 255.0, 0, 255).astype(np.uint8)
    return rgb_srgb


def colorize_image_reuse(session, input_name, input_shape, input_path, output_path):
    original = Image.open(input_path).convert('RGB')
    orig_w, orig_h = original.size
    original_np = np.array(original)
    orig_L = rgb_to_lab_l(original_np)
    gray = original.convert('L')
    gray_resized = gray.resize((INFERENCE_SIZE, INFERENCE_SIZE), Image.BILINEAR)
    input_data = np.array(gray_resized, dtype=np.float32) / 255.0
    if len(input_shape) == 4 and input_shape[1] == 3:
        input_data = np.stack([input_data] * 3, axis=0)[np.newaxis, :, :, :]
    else:
        input_data = input_data[np.newaxis, np.newaxis, :, :]
    outputs = session.run(None, {input_name: input_data})
    output_data = outputs[0]
    if output_data.ndim == 4:
        if output_data.shape[1] in (1, 3):
            output_data = np.transpose(output_data[0], (1, 2, 0))
        else:
            output_data = output_data[0]
    output_data = np.squeeze(output_data)
    if output_data.ndim == 2:
        colorized = np.stack([output_data] * 3, axis=-1)
    elif output_data.shape[-1] == 3:
        colorized = output_data
    elif output_data.shape[-1] == 2:
        pass
    else:
        colorized = output_data[..., :3]
    if output_data.ndim == 3 and output_data.shape[-1] == 3:
        out_a = rgb_to_lab_a(colorized)
        out_b = rgb_to_lab_b(colorized)
    elif output_data.ndim == 3 and output_data.shape[-1] == 2:
        out_a = output_data[..., 0]
        out_b = output_data[..., 1]
    else:
        if colorized.max() <= 1.0:
            colorized = (colorized * 255).astype(np.uint8)
        result = Image.fromarray(colorized).resize((orig_w, orig_h), Image.BILINEAR)
        result.save(output_path)
        return
    out_a_pil = Image.fromarray(out_a.astype(np.float32), mode='F')
    out_b_pil = Image.fromarray(out_b.astype(np.float32), mode='F')
    out_a_resized = out_a_pil.resize((orig_w, orig_h), Image.BILINEAR)
    out_b_resized = out_b_pil.resize((orig_w, orig_h), Image.BILINEAR)
    out_a_arr = np.array(out_a_resized)
    out_b_arr = np.array(out_b_resized)
    result_rgb = lab_to_rgb(orig_L, out_a_arr, out_b_arr)
    result = Image.fromarray(result_rgb)
    result.save(output_path)


def test_cli_mode(images):
    print("\n=== 方式1: CLI 调用（每次子进程，每次重新加载模型）===")
    print(f"图片数量: {len(images)}")
    os.makedirs(OUTPUT_DIR_CLI, exist_ok=True)

    per_image_times = []
    total_start = time.time()

    for i, img_path in enumerate(images):
        out_path = os.path.join(OUTPUT_DIR_CLI, img_path.name)
        t0 = time.time()
        result = subprocess.run(
            [sys.executable, COLORIZE_PY, '-i', str(img_path), '-o', out_path, '-m', MODEL_PATH, '-r', '19'],
            capture_output=True, text=True
        )
        t1 = time.time()
        elapsed = t1 - t0
        per_image_times.append(elapsed)
        size = Image.open(img_path).size
        out_size#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    L = 116.0 * fy - 16.0
    return L


def rgb_to_lab_a(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    return 500.0 * (fx - fy)


def rgb_to_lab_b(rgb):
    rgb_f = rgb.astype(np.float32)
    return 116.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    return 200.0 * (fy - fz)


def lab_to_rgb(L, a, b):
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
    b = 0.0556434 * X - 0.2040259 * Y + 1.0572252 * Z
    rgb = np.stack([r, g, b], axis=-1)
    rgb = np.clip(rgb, 0, 1)
    mask = rgb <= 0.0031308
    rgb_srgb = np.where(mask, 12.92 * rgb, 1.055 * np.power(np.maximum(rgb, 1e-12), 1.0 / 2.4) - 0.055)
    rgb_srgb = np.clip(rgb_srgb * 255.0, 0, 255).astype(np.uint8)
    return rgb_srgb


def colorize_image_reuse(session, input_name, input_shape, input_path, output_path):
    original = Image.open(input_path).convert('RGB')
    orig_w, orig_h = original.size
    original_np = np.array(original)
    orig_L = rgb_to_lab_l(original_np)
    gray = original.convert('L')
    gray_resized = gray.resize((INFERENCE_SIZE, INFERENCE_SIZE), Image.BILINEAR)
    input_data = np.array(gray_resized, dtype=np.float32) / 255.0
    if len(input_shape) == 4 and input_shape[1] == 3:
        input_data = np.stack([input_data] * 3, axis=0)[np.newaxis, :, :, :]
    else:
        input_data = input_data[np.newaxis, np.newaxis, :, :]
    outputs = session.run(None, {input_name: input_data})
    output_data = outputs[0]
    if output_data.ndim == 4:
        if output_data.shape[1] in (1, 3):
            output_data = np.transpose(output_data[0], (1, 2, 0))
        else:
            output_data = output_data[0]
    output_data = np.squeeze(output_data)
    if output_data.ndim == 2:
        colorized = np.stack([output_data] * 3, axis=-1)
    elif output_data.shape[-1] == 3:
        colorized = output_data
    elif output_data.shape[-1] == 2:
        pass
    else:
        colorized = output_data[..., :3]
    if output_data.ndim == 3 and output_data.shape[-1] == 3:
        out_a = rgb_to_lab_a(colorized)
        out_b = rgb_to_lab_b(colorized)
    elif output_data.ndim == 3 and output_data.shape[-1] == 2:
        out_a = output_data[..., 0]
        out_b = output_data[..., 1]
    else:
        if colorized.max() <= 1.0:
            colorized = (colorized * 255).astype(np.uint8)
        result = Image.fromarray(colorized).resize((orig_w, orig_h), Image.BILINEAR)
        result.save(output_path)
        return
    out_a_pil = Image.fromarray(out_a.astype(np.float32), mode='F')
    out_b_pil = Image.fromarray(out_b.astype(np.float32), mode='F')
    out_a_resized = out_a_pil.resize((orig_w, orig_h), Image.BILINEAR)
    out_b_resized = out_b_pil.resize((orig_w, orig_h), Image.BILINEAR)
    out_a_arr = np.array(out_a_resized)
    out_b_arr = np.array(out_b_resized)
    result_rgb = lab_to_rgb(orig_L, out_a_arr, out_b_arr)
    result = Image.fromarray(result_rgb)
    result.save(output_path)


def test_cli_mode(images):
    print("\n=== 方式1: CLI 调用（每次子进程，每次重新加载模型）===")
    print(f"图片数量: {len(images)}")
    os.makedirs(OUTPUT_DIR_CLI, exist_ok=True)

    per_image_times = []
    total_start = time.time()

    for i, img_path in enumerate(images):
        out_path = os.path.join(OUTPUT_DIR_CLI, img_path.name)
        t0 = time.time()
        result = subprocess.run(
            [sys.executable, COLORIZE_PY, '-i', str(img_path), '-o', out_path, '-m', MODEL_PATH, '-r', '19'],
            capture_output=True, text=True
        )
        t1 = time.time()
        elapsed = t1 - t0
        per_image_times.append(elapsed)
        size = Image.open(img_path).size
        out_size = Image.open(out_path).size if os.path.exists(out_path) else 'FAILED'

#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    L = 116.0 * fy - 16.0
    return L


def rgb_to_lab_a(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    return 500.0 * (fx - fy)


def rgb_to_lab_b(rgb):
    rgb_f = rgb.astype(np.float32)
    return 116.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    return 200.0 * (fy - fz)


def lab_to_rgb(L, a, b):
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
    b = 0.0556434 * X - 0.2040259 * Y + 1.0572252 * Z
    rgb = np.stack([r, g, b], axis=-1)
    rgb = np.clip(rgb, 0, 1)
    mask = rgb <= 0.0031308
    rgb_srgb = np.where(mask, 12.92 * rgb, 1.055 * np.power(np.maximum(rgb, 1e-12), 1.0 / 2.4) - 0.055)
    rgb_srgb = np.clip(rgb_srgb * 255.0, 0, 255).astype(np.uint8)
    return rgb_srgb


def colorize_image_reuse(session, input_name, input_shape, input_path, output_path):
    original = Image.open(input_path).convert('RGB')
    orig_w, orig_h = original.size
    original_np = np.array(original)
    orig_L = rgb_to_lab_l(original_np)
    gray = original.convert('L')
    gray_resized = gray.resize((INFERENCE_SIZE, INFERENCE_SIZE), Image.BILINEAR)
    input_data = np.array(gray_resized, dtype=np.float32) / 255.0
    if len(input_shape) == 4 and input_shape[1] == 3:
        input_data = np.stack([input_data] * 3, axis=0)[np.newaxis, :, :, :]
    else:
        input_data = input_data[np.newaxis, np.newaxis, :, :]
    outputs = session.run(None, {input_name: input_data})
    output_data = outputs[0]
    if output_data.ndim == 4:
        if output_data.shape[1] in (1, 3):
            output_data = np.transpose(output_data[0], (1, 2, 0))
        else:
            output_data = output_data[0]
    output_data = np.squeeze(output_data)
    if output_data.ndim == 2:
        colorized = np.stack([output_data] * 3, axis=-1)
    elif output_data.shape[-1] == 3:
        colorized = output_data
    elif output_data.shape[-1] == 2:
        pass
    else:
        colorized = output_data[..., :3]
    if output_data.ndim == 3 and output_data.shape[-1] == 3:
        out_a = rgb_to_lab_a(colorized)
        out_b = rgb_to_lab_b(colorized)
    elif output_data.ndim == 3 and output_data.shape[-1] == 2:
        out_a = output_data[..., 0]
        out_b = output_data[..., 1]
    else:
        if colorized.max() <= 1.0:
            colorized = (colorized * 255).astype(np.uint8)
        result = Image.fromarray(colorized).resize((orig_w, orig_h), Image.BILINEAR)
        result.save(output_path)
        return
    out_a_pil = Image.fromarray(out_a.astype(np.float32), mode='F')
    out_b_pil = Image.fromarray(out_b.astype(np.float32), mode='F')
    out_a_resized = out_a_pil.resize((orig_w, orig_h), Image.BILINEAR)
    out_b_resized = out_b_pil.resize((orig_w, orig_h), Image.BILINEAR)
    out_a_arr = np.array(out_a_resized)
    out_b_arr = np.array(out_b_resized)
    result_rgb = lab_to_rgb(orig_L, out_a_arr, out_b_arr)
    result = Image.fromarray(result_rgb)
    result.save(output_path)


def test_cli_mode(images):
    print("\n=== 方式1: CLI 调用（每次子进程，每次重新加载模型）===")
    print(f"图片数量: {len(images)}")
    os.makedirs(OUTPUT_DIR_CLI, exist_ok=True)

    per_image_times = []
    total_start = time.time()

    for i, img_path in enumerate(images):
        out_path = os.path.join(OUTPUT_DIR_CLI, img_path.name)
        t0 = time.time()
        result = subprocess.run(
            [sys.executable, COLORIZE_PY, '-i', str(img_path), '-o', out_path, '-m', MODEL_PATH, '-r', '19'],
            capture_output=True, text=True
        )
        t1 = time.time()
        elapsed = t1 - t0
        per_image_times.append(elapsed)
        size = Image.open(img_path).size
        out_size = Image.open(out_path).size if os.path.exists(out_path) else 'FAILED'

        status = "OK" if result.returncode == 0 and os.path.exists(out_path) else#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    L = 116.0 * fy - 16.0
    return L


def rgb_to_lab_a(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    return 500.0 * (fx - fy)


def rgb_to_lab_b(rgb):
    rgb_f = rgb.astype(np.float32)
    return 116.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    return 200.0 * (fy - fz)


def lab_to_rgb(L, a, b):
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
    b = 0.0556434 * X - 0.2040259 * Y + 1.0572252 * Z
    rgb = np.stack([r, g, b], axis=-1)
    rgb = np.clip(rgb, 0, 1)
    mask = rgb <= 0.0031308
    rgb_srgb = np.where(mask, 12.92 * rgb, 1.055 * np.power(np.maximum(rgb, 1e-12), 1.0 / 2.4) - 0.055)
    rgb_srgb = np.clip(rgb_srgb * 255.0, 0, 255).astype(np.uint8)
    return rgb_srgb


def colorize_image_reuse(session, input_name, input_shape, input_path, output_path):
    original = Image.open(input_path).convert('RGB')
    orig_w, orig_h = original.size
    original_np = np.array(original)
    orig_L = rgb_to_lab_l(original_np)
    gray = original.convert('L')
    gray_resized = gray.resize((INFERENCE_SIZE, INFERENCE_SIZE), Image.BILINEAR)
    input_data = np.array(gray_resized, dtype=np.float32) / 255.0
    if len(input_shape) == 4 and input_shape[1] == 3:
        input_data = np.stack([input_data] * 3, axis=0)[np.newaxis, :, :, :]
    else:
        input_data = input_data[np.newaxis, np.newaxis, :, :]
    outputs = session.run(None, {input_name: input_data})
    output_data = outputs[0]
    if output_data.ndim == 4:
        if output_data.shape[1] in (1, 3):
            output_data = np.transpose(output_data[0], (1, 2, 0))
        else:
            output_data = output_data[0]
    output_data = np.squeeze(output_data)
    if output_data.ndim == 2:
        colorized = np.stack([output_data] * 3, axis=-1)
    elif output_data.shape[-1] == 3:
        colorized = output_data
    elif output_data.shape[-1] == 2:
        pass
    else:
        colorized = output_data[..., :3]
    if output_data.ndim == 3 and output_data.shape[-1] == 3:
        out_a = rgb_to_lab_a(colorized)
        out_b = rgb_to_lab_b(colorized)
    elif output_data.ndim == 3 and output_data.shape[-1] == 2:
        out_a = output_data[..., 0]
        out_b = output_data[..., 1]
    else:
        if colorized.max() <= 1.0:
            colorized = (colorized * 255).astype(np.uint8)
        result = Image.fromarray(colorized).resize((orig_w, orig_h), Image.BILINEAR)
        result.save(output_path)
        return
    out_a_pil = Image.fromarray(out_a.astype(np.float32), mode='F')
    out_b_pil = Image.fromarray(out_b.astype(np.float32), mode='F')
    out_a_resized = out_a_pil.resize((orig_w, orig_h), Image.BILINEAR)
    out_b_resized = out_b_pil.resize((orig_w, orig_h), Image.BILINEAR)
    out_a_arr = np.array(out_a_resized)
    out_b_arr = np.array(out_b_resized)
    result_rgb = lab_to_rgb(orig_L, out_a_arr, out_b_arr)
    result = Image.fromarray(result_rgb)
    result.save(output_path)


def test_cli_mode(images):
    print("\n=== 方式1: CLI 调用（每次子进程，每次重新加载模型）===")
    print(f"图片数量: {len(images)}")
    os.makedirs(OUTPUT_DIR_CLI, exist_ok=True)

    per_image_times = []
    total_start = time.time()

    for i, img_path in enumerate(images):
        out_path = os.path.join(OUTPUT_DIR_CLI, img_path.name)
        t0 = time.time()
        result = subprocess.run(
            [sys.executable, COLORIZE_PY, '-i', str(img_path), '-o', out_path, '-m', MODEL_PATH, '-r', '19'],
            capture_output=True, text=True
        )
        t1 = time.time()
        elapsed = t1 - t0
        per_image_times.append(elapsed)
        size = Image.open(img_path).size
        out_size = Image.open(out_path).size if os.path.exists(out_path) else 'FAILED'

        status = "OK" if result.returncode == 0 and os.path.exists(out_path) else f"FAIL (rc={result.returncode})"
        print(f"  [{i+#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    L = 116.0 * fy - 16.0
    return L


def rgb_to_lab_a(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    return 500.0 * (fx - fy)


def rgb_to_lab_b(rgb):
    rgb_f = rgb.astype(np.float32)
    return 116.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    return 200.0 * (fy - fz)


def lab_to_rgb(L, a, b):
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
    b = 0.0556434 * X - 0.2040259 * Y + 1.0572252 * Z
    rgb = np.stack([r, g, b], axis=-1)
    rgb = np.clip(rgb, 0, 1)
    mask = rgb <= 0.0031308
    rgb_srgb = np.where(mask, 12.92 * rgb, 1.055 * np.power(np.maximum(rgb, 1e-12), 1.0 / 2.4) - 0.055)
    rgb_srgb = np.clip(rgb_srgb * 255.0, 0, 255).astype(np.uint8)
    return rgb_srgb


def colorize_image_reuse(session, input_name, input_shape, input_path, output_path):
    original = Image.open(input_path).convert('RGB')
    orig_w, orig_h = original.size
    original_np = np.array(original)
    orig_L = rgb_to_lab_l(original_np)
    gray = original.convert('L')
    gray_resized = gray.resize((INFERENCE_SIZE, INFERENCE_SIZE), Image.BILINEAR)
    input_data = np.array(gray_resized, dtype=np.float32) / 255.0
    if len(input_shape) == 4 and input_shape[1] == 3:
        input_data = np.stack([input_data] * 3, axis=0)[np.newaxis, :, :, :]
    else:
        input_data = input_data[np.newaxis, np.newaxis, :, :]
    outputs = session.run(None, {input_name: input_data})
    output_data = outputs[0]
    if output_data.ndim == 4:
        if output_data.shape[1] in (1, 3):
            output_data = np.transpose(output_data[0], (1, 2, 0))
        else:
            output_data = output_data[0]
    output_data = np.squeeze(output_data)
    if output_data.ndim == 2:
        colorized = np.stack([output_data] * 3, axis=-1)
    elif output_data.shape[-1] == 3:
        colorized = output_data
    elif output_data.shape[-1] == 2:
        pass
    else:
        colorized = output_data[..., :3]
    if output_data.ndim == 3 and output_data.shape[-1] == 3:
        out_a = rgb_to_lab_a(colorized)
        out_b = rgb_to_lab_b(colorized)
    elif output_data.ndim == 3 and output_data.shape[-1] == 2:
        out_a = output_data[..., 0]
        out_b = output_data[..., 1]
    else:
        if colorized.max() <= 1.0:
            colorized = (colorized * 255).astype(np.uint8)
        result = Image.fromarray(colorized).resize((orig_w, orig_h), Image.BILINEAR)
        result.save(output_path)
        return
    out_a_pil = Image.fromarray(out_a.astype(np.float32), mode='F')
    out_b_pil = Image.fromarray(out_b.astype(np.float32), mode='F')
    out_a_resized = out_a_pil.resize((orig_w, orig_h), Image.BILINEAR)
    out_b_resized = out_b_pil.resize((orig_w, orig_h), Image.BILINEAR)
    out_a_arr = np.array(out_a_resized)
    out_b_arr = np.array(out_b_resized)
    result_rgb = lab_to_rgb(orig_L, out_a_arr, out_b_arr)
    result = Image.fromarray(result_rgb)
    result.save(output_path)


def test_cli_mode(images):
    print("\n=== 方式1: CLI 调用（每次子进程，每次重新加载模型）===")
    print(f"图片数量: {len(images)}")
    os.makedirs(OUTPUT_DIR_CLI, exist_ok=True)

    per_image_times = []
    total_start = time.time()

    for i, img_path in enumerate(images):
        out_path = os.path.join(OUTPUT_DIR_CLI, img_path.name)
        t0 = time.time()
        result = subprocess.run(
            [sys.executable, COLORIZE_PY, '-i', str(img_path), '-o', out_path, '-m', MODEL_PATH, '-r', '19'],
            capture_output=True, text=True
        )
        t1 = time.time()
        elapsed = t1 - t0
        per_image_times.append(elapsed)
        size = Image.open(img_path).size
        out_size = Image.open(out_path).size if os.path.exists(out_path) else 'FAILED'

        status = "OK" if result.returncode == 0 and os.path.exists(out_path) else f"FAIL (rc={result.returncode})"
        print(f"  [{i+1}/{len(images)}] {img_path.name} {size[0]}x{size#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    L = 116.0 * fy - 16.0
    return L


def rgb_to_lab_a(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    return 500.0 * (fx - fy)


def rgb_to_lab_b(rgb):
    rgb_f = rgb.astype(np.float32)
    return 116.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    return 200.0 * (fy - fz)


def lab_to_rgb(L, a, b):
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
    b = 0.0556434 * X - 0.2040259 * Y + 1.0572252 * Z
    rgb = np.stack([r, g, b], axis=-1)
    rgb = np.clip(rgb, 0, 1)
    mask = rgb <= 0.0031308
    rgb_srgb = np.where(mask, 12.92 * rgb, 1.055 * np.power(np.maximum(rgb, 1e-12), 1.0 / 2.4) - 0.055)
    rgb_srgb = np.clip(rgb_srgb * 255.0, 0, 255).astype(np.uint8)
    return rgb_srgb


def colorize_image_reuse(session, input_name, input_shape, input_path, output_path):
    original = Image.open(input_path).convert('RGB')
    orig_w, orig_h = original.size
    original_np = np.array(original)
    orig_L = rgb_to_lab_l(original_np)
    gray = original.convert('L')
    gray_resized = gray.resize((INFERENCE_SIZE, INFERENCE_SIZE), Image.BILINEAR)
    input_data = np.array(gray_resized, dtype=np.float32) / 255.0
    if len(input_shape) == 4 and input_shape[1] == 3:
        input_data = np.stack([input_data] * 3, axis=0)[np.newaxis, :, :, :]
    else:
        input_data = input_data[np.newaxis, np.newaxis, :, :]
    outputs = session.run(None, {input_name: input_data})
    output_data = outputs[0]
    if output_data.ndim == 4:
        if output_data.shape[1] in (1, 3):
            output_data = np.transpose(output_data[0], (1, 2, 0))
        else:
            output_data = output_data[0]
    output_data = np.squeeze(output_data)
    if output_data.ndim == 2:
        colorized = np.stack([output_data] * 3, axis=-1)
    elif output_data.shape[-1] == 3:
        colorized = output_data
    elif output_data.shape[-1] == 2:
        pass
    else:
        colorized = output_data[..., :3]
    if output_data.ndim == 3 and output_data.shape[-1] == 3:
        out_a = rgb_to_lab_a(colorized)
        out_b = rgb_to_lab_b(colorized)
    elif output_data.ndim == 3 and output_data.shape[-1] == 2:
        out_a = output_data[..., 0]
        out_b = output_data[..., 1]
    else:
        if colorized.max() <= 1.0:
            colorized = (colorized * 255).astype(np.uint8)
        result = Image.fromarray(colorized).resize((orig_w, orig_h), Image.BILINEAR)
        result.save(output_path)
        return
    out_a_pil = Image.fromarray(out_a.astype(np.float32), mode='F')
    out_b_pil = Image.fromarray(out_b.astype(np.float32), mode='F')
    out_a_resized = out_a_pil.resize((orig_w, orig_h), Image.BILINEAR)
    out_b_resized = out_b_pil.resize((orig_w, orig_h), Image.BILINEAR)
    out_a_arr = np.array(out_a_resized)
    out_b_arr = np.array(out_b_resized)
    result_rgb = lab_to_rgb(orig_L, out_a_arr, out_b_arr)
    result = Image.fromarray(result_rgb)
    result.save(output_path)


def test_cli_mode(images):
    print("\n=== 方式1: CLI 调用（每次子进程，每次重新加载模型）===")
    print(f"图片数量: {len(images)}")
    os.makedirs(OUTPUT_DIR_CLI, exist_ok=True)

    per_image_times = []
    total_start = time.time()

    for i, img_path in enumerate(images):
        out_path = os.path.join(OUTPUT_DIR_CLI, img_path.name)
        t0 = time.time()
        result = subprocess.run(
            [sys.executable, COLORIZE_PY, '-i', str(img_path), '-o', out_path, '-m', MODEL_PATH, '-r', '19'],
            capture_output=True, text=True
        )
        t1 = time.time()
        elapsed = t1 - t0
        per_image_times.append(elapsed)
        size = Image.open(img_path).size
        out_size = Image.open(out_path).size if os.path.exists(out_path) else 'FAILED'

        status = "OK" if result.returncode == 0 and os.path.exists(out_path) else f"FAIL (rc={result.returncode})"
        print(f"  [{i+1}/{len(images)}] {img_path.name} {size[0]}x{size[1]} -> {out_size[0]}x{out_size[1]} | {el#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    L = 116.0 * fy - 16.0
    return L


def rgb_to_lab_a(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    return 500.0 * (fx - fy)


def rgb_to_lab_b(rgb):
    rgb_f = rgb.astype(np.float32)
    return 116.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    return 200.0 * (fy - fz)


def lab_to_rgb(L, a, b):
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
    b = 0.0556434 * X - 0.2040259 * Y + 1.0572252 * Z
    rgb = np.stack([r, g, b], axis=-1)
    rgb = np.clip(rgb, 0, 1)
    mask = rgb <= 0.0031308
    rgb_srgb = np.where(mask, 12.92 * rgb, 1.055 * np.power(np.maximum(rgb, 1e-12), 1.0 / 2.4) - 0.055)
    rgb_srgb = np.clip(rgb_srgb * 255.0, 0, 255).astype(np.uint8)
    return rgb_srgb


def colorize_image_reuse(session, input_name, input_shape, input_path, output_path):
    original = Image.open(input_path).convert('RGB')
    orig_w, orig_h = original.size
    original_np = np.array(original)
    orig_L = rgb_to_lab_l(original_np)
    gray = original.convert('L')
    gray_resized = gray.resize((INFERENCE_SIZE, INFERENCE_SIZE), Image.BILINEAR)
    input_data = np.array(gray_resized, dtype=np.float32) / 255.0
    if len(input_shape) == 4 and input_shape[1] == 3:
        input_data = np.stack([input_data] * 3, axis=0)[np.newaxis, :, :, :]
    else:
        input_data = input_data[np.newaxis, np.newaxis, :, :]
    outputs = session.run(None, {input_name: input_data})
    output_data = outputs[0]
    if output_data.ndim == 4:
        if output_data.shape[1] in (1, 3):
            output_data = np.transpose(output_data[0], (1, 2, 0))
        else:
            output_data = output_data[0]
    output_data = np.squeeze(output_data)
    if output_data.ndim == 2:
        colorized = np.stack([output_data] * 3, axis=-1)
    elif output_data.shape[-1] == 3:
        colorized = output_data
    elif output_data.shape[-1] == 2:
        pass
    else:
        colorized = output_data[..., :3]
    if output_data.ndim == 3 and output_data.shape[-1] == 3:
        out_a = rgb_to_lab_a(colorized)
        out_b = rgb_to_lab_b(colorized)
    elif output_data.ndim == 3 and output_data.shape[-1] == 2:
        out_a = output_data[..., 0]
        out_b = output_data[..., 1]
    else:
        if colorized.max() <= 1.0:
            colorized = (colorized * 255).astype(np.uint8)
        result = Image.fromarray(colorized).resize((orig_w, orig_h), Image.BILINEAR)
        result.save(output_path)
        return
    out_a_pil = Image.fromarray(out_a.astype(np.float32), mode='F')
    out_b_pil = Image.fromarray(out_b.astype(np.float32), mode='F')
    out_a_resized = out_a_pil.resize((orig_w, orig_h), Image.BILINEAR)
    out_b_resized = out_b_pil.resize((orig_w, orig_h), Image.BILINEAR)
    out_a_arr = np.array(out_a_resized)
    out_b_arr = np.array(out_b_resized)
    result_rgb = lab_to_rgb(orig_L, out_a_arr, out_b_arr)
    result = Image.fromarray(result_rgb)
    result.save(output_path)


def test_cli_mode(images):
    print("\n=== 方式1: CLI 调用（每次子进程，每次重新加载模型）===")
    print(f"图片数量: {len(images)}")
    os.makedirs(OUTPUT_DIR_CLI, exist_ok=True)

    per_image_times = []
    total_start = time.time()

    for i, img_path in enumerate(images):
        out_path = os.path.join(OUTPUT_DIR_CLI, img_path.name)
        t0 = time.time()
        result = subprocess.run(
            [sys.executable, COLORIZE_PY, '-i', str(img_path), '-o', out_path, '-m', MODEL_PATH, '-r', '19'],
            capture_output=True, text=True
        )
        t1 = time.time()
        elapsed = t1 - t0
        per_image_times.append(elapsed)
        size = Image.open(img_path).size
        out_size = Image.open(out_path).size if os.path.exists(out_path) else 'FAILED'

        status = "OK" if result.returncode == 0 and os.path.exists(out_path) else f"FAIL (rc={result.returncode})"
        print(f"  [{i+1}/{len(images)}] {img_path.name} {size[0]}x{size[1]} -> {out_size[0]}x{out_size[1]} | {elapsed:.2f}s [{status}]")
        if result.stderr:
            print#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    L = 116.0 * fy - 16.0
    return L


def rgb_to_lab_a(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    return 500.0 * (fx - fy)


def rgb_to_lab_b(rgb):
    rgb_f = rgb.astype(np.float32)
    return 116.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    return 200.0 * (fy - fz)


def lab_to_rgb(L, a, b):
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
    b = 0.0556434 * X - 0.2040259 * Y + 1.0572252 * Z
    rgb = np.stack([r, g, b], axis=-1)
    rgb = np.clip(rgb, 0, 1)
    mask = rgb <= 0.0031308
    rgb_srgb = np.where(mask, 12.92 * rgb, 1.055 * np.power(np.maximum(rgb, 1e-12), 1.0 / 2.4) - 0.055)
    rgb_srgb = np.clip(rgb_srgb * 255.0, 0, 255).astype(np.uint8)
    return rgb_srgb


def colorize_image_reuse(session, input_name, input_shape, input_path, output_path):
    original = Image.open(input_path).convert('RGB')
    orig_w, orig_h = original.size
    original_np = np.array(original)
    orig_L = rgb_to_lab_l(original_np)
    gray = original.convert('L')
    gray_resized = gray.resize((INFERENCE_SIZE, INFERENCE_SIZE), Image.BILINEAR)
    input_data = np.array(gray_resized, dtype=np.float32) / 255.0
    if len(input_shape) == 4 and input_shape[1] == 3:
        input_data = np.stack([input_data] * 3, axis=0)[np.newaxis, :, :, :]
    else:
        input_data = input_data[np.newaxis, np.newaxis, :, :]
    outputs = session.run(None, {input_name: input_data})
    output_data = outputs[0]
    if output_data.ndim == 4:
        if output_data.shape[1] in (1, 3):
            output_data = np.transpose(output_data[0], (1, 2, 0))
        else:
            output_data = output_data[0]
    output_data = np.squeeze(output_data)
    if output_data.ndim == 2:
        colorized = np.stack([output_data] * 3, axis=-1)
    elif output_data.shape[-1] == 3:
        colorized = output_data
    elif output_data.shape[-1] == 2:
        pass
    else:
        colorized = output_data[..., :3]
    if output_data.ndim == 3 and output_data.shape[-1] == 3:
        out_a = rgb_to_lab_a(colorized)
        out_b = rgb_to_lab_b(colorized)
    elif output_data.ndim == 3 and output_data.shape[-1] == 2:
        out_a = output_data[..., 0]
        out_b = output_data[..., 1]
    else:
        if colorized.max() <= 1.0:
            colorized = (colorized * 255).astype(np.uint8)
        result = Image.fromarray(colorized).resize((orig_w, orig_h), Image.BILINEAR)
        result.save(output_path)
        return
    out_a_pil = Image.fromarray(out_a.astype(np.float32), mode='F')
    out_b_pil = Image.fromarray(out_b.astype(np.float32), mode='F')
    out_a_resized = out_a_pil.resize((orig_w, orig_h), Image.BILINEAR)
    out_b_resized = out_b_pil.resize((orig_w, orig_h), Image.BILINEAR)
    out_a_arr = np.array(out_a_resized)
    out_b_arr = np.array(out_b_resized)
    result_rgb = lab_to_rgb(orig_L, out_a_arr, out_b_arr)
    result = Image.fromarray(result_rgb)
    result.save(output_path)


def test_cli_mode(images):
    print("\n=== 方式1: CLI 调用（每次子进程，每次重新加载模型）===")
    print(f"图片数量: {len(images)}")
    os.makedirs(OUTPUT_DIR_CLI, exist_ok=True)

    per_image_times = []
    total_start = time.time()

    for i, img_path in enumerate(images):
        out_path = os.path.join(OUTPUT_DIR_CLI, img_path.name)
        t0 = time.time()
        result = subprocess.run(
            [sys.executable, COLORIZE_PY, '-i', str(img_path), '-o', out_path, '-m', MODEL_PATH, '-r', '19'],
            capture_output=True, text=True
        )
        t1 = time.time()
        elapsed = t1 - t0
        per_image_times.append(elapsed)
        size = Image.open(img_path).size
        out_size = Image.open(out_path).size if os.path.exists(out_path) else 'FAILED'

        status = "OK" if result.returncode == 0 and os.path.exists(out_path) else f"FAIL (rc={result.returncode})"
        print(f"  [{i+1}/{len(images)}] {img_path.name} {size[0]}x{size[1]} -> {out_size[0]}x{out_size[1]} | {elapsed:.2f}s [{status}]")
        if result.stderr:
            print(f"      stderr: {result.stderr.strip#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    L = 116.0 * fy - 16.0
    return L


def rgb_to_lab_a(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    return 500.0 * (fx - fy)


def rgb_to_lab_b(rgb):
    rgb_f = rgb.astype(np.float32)
    return 116.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    return 200.0 * (fy - fz)


def lab_to_rgb(L, a, b):
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
    b = 0.0556434 * X - 0.2040259 * Y + 1.0572252 * Z
    rgb = np.stack([r, g, b], axis=-1)
    rgb = np.clip(rgb, 0, 1)
    mask = rgb <= 0.0031308
    rgb_srgb = np.where(mask, 12.92 * rgb, 1.055 * np.power(np.maximum(rgb, 1e-12), 1.0 / 2.4) - 0.055)
    rgb_srgb = np.clip(rgb_srgb * 255.0, 0, 255).astype(np.uint8)
    return rgb_srgb


def colorize_image_reuse(session, input_name, input_shape, input_path, output_path):
    original = Image.open(input_path).convert('RGB')
    orig_w, orig_h = original.size
    original_np = np.array(original)
    orig_L = rgb_to_lab_l(original_np)
    gray = original.convert('L')
    gray_resized = gray.resize((INFERENCE_SIZE, INFERENCE_SIZE), Image.BILINEAR)
    input_data = np.array(gray_resized, dtype=np.float32) / 255.0
    if len(input_shape) == 4 and input_shape[1] == 3:
        input_data = np.stack([input_data] * 3, axis=0)[np.newaxis, :, :, :]
    else:
        input_data = input_data[np.newaxis, np.newaxis, :, :]
    outputs = session.run(None, {input_name: input_data})
    output_data = outputs[0]
    if output_data.ndim == 4:
        if output_data.shape[1] in (1, 3):
            output_data = np.transpose(output_data[0], (1, 2, 0))
        else:
            output_data = output_data[0]
    output_data = np.squeeze(output_data)
    if output_data.ndim == 2:
        colorized = np.stack([output_data] * 3, axis=-1)
    elif output_data.shape[-1] == 3:
        colorized = output_data
    elif output_data.shape[-1] == 2:
        pass
    else:
        colorized = output_data[..., :3]
    if output_data.ndim == 3 and output_data.shape[-1] == 3:
        out_a = rgb_to_lab_a(colorized)
        out_b = rgb_to_lab_b(colorized)
    elif output_data.ndim == 3 and output_data.shape[-1] == 2:
        out_a = output_data[..., 0]
        out_b = output_data[..., 1]
    else:
        if colorized.max() <= 1.0:
            colorized = (colorized * 255).astype(np.uint8)
        result = Image.fromarray(colorized).resize((orig_w, orig_h), Image.BILINEAR)
        result.save(output_path)
        return
    out_a_pil = Image.fromarray(out_a.astype(np.float32), mode='F')
    out_b_pil = Image.fromarray(out_b.astype(np.float32), mode='F')
    out_a_resized = out_a_pil.resize((orig_w, orig_h), Image.BILINEAR)
    out_b_resized = out_b_pil.resize((orig_w, orig_h), Image.BILINEAR)
    out_a_arr = np.array(out_a_resized)
    out_b_arr = np.array(out_b_resized)
    result_rgb = lab_to_rgb(orig_L, out_a_arr, out_b_arr)
    result = Image.fromarray(result_rgb)
    result.save(output_path)


def test_cli_mode(images):
    print("\n=== 方式1: CLI 调用（每次子进程，每次重新加载模型）===")
    print(f"图片数量: {len(images)}")
    os.makedirs(OUTPUT_DIR_CLI, exist_ok=True)

    per_image_times = []
    total_start = time.time()

    for i, img_path in enumerate(images):
        out_path = os.path.join(OUTPUT_DIR_CLI, img_path.name)
        t0 = time.time()
        result = subprocess.run(
            [sys.executable, COLORIZE_PY, '-i', str(img_path), '-o', out_path, '-m', MODEL_PATH, '-r', '19'],
            capture_output=True, text=True
        )
        t1 = time.time()
        elapsed = t1 - t0
        per_image_times.append(elapsed)
        size = Image.open(img_path).size
        out_size = Image.open(out_path).size if os.path.exists(out_path) else 'FAILED'

        status = "OK" if result.returncode == 0 and os.path.exists(out_path) else f"FAIL (rc={result.returncode})"
        print(f"  [{i+1}/{len(images)}] {img_path.name} {size[0]}x{size[1]} -> {out_size[0]}x{out_size[1]} | {elapsed:.2f}s [{status}]")
        if result.stderr:
            print(f"      stderr: {result.stderr.strip()}")

    total_time = time.time()#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    L = 116.0 * fy - 16.0
    return L


def rgb_to_lab_a(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    return 500.0 * (fx - fy)


def rgb_to_lab_b(rgb):
    rgb_f = rgb.astype(np.float32)
    return 116.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    return 200.0 * (fy - fz)


def lab_to_rgb(L, a, b):
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
    b = 0.0556434 * X - 0.2040259 * Y + 1.0572252 * Z
    rgb = np.stack([r, g, b], axis=-1)
    rgb = np.clip(rgb, 0, 1)
    mask = rgb <= 0.0031308
    rgb_srgb = np.where(mask, 12.92 * rgb, 1.055 * np.power(np.maximum(rgb, 1e-12), 1.0 / 2.4) - 0.055)
    rgb_srgb = np.clip(rgb_srgb * 255.0, 0, 255).astype(np.uint8)
    return rgb_srgb


def colorize_image_reuse(session, input_name, input_shape, input_path, output_path):
    original = Image.open(input_path).convert('RGB')
    orig_w, orig_h = original.size
    original_np = np.array(original)
    orig_L = rgb_to_lab_l(original_np)
    gray = original.convert('L')
    gray_resized = gray.resize((INFERENCE_SIZE, INFERENCE_SIZE), Image.BILINEAR)
    input_data = np.array(gray_resized, dtype=np.float32) / 255.0
    if len(input_shape) == 4 and input_shape[1] == 3:
        input_data = np.stack([input_data] * 3, axis=0)[np.newaxis, :, :, :]
    else:
        input_data = input_data[np.newaxis, np.newaxis, :, :]
    outputs = session.run(None, {input_name: input_data})
    output_data = outputs[0]
    if output_data.ndim == 4:
        if output_data.shape[1] in (1, 3):
            output_data = np.transpose(output_data[0], (1, 2, 0))
        else:
            output_data = output_data[0]
    output_data = np.squeeze(output_data)
    if output_data.ndim == 2:
        colorized = np.stack([output_data] * 3, axis=-1)
    elif output_data.shape[-1] == 3:
        colorized = output_data
    elif output_data.shape[-1] == 2:
        pass
    else:
        colorized = output_data[..., :3]
    if output_data.ndim == 3 and output_data.shape[-1] == 3:
        out_a = rgb_to_lab_a(colorized)
        out_b = rgb_to_lab_b(colorized)
    elif output_data.ndim == 3 and output_data.shape[-1] == 2:
        out_a = output_data[..., 0]
        out_b = output_data[..., 1]
    else:
        if colorized.max() <= 1.0:
            colorized = (colorized * 255).astype(np.uint8)
        result = Image.fromarray(colorized).resize((orig_w, orig_h), Image.BILINEAR)
        result.save(output_path)
        return
    out_a_pil = Image.fromarray(out_a.astype(np.float32), mode='F')
    out_b_pil = Image.fromarray(out_b.astype(np.float32), mode='F')
    out_a_resized = out_a_pil.resize((orig_w, orig_h), Image.BILINEAR)
    out_b_resized = out_b_pil.resize((orig_w, orig_h), Image.BILINEAR)
    out_a_arr = np.array(out_a_resized)
    out_b_arr = np.array(out_b_resized)
    result_rgb = lab_to_rgb(orig_L, out_a_arr, out_b_arr)
    result = Image.fromarray(result_rgb)
    result.save(output_path)


def test_cli_mode(images):
    print("\n=== 方式1: CLI 调用（每次子进程，每次重新加载模型）===")
    print(f"图片数量: {len(images)}")
    os.makedirs(OUTPUT_DIR_CLI, exist_ok=True)

    per_image_times = []
    total_start = time.time()

    for i, img_path in enumerate(images):
        out_path = os.path.join(OUTPUT_DIR_CLI, img_path.name)
        t0 = time.time()
        result = subprocess.run(
            [sys.executable, COLORIZE_PY, '-i', str(img_path), '-o', out_path, '-m', MODEL_PATH, '-r', '19'],
            capture_output=True, text=True
        )
        t1 = time.time()
        elapsed = t1 - t0
        per_image_times.append(elapsed)
        size = Image.open(img_path).size
        out_size = Image.open(out_path).size if os.path.exists(out_path) else 'FAILED'

        status = "OK" if result.returncode == 0 and os.path.exists(out_path) else f"FAIL (rc={result.returncode})"
        print(f"  [{i+1}/{len(images)}] {img_path.name} {size[0]}x{size[1]} -> {out_size[0]}x{out_size[1]} | {elapsed:.2f}s [{status}]")
        if result.stderr:
            print(f"      stderr: {result.stderr.strip()}")

    total_time = time.time() - total_start
    print(f"\n#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    L = 116.0 * fy - 16.0
    return L


def rgb_to_lab_a(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    return 500.0 * (fx - fy)


def rgb_to_lab_b(rgb):
    rgb_f = rgb.astype(np.float32)
    return 116.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    return 200.0 * (fy - fz)


def lab_to_rgb(L, a, b):
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
    b = 0.0556434 * X - 0.2040259 * Y + 1.0572252 * Z
    rgb = np.stack([r, g, b], axis=-1)
    rgb = np.clip(rgb, 0, 1)
    mask = rgb <= 0.0031308
    rgb_srgb = np.where(mask, 12.92 * rgb, 1.055 * np.power(np.maximum(rgb, 1e-12), 1.0 / 2.4) - 0.055)
    rgb_srgb = np.clip(rgb_srgb * 255.0, 0, 255).astype(np.uint8)
    return rgb_srgb


def colorize_image_reuse(session, input_name, input_shape, input_path, output_path):
    original = Image.open(input_path).convert('RGB')
    orig_w, orig_h = original.size
    original_np = np.array(original)
    orig_L = rgb_to_lab_l(original_np)
    gray = original.convert('L')
    gray_resized = gray.resize((INFERENCE_SIZE, INFERENCE_SIZE), Image.BILINEAR)
    input_data = np.array(gray_resized, dtype=np.float32) / 255.0
    if len(input_shape) == 4 and input_shape[1] == 3:
        input_data = np.stack([input_data] * 3, axis=0)[np.newaxis, :, :, :]
    else:
        input_data = input_data[np.newaxis, np.newaxis, :, :]
    outputs = session.run(None, {input_name: input_data})
    output_data = outputs[0]
    if output_data.ndim == 4:
        if output_data.shape[1] in (1, 3):
            output_data = np.transpose(output_data[0], (1, 2, 0))
        else:
            output_data = output_data[0]
    output_data = np.squeeze(output_data)
    if output_data.ndim == 2:
        colorized = np.stack([output_data] * 3, axis=-1)
    elif output_data.shape[-1] == 3:
        colorized = output_data
    elif output_data.shape[-1] == 2:
        pass
    else:
        colorized = output_data[..., :3]
    if output_data.ndim == 3 and output_data.shape[-1] == 3:
        out_a = rgb_to_lab_a(colorized)
        out_b = rgb_to_lab_b(colorized)
    elif output_data.ndim == 3 and output_data.shape[-1] == 2:
        out_a = output_data[..., 0]
        out_b = output_data[..., 1]
    else:
        if colorized.max() <= 1.0:
            colorized = (colorized * 255).astype(np.uint8)
        result = Image.fromarray(colorized).resize((orig_w, orig_h), Image.BILINEAR)
        result.save(output_path)
        return
    out_a_pil = Image.fromarray(out_a.astype(np.float32), mode='F')
    out_b_pil = Image.fromarray(out_b.astype(np.float32), mode='F')
    out_a_resized = out_a_pil.resize((orig_w, orig_h), Image.BILINEAR)
    out_b_resized = out_b_pil.resize((orig_w, orig_h), Image.BILINEAR)
    out_a_arr = np.array(out_a_resized)
    out_b_arr = np.array(out_b_resized)
    result_rgb = lab_to_rgb(orig_L, out_a_arr, out_b_arr)
    result = Image.fromarray(result_rgb)
    result.save(output_path)


def test_cli_mode(images):
    print("\n=== 方式1: CLI 调用（每次子进程，每次重新加载模型）===")
    print(f"图片数量: {len(images)}")
    os.makedirs(OUTPUT_DIR_CLI, exist_ok=True)

    per_image_times = []
    total_start = time.time()

    for i, img_path in enumerate(images):
        out_path = os.path.join(OUTPUT_DIR_CLI, img_path.name)
        t0 = time.time()
        result = subprocess.run(
            [sys.executable, COLORIZE_PY, '-i', str(img_path), '-o', out_path, '-m', MODEL_PATH, '-r', '19'],
            capture_output=True, text=True
        )
        t1 = time.time()
        elapsed = t1 - t0
        per_image_times.append(elapsed)
        size = Image.open(img_path).size
        out_size = Image.open(out_path).size if os.path.exists(out_path) else 'FAILED'

        status = "OK" if result.returncode == 0 and os.path.exists(out_path) else f"FAIL (rc={result.returncode})"
        print(f"  [{i+1}/{len(images)}] {img_path.name} {size[0]}x{size[1]} -> {out_size[0]}x{out_size[1]} | {elapsed:.2f}s [{status}]")
        if result.stderr:
            print(f"      stderr: {result.stderr.strip()}")

    total_time = time.time() - total_start
    print(f"\n  CLI 总耗时: {total_time:.2f}s")
    print(f"#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    L = 116.0 * fy - 16.0
    return L


def rgb_to_lab_a(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    return 500.0 * (fx - fy)


def rgb_to_lab_b(rgb):
    rgb_f = rgb.astype(np.float32)
    return 116.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    return 200.0 * (fy - fz)


def lab_to_rgb(L, a, b):
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
    b = 0.0556434 * X - 0.2040259 * Y + 1.0572252 * Z
    rgb = np.stack([r, g, b], axis=-1)
    rgb = np.clip(rgb, 0, 1)
    mask = rgb <= 0.0031308
    rgb_srgb = np.where(mask, 12.92 * rgb, 1.055 * np.power(np.maximum(rgb, 1e-12), 1.0 / 2.4) - 0.055)
    rgb_srgb = np.clip(rgb_srgb * 255.0, 0, 255).astype(np.uint8)
    return rgb_srgb


def colorize_image_reuse(session, input_name, input_shape, input_path, output_path):
    original = Image.open(input_path).convert('RGB')
    orig_w, orig_h = original.size
    original_np = np.array(original)
    orig_L = rgb_to_lab_l(original_np)
    gray = original.convert('L')
    gray_resized = gray.resize((INFERENCE_SIZE, INFERENCE_SIZE), Image.BILINEAR)
    input_data = np.array(gray_resized, dtype=np.float32) / 255.0
    if len(input_shape) == 4 and input_shape[1] == 3:
        input_data = np.stack([input_data] * 3, axis=0)[np.newaxis, :, :, :]
    else:
        input_data = input_data[np.newaxis, np.newaxis, :, :]
    outputs = session.run(None, {input_name: input_data})
    output_data = outputs[0]
    if output_data.ndim == 4:
        if output_data.shape[1] in (1, 3):
            output_data = np.transpose(output_data[0], (1, 2, 0))
        else:
            output_data = output_data[0]
    output_data = np.squeeze(output_data)
    if output_data.ndim == 2:
        colorized = np.stack([output_data] * 3, axis=-1)
    elif output_data.shape[-1] == 3:
        colorized = output_data
    elif output_data.shape[-1] == 2:
        pass
    else:
        colorized = output_data[..., :3]
    if output_data.ndim == 3 and output_data.shape[-1] == 3:
        out_a = rgb_to_lab_a(colorized)
        out_b = rgb_to_lab_b(colorized)
    elif output_data.ndim == 3 and output_data.shape[-1] == 2:
        out_a = output_data[..., 0]
        out_b = output_data[..., 1]
    else:
        if colorized.max() <= 1.0:
            colorized = (colorized * 255).astype(np.uint8)
        result = Image.fromarray(colorized).resize((orig_w, orig_h), Image.BILINEAR)
        result.save(output_path)
        return
    out_a_pil = Image.fromarray(out_a.astype(np.float32), mode='F')
    out_b_pil = Image.fromarray(out_b.astype(np.float32), mode='F')
    out_a_resized = out_a_pil.resize((orig_w, orig_h), Image.BILINEAR)
    out_b_resized = out_b_pil.resize((orig_w, orig_h), Image.BILINEAR)
    out_a_arr = np.array(out_a_resized)
    out_b_arr = np.array(out_b_resized)
    result_rgb = lab_to_rgb(orig_L, out_a_arr, out_b_arr)
    result = Image.fromarray(result_rgb)
    result.save(output_path)


def test_cli_mode(images):
    print("\n=== 方式1: CLI 调用（每次子进程，每次重新加载模型）===")
    print(f"图片数量: {len(images)}")
    os.makedirs(OUTPUT_DIR_CLI, exist_ok=True)

    per_image_times = []
    total_start = time.time()

    for i, img_path in enumerate(images):
        out_path = os.path.join(OUTPUT_DIR_CLI, img_path.name)
        t0 = time.time()
        result = subprocess.run(
            [sys.executable, COLORIZE_PY, '-i', str(img_path), '-o', out_path, '-m', MODEL_PATH, '-r', '19'],
            capture_output=True, text=True
        )
        t1 = time.time()
        elapsed = t1 - t0
        per_image_times.append(elapsed)
        size = Image.open(img_path).size
        out_size = Image.open(out_path).size if os.path.exists(out_path) else 'FAILED'

        status = "OK" if result.returncode == 0 and os.path.exists(out_path) else f"FAIL (rc={result.returncode})"
        print(f"  [{i+1}/{len(images)}] {img_path.name} {size[0]}x{size[1]} -> {out_size[0]}x{out_size[1]} | {elapsed:.2f}s [{status}]")
        if result.stderr:
            print(f"      stderr: {result.stderr.strip()}")

    total_time = time.time() - total_start
    print(f"\n  CLI 总耗时: {total_time:.2f}s")
    print(f"  单张平均: {np.mean(per#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    L = 116.0 * fy - 16.0
    return L


def rgb_to_lab_a(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    return 500.0 * (fx - fy)


def rgb_to_lab_b(rgb):
    rgb_f = rgb.astype(np.float32)
    return 116.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    return 200.0 * (fy - fz)


def lab_to_rgb(L, a, b):
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
    b = 0.0556434 * X - 0.2040259 * Y + 1.0572252 * Z
    rgb = np.stack([r, g, b], axis=-1)
    rgb = np.clip(rgb, 0, 1)
    mask = rgb <= 0.0031308
    rgb_srgb = np.where(mask, 12.92 * rgb, 1.055 * np.power(np.maximum(rgb, 1e-12), 1.0 / 2.4) - 0.055)
    rgb_srgb = np.clip(rgb_srgb * 255.0, 0, 255).astype(np.uint8)
    return rgb_srgb


def colorize_image_reuse(session, input_name, input_shape, input_path, output_path):
    original = Image.open(input_path).convert('RGB')
    orig_w, orig_h = original.size
    original_np = np.array(original)
    orig_L = rgb_to_lab_l(original_np)
    gray = original.convert('L')
    gray_resized = gray.resize((INFERENCE_SIZE, INFERENCE_SIZE), Image.BILINEAR)
    input_data = np.array(gray_resized, dtype=np.float32) / 255.0
    if len(input_shape) == 4 and input_shape[1] == 3:
        input_data = np.stack([input_data] * 3, axis=0)[np.newaxis, :, :, :]
    else:
        input_data = input_data[np.newaxis, np.newaxis, :, :]
    outputs = session.run(None, {input_name: input_data})
    output_data = outputs[0]
    if output_data.ndim == 4:
        if output_data.shape[1] in (1, 3):
            output_data = np.transpose(output_data[0], (1, 2, 0))
        else:
            output_data = output_data[0]
    output_data = np.squeeze(output_data)
    if output_data.ndim == 2:
        colorized = np.stack([output_data] * 3, axis=-1)
    elif output_data.shape[-1] == 3:
        colorized = output_data
    elif output_data.shape[-1] == 2:
        pass
    else:
        colorized = output_data[..., :3]
    if output_data.ndim == 3 and output_data.shape[-1] == 3:
        out_a = rgb_to_lab_a(colorized)
        out_b = rgb_to_lab_b(colorized)
    elif output_data.ndim == 3 and output_data.shape[-1] == 2:
        out_a = output_data[..., 0]
        out_b = output_data[..., 1]
    else:
        if colorized.max() <= 1.0:
            colorized = (colorized * 255).astype(np.uint8)
        result = Image.fromarray(colorized).resize((orig_w, orig_h), Image.BILINEAR)
        result.save(output_path)
        return
    out_a_pil = Image.fromarray(out_a.astype(np.float32), mode='F')
    out_b_pil = Image.fromarray(out_b.astype(np.float32), mode='F')
    out_a_resized = out_a_pil.resize((orig_w, orig_h), Image.BILINEAR)
    out_b_resized = out_b_pil.resize((orig_w, orig_h), Image.BILINEAR)
    out_a_arr = np.array(out_a_resized)
    out_b_arr = np.array(out_b_resized)
    result_rgb = lab_to_rgb(orig_L, out_a_arr, out_b_arr)
    result = Image.fromarray(result_rgb)
    result.save(output_path)


def test_cli_mode(images):
    print("\n=== 方式1: CLI 调用（每次子进程，每次重新加载模型）===")
    print(f"图片数量: {len(images)}")
    os.makedirs(OUTPUT_DIR_CLI, exist_ok=True)

    per_image_times = []
    total_start = time.time()

    for i, img_path in enumerate(images):
        out_path = os.path.join(OUTPUT_DIR_CLI, img_path.name)
        t0 = time.time()
        result = subprocess.run(
            [sys.executable, COLORIZE_PY, '-i', str(img_path), '-o', out_path, '-m', MODEL_PATH, '-r', '19'],
            capture_output=True, text=True
        )
        t1 = time.time()
        elapsed = t1 - t0
        per_image_times.append(elapsed)
        size = Image.open(img_path).size
        out_size = Image.open(out_path).size if os.path.exists(out_path) else 'FAILED'

        status = "OK" if result.returncode == 0 and os.path.exists(out_path) else f"FAIL (rc={result.returncode})"
        print(f"  [{i+1}/{len(images)}] {img_path.name} {size[0]}x{size[1]} -> {out_size[0]}x{out_size[1]} | {elapsed:.2f}s [{status}]")
        if result.stderr:
            print(f"      stderr: {result.stderr.strip()}")

    total_time = time.time() - total_start
    print(f"\n  CLI 总耗时: {total_time:.2f}s")
    print(f"  单张平均: {np.mean(per_image_times):.2f}s")
    print(f"  单张最慢:#!/usr/bin/env python3
"""
批量上色测试：模拟 App 集成测试

测试：
1. 当前 App 调用方式：每次 subprocess 调用 colorize.py（每次加载模型）
2. 优化方式：单进程内复用 InferenceSession
"""
import sys
import os
import time
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
import onnxruntime as ort

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

INFERENCE_SIZE = 256
MODEL_PATH = "/workspace/colorization_test/test_colorize_models/deoldify_artistic.onnx"
INPUT_DIR = "/workspace/colorization_test/batch_input"
OUTPUT_DIR_CLI = "/workspace/colorization_test/batch_output/cli"
OUTPUT_DIR_OPT = "/workspace/colorization_test/batch_output/optimized"
COLORIZE_PY = "/workspace/assets/colorize/colorize.py"


def list_images(d):
    return sorted([p for p in Path(d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg')])


def rgb_to_lab_l(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    L = 116.0 * fy - 16.0
    return L


def rgb_to_lab_a(rgb):
    rgb_f = rgb.astype(np.float32) / 255.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fx = np.cbrt(np.clip(x / xn, 0, None))
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fx = np.where(x / xn > eps, fx, (k * (x / xn) + 16.0) / 116.0)
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    return 500.0 * (fx - fy)


def rgb_to_lab_b(rgb):
    rgb_f = rgb.astype(np.float32)
    return 116.0
    mask = rgb_f <= 0.04045
    rgb_linear = np.where(mask, rgb_f / 12.92, ((rgb_f + 0.055) / 1.055) ** 2.4)
    x = 0.4124564 * rgb_linear[..., 0] + 0.3575761 * rgb_linear[..., 1] + 0.1804375 * rgb_linear[..., 2]
    y = 0.2126729 * rgb_linear[..., 0] + 0.7151522 * rgb_linear[..., 1] + 0.0721750 * rgb_linear[..., 2]
    z = 0.0193339 * rgb_linear[..., 0] + 0.1191920 * rgb_linear[..., 1] + 1.0572252 * rgb_linear[..., 2]
    xn, yn, zn = 0.95047, 1.0, 1.08883
    fy = np.cbrt(np.clip(y / yn, 0, None))
    fz = np.cbrt(np.clip(z / zn, 0, None))
    eps = 216.0 / 24389.0
    k = 24389.0 / 27.0
    fy = np.where(y / yn > eps, fy, (k * (y / yn) + 16.0) / 116.0)
    fz = np.where(z / zn > eps, fz, (k * (z / zn) + 16.0) / 116.0)
    return 200.0 * (fy - fz)


def lab_to_rgb(L, a, b):
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
    b = 0.0556434 * X - 0.2040259 * Y + 1.0572252 * Z
    rgb = np.stack([r, g, b], axis=-1)
    rgb = np.clip(rgb, 0, 1)
    mask = rgb <= 0.0031308
    rgb_srgb = np.where(mask, 12.92 * rgb, 1.055 * np.power(np.maximum(rgb, 1e-12), 1.0 / 2.4) - 0.055)
    rgb_srgb = np.clip(rgb_srgb * 255.0, 0, 255).astype(np.uint8)
    return rgb_srgb


def colorize_image_reuse(session, input_name, input_shape, input_path, output_path):
    original = Image.open(input_path).convert('RGB')
    orig_w, orig_h = original.size
    original_np = np.array(original)
    orig_L = rgb_to_lab_l(original_np)
    gray = original.convert('L')
    gray_resized = gray.resize((INFERENCE_SIZE, INFERENCE_SIZE), Image.BILINEAR)
    input_data = np.array(gray_resized, dtype=np.float32) / 255.0
    if len(input_shape) == 4 and input_shape[1] == 3:
        input_data = np.stack([input_data] * 3, axis=0)[np.newaxis, :, :, :]
    else:
        input_data = input_data[np.newaxis, np.newaxis, :, :]
    outputs = session.run(None, {input_name: input_data})
    output_data = outputs[0]
    if output_data.ndim == 4:
        if output_data.shape[1] in (1, 3):
            output_data = np.transpose(output_data[0], (1, 2, 0))
        else:
            output_data = output_data[0]
    output_data = np.squeeze(output_data)
    if output_data.ndim == 2:
        colorized = np.stack([output_data] * 3, axis=-1)
    elif output_data.shape[-1] == 3:
        colorized = output_data
    elif output_data.shape[-1] == 2:
        pass
    else:
        colorized = output_data[..., :3]
    if output_data.ndim == 3 and output_data.shape[-1] == 3:
        out_a = rgb_to_lab_a(colorized)
        out_b = rgb_to_lab_b(colorized)
    elif output_data.ndim == 3 and output_data.shape[-1] == 2:
        out_a = output_data[..., 0]
        out_b = output_data[..., 1]
    else:
        if colorized.max() <= 1.0:
            colorized = (colorized * 255).astype(np.uint8)
        result = Image.fromarray(colorized).resize((orig_w, orig_h), Image.BILINEAR)
        result.save(output_path)
        return
    out_a_pil = Image.fromarray(out_a.astype(np.float32), mode='F')
    out_b_pil = Image.fromarray(out_b.astype(np.float32), mode='F')
    out_a_resized = out_a_pil.resize((orig_w, orig_h), Image.BILINEAR)
    out_b_resized = out_b_pil.resize((orig_w, orig_h), Image.BILINEAR)
    out_a_arr = np.array(out_a_resized)
    out_b_arr = np.array(out_b_resized)
    result_rgb = lab_to_rgb(orig_L, out_a_arr, out_b_arr)
    result = Image.fromarray(result_rgb)
    result.save(output_path)


def test_cli_mode(images):
    print("\n=== 方式1: CLI 调用（每次子进程，每次重新加载模型）===")
    print(f"图片数量: {len(images)}")
    os.makedirs(OUTPUT_DIR_CLI, exist_ok=True)

    per_image_times = []
    total_start = time.time()

    for i, img_path in enumerate(images):
        out_path = os.path.join(OUTPUT_DIR_CLI, img_path.name)
        t0 = time.time()
        result = subprocess.run(
            [sys.executable, COLORIZE_PY, '-i', str(img_path), '-o', out_path, '-m', MODEL_PATH, '-r', '19'],
            capture_output=True, text=True
        )
        t1 = time.time()
        elapsed = t1 - t0
        per_image_times.append(elapsed)
        size = Image.open(img_path).size
        out_size = Image.open(out_path).size if os.path.exists(out_path) else 'FAILED'

        status = "OK" if result.returncode == 0 and os.path.exists(out_path) else f"FAIL (rc={result.returncode})"
        print(f"  [{i+1}/{len(images)}] {img_path.name} {size[0]}x{size[1]} -> {out_size[0]}x{out_size[1]} | {elapsed:.2f}s [{status}]")
        if result.stderr:
            print(f"      stderr: {result.stderr.strip()}")

    total_time = time.time() - total_start
    print(f"\n  CLI 总耗时: {total_time:.2f}s")
    print(f"  单张平均: {np.mean(per_image_times):.2f}s")
    print(f"  单张最慢: {np.max(per_image_times):.2f}s")
    print(f"