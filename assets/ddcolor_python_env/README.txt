DDColor Python Environment for JHenTai (Windows x64)
=====================================================

This package contains an embeddable Python 3.11.9 environment with all
Python dependencies required by the DDColor colorization feature:
  - onnxruntime-gpu (GPU accelerated, falls back to CPU if no GPU)
  - numpy
  - Pillow
  - opencv-python
  - flatbuffers, packaging, protobuf (transitive deps)

IMPORTANT - Installation Directory:
  All dependencies are installed INSIDE the Python extraction directory
  at: <extracted folder>\python\Lib\site-packages\
  NOTHING is written to C:\Users\<yourname>\ or the system registry.

How to use
----------
1. Unzip this archive anywhere on your Windows PC, e.g.
      D:\Tools\python_env\

2. Double-click "install.bat" and wait for the installation to finish.
   It will install pip, offline wheels, and onnxruntime-gpu into:
      D:\Tools\python_env\python\Lib\site-packages\

3. After installation, open JHenTai -> Settings -> Colorization.
   Set the "Python Path" to:
      D:\Tools\python_env\python\python.exe
   (adjust the drive/path to match where you extracted the archive)

4. Download the DDColor ONNX model file and set the "Model Directory".

5. Restart JHenTai if it was already running, then use the colorize button.

Notes
-----
- This package is for Windows 64-bit only.
- Internet connection IS required during "install.bat" because
  onnxruntime-gpu and opencv-python are downloaded from PyPI.
- onnxruntime-gpu requires NVIDIA GPU drivers and CUDA toolkit.
  If no GPU is available, it will fall back to CPU automatically.
- To completely remove: just delete the python_env folder.
