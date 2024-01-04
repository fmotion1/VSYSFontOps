import argparse
import sys
from fontbro import Font

def get_font_filename(font_path, variable_suffix, variable_axes_tags, variable_axes_values):
    """
    Gets the filename to use for saving the font to the file-system.

    :param font_path: Path to the font file.
    :param variable_suffix: The variable suffix.
    :type variable_suffix: str
    :param variable_axes_tags: If True, the axes tags will be appended.
    :type variable_axes_tags: bool
    :param variable_axes_values: If True, each axis values will be appended. Example: '[wght(100,100,900),wdth(75,100,125)]'
    :type variable_axes_values: bool
    :returns: The filename.
    :rtype: str
    """
    font = Font(font_path)
    return font.get_filename(variable_suffix=variable_suffix, 
                             variable_axes_tags=variable_axes_tags, 
                             variable_axes_values=variable_axes_values)

def main():
    # Create the parser
    parser = argparse.ArgumentParser(description='Get the filename for saving the font to the file-system.')
    # Add an argument for the font path
    parser.add_argument('font_path', type=str, help='The path to the font file')
    # Add optional arguments with default values
    parser.add_argument('--variable_suffix', type=str, default="Variable", help='The variable suffix, default "Variable"')
    parser.add_argument('--variable_axes_tags', action='store_true', help='If True, append the axes tags, eg "[wght,wdth]"')
    parser.add_argument('--variable_axes_values', action='store_true', help='If True, append each axis values, eg "[wght(100,100,900),wdth(75,100,125)]"')
    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)
    # Parse the arguments
    args = parser.parse_args()

    # Get and print the filename for the font
    filename = get_font_filename(args.font_path, args.variable_suffix, args.variable_axes_tags, args.variable_axes_values)
    print(f"Filename for the font: {filename}")

if __name__ == "__main__":
    main()

# python FontOpsGetFontFilename.py /path/to/fontfile.ttf
# python FontOpsGetFontFilename.py /path/to/fontfile.ttf --variable_suffix "MySuffix"
# python FontOpsGetFontFilename.py /path/to/fontfile.ttf --variable_suffix "Custom" --variable_axes_tags --variable_axes_values
# python FontOpsGetFontFilename.py C:\Fonts\MyFont.otf
# python /path/to/script/FontOpsGetFontFilename.py /path/to/fontfile.ttf --variable_suffix "Unique" --variable_axes_tags
