import argparse
import json
import sys
from fontbro import Font

def set_names(font_path, names_json, output_font_path, overwrite):
    """
    Sets the names by their identifier in the font name table and saves the font.

    :param font_path: Path to the font file.
    :param names_json: The names in JSON format, where each key is the name id or key and each value is the new name.
    :param output_font_path: Path to save the modified font file.
    :param overwrite: Whether to overwrite the file if it already exists.
    """
    font = Font(font_path)
    names = json.loads(names_json)
    font.set_names(names=names)
    font.save(output_font_path, overwrite)

def main():
    parser = argparse.ArgumentParser(description='Set multiple name records in the font name table and save it.')
    parser.add_argument('font_path', type=str, help='The path to the font file')
    parser.add_argument('names_json', type=str, help='The names in JSON format. (e.g., \'{"1": "Family Name Renamed", "2": "Regular Renamed"}\')')
    parser.add_argument('output_font_path', type=str, help='The path to save the modified font file')
    parser.add_argument('--overwrite', type=lambda x: x.lower() == 'true', default=False, help='Whether to overwrite the file if it already exists (True/False)')

    if len(sys.argv)==1:
        parser.print_help(sys.stderr)
        sys.exit(1)

    args = parser.parse_args()
    # Set the new names and save the font
    set_names(args.font_path, args.names_json, args.output_font_path, args.overwrite)
    print(f"Names updated and saved to '{args.output_font_path}' (overwrite={args.overwrite})")

if __name__ == "__main__":
    main()


# python FontOpsSetNames.py /path/to/fontfile.ttf '{"1": "New Family Name", "2": "New Subfamily Name"}' /path/to/save/newfontfile.ttf
# python FontOpsSetNames.py /path/to/fontfile.ttf '{"4": "New Full Name", "5": "2.0"}' /path/to/save/newfontfile.ttf --overwrite true
# python FontOpsSetNames.py C:\Fonts\MyFont.otf '{"16": "New Typographic Family", "17": "New Typographic Subfamily"}' C:\Fonts\Saved\MyFont_Modified.otf
# python /path/to/script/FontOpsSetNames.py /path/to/fontfile.ttf '{"7": "New Trademark", "11": "http://newvendorurl.com"}' /path/to/save/newfontfile.ttf --overwrite false
# python FontOpsSetNames.py /path/to/fontfile.otf '{"1": "Family Renamed", "2": "Regular Renamed", "3": "Unique Identifier Updated"}' /otherpath/save/renamedfont.otf --overwrite true
