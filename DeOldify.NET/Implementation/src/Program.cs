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

                    // Try to find model file in the specified directory
                    string modelPath = null;
                    if(!string.IsNullOrEmpty(modelDirectory) && Directory.Exists(modelDirectory))
                    {
                        // Try .model first (float), then .hmodel (half)
                        string[] modelFiles = Directory.GetFiles(modelDirectory, "*" + modelType + "*.model");
                        if(modelFiles.Length == 0)
                        {
                            modelFiles = Directory.GetFiles(modelDirectory, "*" + modelType + "*.hmodel");
                        }
                        if(modelFiles.Length == 0)
                        {
                            // Try exact filenames
                            string exactModel = Path.Combine(modelDirectory, "Colorize" + char.ToUpper(modelType[0]) + modelType.Substring(1) + "_gen.model");
                            if(File.Exists(exactModel))
                            {
                                modelPath = exactModel;
                            }
                            else
                            {
                                string exactHModel = Path.Combine(modelDirectory, "Colorize" + char.ToUpper(modelType[0]) + modelType.Substring(1) + "_gen.hmodel");
                                if(File.Exists(exactHModel))
                                {
                                    modelPath = exactHModel;
                                }
                            }
                        }
                        else
                        {
                            modelPath = modelFiles[0];
                        }
                    }

                    // Initialize with external model file (or embedded if not found)
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
