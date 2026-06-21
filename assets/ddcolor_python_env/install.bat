@echo off
chcp 65001 >nul
title DDColor Python Environment Installer
echo ===========================================
echo  DDColor Python Environment Installer
echo  (GPU accelerated with onnxruntime-gpu)
echo ===========================================
echo.

set "HERE=%~dp0"
set "PYTHON=%HERE%python\python.exe"
set "SITE=%HERE%python\Lib\site-packages"
set "WHEELS=%HERE%wheels"

if not exist "%PYTHON%" (
    echo [ERROR] Python executable not found at: %PYTHON%
    echo Please do not move python folder.
    pause
    exit /b 1
)

mkdir "%SITE%" 2>nul

echo [1/6] Installing pip into Python directory...
"%PYTHON%" "%HERE%python\get-pip.py" --no-warn-script-location --target="%SITE%"
if errorlevel 1 (
    echo [ERROR] pip installation failed.
    pause
    exit /b 1
)

echo.
echo [2/6] Installing offline wheels (numpy, Pillow) into Python directory...
"%PYTHON%" -m pip install --no-index --find-links="%WHEELS%" --target="%SITE%" --no-warn-script-location numpy Pillow
if errorlevel 1 (
    echo [ERROR] Wheel installation failed.
    pause
    exit /b 1
)

echo.
echo [3/6] Installing opencv-python from internet...
"%PYTHON%" -m pip install --target="%SITE%" --no-warn-script-location opencv-python
if errorlevel 1 (
    echo [ERROR] opencv-python installation failed.
    pause
    exit /b 1
)

echo.
echo [4/6] Installing onnxruntime-gpu from internet...
echo (This replaces the CPU-only onnxruntime with GPU support)
"%PYTHON%" -m pip install --target="%SITE%" --no-warn-script-location onnxruntime-gpu
if errorlevel 1 (
    echo [ERROR] onnxruntime-gpu installation failed.
    echo Make sure you have NVIDIA GPU drivers installed.
    echo Falling back to CPU-only onnxruntime...
    "%PYTHON%" -m pip install --no-index --find-links="%WHEELS%" --target="%SITE%" --no-warn-script-location onnxruntime
    if errorlevel 1 (
        echo [ERROR] Fallback onnxruntime installation also failed.
        pause
        exit /b 1
    )
)

echo.
echo [5/6] Installing transitive dependencies (flatbuffers, packaging, protobuf) from offline wheels...
"%PYTHON%" -m pip install --no-index --find-links="%WHEELS%" --target="%SITE%" --no-warn-script-location flatbuffers packaging protobuf
if errorlevel 1 (
    echo [WARNING] Some transitive dependencies may not have installed, but this is usually harmless.
)

echo.
echo [6/6] Verifying environment...
"%PYTHON%" -c "import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(sys.executable), 'Lib', 'site-packages')); import onnxruntime, numpy, PIL, cv2; print('All modules OK'); print('Available providers:', onnxruntime.get_available_providers())"
if errorlevel 1 (
    echo [ERROR] Environment verification failed.
    pause
    exit /b 1
)

echo.
echo ===========================================
echo  Installation completed successfully!
echo ===========================================
echo.
echo All packages installed inside:
echo   %SITE%
echo.
echo Please set Python path in JHenTai:
echo   %PYTHON%
echo.
echo Model directory still needs to be configured manually.
echo.
echo NOTE: onnxruntime-gpu requires NVIDIA GPU drivers and CUDA toolkit.
echo If no GPU is available, it will fall back to CPU automatically.
echo.
pause
