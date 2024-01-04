import argparse
import sys
from fontbro import Font

def set_family_name(font_path, new_name, output_font_path, overwrite):
    """
    Sets the family name updating the related font names records and saves the font.

    :param font_path: Path to the font file.
    :param new_name: The new family name.
    :param output_font_path: Path to save the modified font file.
    :param overwrite: Whether to overwrite the file if it already exists.
    """
    font = Font(font_path)
    font.set_family_name(name=new_name)
    font.save(output_font_path, overwrite)

def main():
    # Create the parser
    parser = argparse.ArgumentParser(description='Set the family name of a font and save it.')
    # Add an argument for the font path
    parser.add_argument('font_path', type=str, help='The path to the font file')
    # Add an argument for the new family name
    parser.add_argument('new_name', type=str, help='The new family name for the font')
    # Add an argument for the output font path
    parser.add_argument('output_font_path', type=str, help='The path to save the modified font file')
    # Add an argument for the overwrite flag
    parser.add_argument('--overwrite', type=lambda x: x.lower() == 'true', default=False, help='Whether to overwrite the file if it already exists (True/False)')

    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)

    args = parser.parse_args()

    # Set the new family name and save the font
    set_family_name(args.font_path, args.new_name, args.output_font_path, args.overwrite)
    print(f"Family name set to '{args.new_name}' and saved to '{args.output_font_path}' (overwrite={args.overwrite})")

if __name__ == "__main__":
    main()



# python FontOpsSetFamilyName.py /path/to/fontfile.ttf "NewFamilyName" /path/to/save/newfontfile.ttf
# python FontOpsSetFamilyName.py /path/to/fontfile.ttf "AnotherFamily" /path/to/save/fontfile.ttf --overwrite true
# python FontOpsSetFamilyName.py C:\Fonts\MyFont.otf "UpdatedFamily" C:\Fonts\Saved\MyFont_Modified.otf
# python /path/to/script/FontOpsSetFamilyName.py /path/to/fontfile.ttf "ModernFamily" /path/to/save/newfontfile.ttf
# python FontOpsSetFamilyName.py /path/to/fontfile.otf "CreativeFamily" /otherpath/save/creativefont.otf --overwrite true
