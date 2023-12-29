using System;
using System.Management.Automation;
using System.Diagnostics;
using System.IO;
using Newtonsoft.Json;


namespace VSYSFontOps.Fonts
{

    [Cmdlet(VerbsCommon.Get, "FontRecord")]
    public class GetFontRecordCommand : PSCmdlet
    {
        [Parameter(Mandatory = true)]
        public string[] Fonts { get; set; }

        protected override void ProcessRecord()
        {
            foreach (var font in Fonts)
            {
                bool isValidPath = PathValidator.IsValidPath(font);
                if(!isValidPath){
                    Console.WriteLine("Font path is invalid. Skipping.");
                }else{
                    new FontRecord(font);
                    
                }
            }
        }
    }

    public class FontRecord
    {
        public string FontPath { get; private set; }
        public string FontFilename { get; private set; }
        public string FontNamePostscript { get; private set; }
        public string FontNameFull { get; private set; }
        public string FontFormat { get; private set; }
        public string FontVersion { get; private set; }
        public bool FontIsVariable { get; private set; }

        public FontRecord(string fontPath)
        {
            FontFilename = Path.GetFileName(fontPath);
            PopulateFontNames(fontPath);
        }

        private void PopulateFontNames(string fontPath)
        {

            string baseDirectory = AppDomain.CurrentDomain.BaseDirectory;
            string pythonExecutableRelativePath = "../bin/FontTools/Scripts/python.exe";
            string scriptRelativePath = @"../bin/FontScripts/FontOpsMain.py";

            string pythonExecutable = Path.Combine(baseDirectory, pythonExecutableRelativePath);
            string scriptPath = Path.Combine(baseDirectory, scriptRelativePath);

            // Ensure the paths are correctly formatted for the current platform
            pythonExecutable = Path.GetFullPath(pythonExecutable);
            scriptPath = Path.GetFullPath(scriptPath);

            // Escaping the double quotes by using \"
            string escapedArgument = $"\"{fontPath}\"";

            // Arguments to pass to the script, space-separated
            string scriptArguments = $"{escapedArgument}";

            ProcessStartInfo start = new ProcessStartInfo
            {
                FileName = pythonExecutable,
                Arguments = $"\"{scriptPath}\" {scriptArguments}",
                UseShellExecute = false,
                RedirectStandardOutput = true,
                RedirectStandardError = true,
                CreateNoWindow = true
            };

            using (Process process = Process.Start(start))
            {
                using (StreamReader reader = process.StandardOutput)
                {
                    // Read the JSON output from the script
                    string result = reader.ReadToEnd();

                    // Parse the JSON output
                    dynamic fontInfo = JsonConvert.DeserializeObject(result); 

                    // Populate the properties
                    FontFormat = fontInfo.fontFormat;
                    FontIsVariable = fontInfo.fontIsVariable;
                }
            }
        }

        public override string ToString()
        {
            return $"FontPath: {FontPath}, FontFilename: {FontFilename}, FontNamePostscript: {FontNamePostscript}, " +
                   $"FontNameFull: {FontNameFull}, FontFormat: {FontFormat}, FontIsVariable: {FontIsVariable}";
        }
    }
    public class PathValidator
    {
        public static bool IsValidPath(string path)
        {
            if (string.IsNullOrWhiteSpace(path))
            {
                return false;
            }

            // Check for invalid path characters
            char[] invalidPathChars = Path.GetInvalidPathChars();
            foreach (char c in invalidPathChars)
            {
                if (path.Contains(c))
                {
                    return false;
                }
            }

            // Attempt to parse the path to ensure it's well-formed
            try
            {
                Path.GetFullPath(path); // This checks for invalid paths, etc.
            }
            catch (Exception)
            {
                // If an exception is thrown, the path is invalid
                return false;
            }

            // The path seems to be valid
            return true;
        }
    }
}
