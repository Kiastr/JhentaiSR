This directory should contain the DeOldify.NET executable and model files for AI image colorization.

How to set up:

1. Build deoldify.exe from the DeOldify.NET project (https://github.com/ColorfulSoft/DeOldify.NET)
   and place it in this directory.

2. Download model files from:
   https://github.com/ColorfulSoft/DeOldify.NET/releases/download/Weights

3. Place the model files in a subdirectory called "models":
   - models/ColorizeArtistic_gen.model
   - models/ColorizeStable_gen.model

Example directory structure:
  windows/deoldify/
    deoldify.exe
    models/
      ColorizeArtistic_gen.model
      ColorizeStable_gen.model

4. In the application, go to Settings > Advanced > DeOldify and set the model directory path
   to the directory containing the model files.
