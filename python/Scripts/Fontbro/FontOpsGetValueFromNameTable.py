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


def get_value_from_name_table(font_path, name_key):
    """
    Gets the name by its identifier from the font name table.

    :param font_path: Path to the font file.
    :param name_key: The name id or key (e.g., "family_name" or Font.NAME_FAMILY_NAME).
    :returns: The name.
    :rtype: str or None
    :raises KeyError: if the key is not a valid name key/id
    """
    font = Font(font_path)
    try:
        name_value = font.get_name(key=name_key)
        return name_value
    except KeyError as e:
        print(f"KeyError: {e}")
        return None

def main():
    parser = argparse.ArgumentParser(description='Get a value from the font name table.')
    parser.add_argument('font_path', type=str, help='The path to the font file')
    parser.add_argument('name_key', type=str, help='The name key to retrieve (e.g., "family_name")')
    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)
    args = parser.parse_args()

    # Convert name_key to int if it's a digit, otherwise pass as is
    name_key = int(args.name_key) if args.name_key.isdigit() else args.name_key

    # Retrieve and print the value from the name table
    name_value = get_value_from_name_table(args.font_path, name_key)
    print(name_value)

if __name__ == "__main__":
    main()

# python FontOpsGetValueFromNameTable.py /path/to/fontfile.ttf family_name
# python FontOpsGetValueFromNameTable.py /path/to/fontfile.ttf full_name
# python FontOpsGetValueFromNameTable.py C:\Fonts\MyFont.otf 9
# python FontOpsGetValueFromNameTable.py /path/to/differentfont.otf license_description
# python /path/to/script/FontOpsGetValueFromNameTable.py /path/to/fontfile.ttf version
