//*************************************************************************************************
//* (C) ColorfulSoft corp., 2021 - 2022. All Rights reserved.
//*************************************************************************************************

using System;
using System.IO;
using System.Drawing;
using System.Windows.Forms;
using System.Runtime.ExceptionServices;

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
        [HandleProcessCorruptedStateExceptions]
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
                        // Both .model (float32) and .hmodel (float16) are supported.
                        // The format is auto-detected by the Initialize method from the file extension.
                        string[] modelFilePatterns = new string[]
                        {
                            "Colorize" + char.ToUpper(modelType[0]) + modelType.Substring(1) + "_gen.model",
                            "Colorize" + char.ToUpper(modelType[0]) + modelType.Substring(1) + "_gen.hmodel",
                            "Colorize" + char.ToUpper(modelType[0]) + modelType.Substring(1) + ".model",
                            "Colorize" + char.ToUpper(modelType[0]) + modelType.Substring(1) + ".hmodel",
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

                    // Check architecture mismatch: exe compiled as stable/artistic vs model type
                    #if stable
                        if(modelType.ToLowerInvariant() != "stable")
                        {
                            Console.Error.WriteLine("DeOldify FATAL: Architecture mismatch!");
                            Console.Error.WriteLine("  This exe was compiled with /define:stable (stable architecture).");
                            Console.Error.WriteLine("  But the model type requested is: " + modelType);
                            Console.Error.WriteLine("  The model file is: " + modelPath);
                            Console.Error.WriteLine("");
                            Console.Error.WriteLine("  Solution: Either:");
                            Console.Error.WriteLine("    1. Use deoldify_stable.exe with a stable model (ColorizeStable_gen.model)");
                            Console.Error.WriteLine("    2. Recompile without /define:stable for artistic model support");
                            Console.Error.WriteLine("       Use: Compile.artistic.unified.bat");
                            Environment.Exit(2);
                        }
                    #else
                        if(modelType.ToLowerInvariant() == "stable")
                        {
                            Console.Error.WriteLine("DeOldify FATAL: Architecture mismatch!");
                            Console.Error.WriteLine("  This exe was compiled for artistic model (no /define:stable).");
                            Console.Error.WriteLine("  But the model type requested is: stable");
                            Console.Error.WriteLine("  The model file is: " + modelPath);
                            Console.Error.WriteLine("");
                            Console.Error.WriteLine("  Solution: Either:");
                            Console.Error.WriteLine("    1. Use deoldify_artistic.exe with an artistic model (ColorizeArtistic_gen.model)");
                            Console.Error.WriteLine("    2. Recompile with /define:stable for stable model support");
                            Console.Error.WriteLine("       Use: Compile.stable.unified.bat");
                            Environment.Exit(2);
                        }
                    #endif

                    // Initialize with external model file
                    DeOldify.Initialize(modelPath);

                    Bitmap inputBitmap = new Bitmap(args[0]);
                    var result = DeOldify.Colorize(inputBitmap);
                    result.Save(args[1], System.Drawing.Imaging.ImageFormat.Png);
                    Console.Out.WriteLine("DeOldify: colorization complete");
                    return;
                }
                catch(AccessViolationException ex)
                {
                    Console.Error.WriteLine("DeOldify FATAL: AccessViolationException (memory access violation)");
                    Console.Error.WriteLine("This is likely caused by:");
                    Console.Error.WriteLine("  1. Architecture mismatch (exe compiled as stable but using artistic model, or vice versa)");
                    Console.Error.WriteLine("  2. Model format mismatch (float32 .model vs float16 .hmodel)");
                    Console.Error.WriteLine("  3. Corrupted model file");
                    Console.Error.WriteLine("");
                    Console.Error.WriteLine("Solution: Ensure the exe architecture matches the model type:");
                    Console.Error.WriteLine("  - For artistic models (ColorizeArtistic_gen.model): use Compile.artistic.unified.bat");
                    Console.Error.WriteLine("  - For stable models (ColorizeStable_gen.model): use Compile.stable.unified.bat");
                    Console.Error.WriteLine("");
                    Console.Error.WriteLine(ex.Message);
                    Console.Error.WriteLine(ex.StackTrace);
                    Environment.Exit(-1073741819); // 0xC0000005
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
