import argparse
import sys
from fontbro import Font

# Name Values:

# 00 "copyright_notice"
# 01 "family_name"
# 02 "subfamily_name"
# 03 "unique_identifier"
# 04 "full_name"
# 05 "version"
# 06 "postscript_name"
# 07 "trademark"
# 08 "manufacturer_name"
# 09 "designer"
# 10 "description"
# 11 "vendor_url"
# 12 "designer_url"
# 13 "license_description"
# 14 "license_info_url"
# 15 "reserved"
# 16 "typographic_family_name"
# 17 "typographic_subfamily_name"
# 18 "compatible_full"
# 19 "sample_text"
# 20 "postscript_cid_findfont_name"
# 21 "wws_family_name"
# 22 "wws_subfamily_name"
# 23 "light_background_palette"
# 24 "dark_background_palette"
# 25 "variations_postscript_name_prefix"


def set_name(font_path, name_key, new_value, output_font_path, overwrite):
    """
    Sets the name by its identifier in the font name table and saves the font.

    :param font_path: Path to the font file.
    :param name_key: The name id or key (e.g., "family_name" or Font.NAME_FAMILY_NAME).
    :param new_value: The new value for the specified name key.
    :param output_font_path: Path to save the modified font file.
    :param overwrite: Whether to overwrite the file if it already exists.
    """
    font = Font(font_path)
    font.set_name(name_key, new_value)
    font.save(output_font_path, overwrite)

def main():
    parser = argparse.ArgumentParser(description='Set a name record in the font name table and save it.')
    parser.add_argument('font_path', type=str, help='The path to the font file')
    parser.add_argument('name_key', type=str, help='The name id or key to set (e.g., "family_name" or a number for the ID)')
    parser.add_argument('new_value', type=str, help='The new value for the specified name key')
    parser.add_argument('output_font_path', type=str, help='The path to save the modified font file')
    parser.add_argument('--overwrite', type=lambda x: x.lower() == 'true', default=False, help='Whether to overwrite the file if it already exists (True/False)')

    if len(sys.argv)==1:
        parser.print_help(sys.stderr)
        sys.exit(1)

    args = parser.parse_args()

    # Convert name_key to int if it's a digit, otherwise pass as is
    name_key = int(args.name_key) if args.name_key.isdigit() else args.name_key

    # Set the new name and save the font
    set_name(args.font_path, name_key, args.new_value, args.output_font_path, args.overwrite)
    print(f"Name '{args.name_key}' set to '{args.new_value}' and saved to '{args.output_font_path}' (overwrite={args.overwrite})")

if __name__ == "__main__":
    main()


# python FontOpsSetName.py /path/to/fontfile.ttf family_name "NewFamily" /path/to/save/newfontfile.ttf
# python FontOpsSetName.py /path/to/fontfile.ttf version "2.0" /path/to/save/newfontfile.ttf --overwrite true
# python FontOpsSetName.py C:\Fonts\MyFont.otf full_name "My Full Font Name" C:\Fonts\Saved\MyFont_Modified.otf
# python /path/to/script/FontOpsSetName.py /path/to/fontfile.ttf postscript_name "MyFont-PostScript" /path/to/save/newfontfile.ps --overwrite false
# python FontOpsSetName.py /path/to/fontfile.otf typographic_family_name "TypoFamily" /otherpath/save/typofamilyfont.otf --overwrite true
