using System;
using System.Management.Automation;
using System.Diagnostics;
using System.IO;

namespace VSYSFontOps.FontObjects
{
    public sealed class FontFile
    {
        public string FontPath { get; set; }
        public string FontFilename { get; set; }
        public string FontFamilyName { get; set; }
        public string FontStyleName { get; set; }
        public string FontPostscriptName { get; set; }
        public string FontFullName { get; set; }
        public string FontFormat { get; set; }
        public string FontUPM { get; set; }
        public string NumGlyphs { get; set; }
        public bool FontIsVariable { get; set; }

        public FontFile ( string fontPath, string fontFilename, string fontFamilyName, 
                          string fontStyleName, string fontPostscriptName, 
                          string fontFullName, string fontFormat, string fontUPM, 
                          string numGlyphs, bool fontIsVariable)
        {
            FontPath           = fontPath;
            FontFilename       = fontFilename;
            FontFamilyName     = fontFamilyName;
            FontStyleName      = fontStyleName;
            FontPostscriptName = fontPostscriptName;
            FontFullName       = fontFullName;
            FontFormat         = fontFormat;
            FontUPM            = fontUPM;
            NumGlyphs          = numGlyphs;
            FontIsVariable     = fontIsVariable;

        }

        public override string ToString()
        {
            return $"FontPath: {FontPath}, FontFilename: {FontFilename}, FontFamilyName: {FontFamilyName}, " +
                   $"FontStyleName: {FontStyleName}, FontPostscriptName: {FontPostscriptName}, FontFullName: {FontFullName}, " +
                   $"FontFormat: {FontFormat}, FontUPM: {FontUPM}, NumGlyphs: {NumGlyphs}, FontIsVariable: {FontIsVariable}";
        }
    }
}
