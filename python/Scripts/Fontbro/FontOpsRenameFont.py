import argparse
import sys
from fontbro import Font

def rename_font(font_path, family_name, style_name, update_style_flags, output_font_path, overwrite):
    """
    Renames the font names records according to the given family_name and style_name and saves it.

    :param font_path: Path to the font file.
    :param family_name: The new family name.
    :param style_name: The new style name.
    :param update_style_flags: if True the style flags will be updated by subfamily name.
    :param output_font_path: Path to save the modified font file.
    :param overwrite: Whether to overwrite the file if it already exists.
    :raises ValueError: if the computed PostScript-name is longer than 63 characters.
    """
    font = Font(font_path)
    font.rename(family_name=family_name, style_name=style_name, update_style_flags=update_style_flags)
    font.save(output_font_path, overwrite)

def main():
    parser = argparse.ArgumentParser(description='Rename font family and style names and save it.')
    parser.add_argument('font_path', type=str, help='The path to the font file')
    parser.add_argument('family_name', type=str, help='The new family name for the font')
    parser.add_argument('style_name', type=str, help='The new style name for the font')
    parser.add_argument('update_style_flags', type=lambda x: (str(x).lower() == 'true'), help='Whether to update style flags based on the subfamily name (true/false)')
    parser.add_argument('output_font_path', type=str, help='The path to save the modified font file')
    parser.add_argument('--overwrite', type=lambda x: x.lower() == 'true', default=False, help='Whether to overwrite the file if it already exists (True/False)')

    if len(sys.argv)==1:
        parser.print_help(sys.stderr)
        sys.exit(1)
        
    args = parser.parse_args()

    rename_font(args.font_path, args.family_name, args.style_name, args.update_style_flags, args.output_font_path, args.overwrite)
    print(f"Font renamed and saved to '{args.output_font_path}' (overwrite={args.overwrite})")

if __name__ == "__main__":
    main()


# python FontOpsRenameFont.py /path/to/original/fontfile.ttf "NewFamilyName" "Regular" true /path/to/save/newfont.ttf
# python FontOpsRenameFont.py /path/to/original/fontfile.ttf "MyFontFamily" "BoldItalic" false /path/to/save/modifiedfont.ttf --overwrite true
# python FontOpsRenameFont.py /path/to/font.ttf "SimpleFamily" "SimpleStyle" false /path/to/save/simplefont.ttf
# python FontOpsRenameFont.py "C:\Fonts\oldfont.ttf" "WindowsFamily" "WindowsStyle" true "C:\Fonts\newfont.ttf" --overwrite true
