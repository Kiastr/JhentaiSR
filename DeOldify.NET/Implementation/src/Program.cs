//*************************************************************************************************
//* (C) ColorfulSoft corp., 2021 - 2022. All Rights reserved.
//*************************************************************************************************

using System;
using System.IO;
using System.Drawing;
using System.Windows.Forms;

namespace ColorfulSoft.DeOldify
{

    /// <summary>
    /// Main class.
    /// </summary>
    public static class Program
    {

        /// <summary>
        /// Entry point.
        /// </summary>
        [STAThread]
        public static void Main(string[] args)
        {
            // Command line mode: deoldify.exe <input> <output> <modelType> [modelDirectory]
            if (args.Length >= 3)
            {
                try
                {
                    string modelType = args[2]; // "stable" or "artistic"
                    string modelDirectory = args.Length >= 4 ? args[3] : "";

                    Console.Out.WriteLine("DeOldify CLI: modelType=" + modelType + ", modelDirectory=" + modelDirectory);

                    // Try to find model file in the specified directory
                    string modelPath = null;
                    if(!string.IsNullOrEmpty(modelDirectory))
                    {
                        // Search in the directory itself and all subdirectories
                        string[] searchPaths = new string[] { modelDirectory, Path.Combine(modelDirectory, "models") };

                        // Possible model file names (case-insensitive search)
                        string[] modelFilePatterns = new string[]
                        {
                            "Colorize" + char.ToUpper(modelType[0]) + modelType.Substring(1) + "_gen.model",
                            "Colorize" + char.ToUpper(modelType[0]) + modelType.Substring(1) + "_gen.hmodel",
                            "*" + modelType + "*.model",
                            "*" + modelType + "*.hmodel",
                            "*.model",
                            "*.hmodel"
                        };

                        foreach(string searchPath in searchPaths)
                        {
                            if(!Directory.Exists(searchPath))
                            {
                                continue;
                            }

                            Console.Out.WriteLine("DeOldify CLI: searching in: " + searchPath);

                            // List all files for debugging
                            string[] allFiles = Directory.GetFiles(searchPath);
                            Console.Out.WriteLine("DeOldify CLI: files in directory: " + string.Join(", ", allFiles));

                            foreach(string pattern in modelFilePatterns)
                            {
                                string[] found = Directory.GetFiles(searchPath, pattern, SearchOption.TopDirectoryOnly);
                                if(found.Length > 0)
                                {
                                    modelPath = found[0];
                                    Console.Out.WriteLine("DeOldify CLI: found model: " + modelPath);
                                    break;
                                }
                            }

                            if(modelPath != null)
                            {
                                break;
                            }
                        }
                    }

                    if(modelPath == null)
                    {
                        throw new FileNotFoundException(
                            "Model file not found. Searched in: " + modelDirectory +
                            " (and models/ subdirectory). Please download model files from " +
                            "https://github.com/ColorfulSoft/DeOldify.NET/releases/tag/Weights " +
                            "and place ColorizeStable_gen.model and/or ColorizeArtistic_gen.model " +
                            "in the model directory.");
                    }

                    // Initialize with external model file
                    DeOldify.Initialize(modelPath);

                    Bitmap inputBitmap = new Bitmap(args[0]);
                    var result = DeOldify.Colorize(inputBitmap);
                    result.Save(args[1], System.Drawing.Imaging.ImageFormat.Png);
                    Console.Out.WriteLine("DeOldify: colorization complete");
                    return;
                }
                catch(Exception ex)
                {
                    Console.Error.WriteLine("DeOldify CLI error: " + ex.Message);
                    Console.Error.WriteLine(ex.StackTrace);
                    Environment.Exit(1);
                }
            }

            if(args.Length > 0)
            {
                return;
            }
            Application.EnableVisualStyles();
            try
            {
                Application.Run(new MainForm());
            }
            catch
            {
            }
        }

    }

}
