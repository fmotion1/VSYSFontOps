import argparse
import sys
from fontbro import Font

def set_style_flags_by_subfamily_name(font_path, output_font_path, overwrite):
    """
    Sets the style flags by the subfamily name value and saves the font.

    :param font_path: Path to the font file.
    :param output_font_path: Path to save the modified font file.
    :param overwrite: Whether to overwrite the file if it already exists.
    """
    font = Font(font_path)
    font.set_style_flags_by_subfamily_name()
    font.save(output_font_path, overwrite)

def main():
    # Create the parser
    parser = argparse.ArgumentParser(description='Set the style flags by the subfamily name of a font and save it.')
    # Add an argument for the font path
    parser.add_argument('font_path', type=str, help='The path to the font file')
    # Add an argument for the output font path
    parser.add_argument('output_font_path', type=str, help='The path to save the modified font file')
    # Add an argument for the overwrite flag
    parser.add_argument('--overwrite', type=lambda x: x.lower() == 'true', default=False, help='Whether to overwrite the file if it already exists (True/False)')

    if len(sys.argv) == 1:
            parser.print_help(sys.stderr)
            sys.exit(1)
    
    args = parser.parse_args()

    # Set the style flags by subfamily name and save the font
    set_style_flags_by_subfamily_name(args.font_path, args.output_font_path, args.overwrite)
    print(f"Style flags set by subfamily name and saved to '{args.output_font_path}' (overwrite={args.overwrite})")

if __name__ == "__main__":
    main()



# python FontOpsSetStyleFlagsBySubfamilyName.py /path/to/fontfile.ttf /path/to/save/newfontfile.ttf
# python FontOpsSetStyleFlagsBySubfamilyName.py /path/to/fontfile.ttf /path/to/save/newfontfile.ttf --overwrite true
# python FontOpsSetStyleFlagsBySubfamilyName.py C:\Fonts\MyFont.otf C:\Fonts\Saved\MyFont_Modified.otf
# python /path/to/script/FontOpsSetStyleFlagsBySubfamilyName.py /path/to/fontfile.ttf /path/to/save/newfontfile.ttf
# python FontOpsSetStyleFlagsBySubfamilyName.py /path/to/fontfile.otf /otherpath/save/modifiedfont.otf --overwrite true
