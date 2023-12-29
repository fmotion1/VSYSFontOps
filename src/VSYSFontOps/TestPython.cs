using System;
using System.Diagnostics;

namespace VSYSFontOps {

    class Program {

        static void Main(string[] args) {
            // Path to the Python interpreter (change as needed)
            string pythonExecutable = @"D:\Dev\Python\00 VENV\FontTools\Scripts\python.exe";

            // Path to your Python script
            string script = @"D:\Dev\Python\font_vsys\fontbro_get_font_name.py";

            // Argument with spaces
            string argumentWithSpaces = "D:/Fonts/Licensed/Mono/JetBrains Mono/TT 2.304/JetBrainsMono-Bold.ttf";

            // Escaping the double quotes by using \"
            string escapedArgument = $"\"{argumentWithSpaces}\"";

            // Arguments to pass to the script, space-separated
            string scriptArguments = $"{escapedArgument}";

            // Set up the process start info
            ProcessStartInfo start = new ProcessStartInfo {
                FileName = pythonExecutable,
                Arguments = $"\"{script}\" {scriptArguments}", // Arguments including the script and the arguments for the script
                UseShellExecute = false, // Do not use the system shell to start the process
                RedirectStandardOutput = true, // Redirect the standard output so it can be read from C#
                RedirectStandardError = true, // Redirect the standard error (optional)
                CreateNoWindow = true // Do not create a window (optional)
            };

            // Start the process and read the output
            using (Process process = Process.Start(start)) {
                using (StreamReader reader = process.StandardOutput) {
                    string result = reader.ReadToEnd(); // Read the standard output of the script
                    Console.WriteLine(result);
                }

                using (StreamReader reader = process.StandardError) {
                    string error = reader.ReadToEnd(); // Read any errors
                    if (!string.IsNullOrEmpty(error)) {
                        Console.Error.WriteLine(error);
                    }
                }
            }
        }
    }
}
