import argparse
import sys
from fontbro import Font

def get_characters(font_path, ignore_blank):
    """
    Gets the font characters.

    :param font_path: Path to the font file.
    :param ignore_blank: If True, characters without contours will not be returned.
    :returns: The characters.
    :rtype: generator of dicts
    """
    font = Font(font_path)
    return font.get_characters(ignore_blank=ignore_blank)

def main():
    parser = argparse.ArgumentParser(description='Get the characters of a font file.')
    parser.add_argument('font_path', type=str, help='The path to the font file')
    parser.add_argument('--ignore_blank', action='store_true', help='If set, characters without contours will not be returned')
    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)
    args = parser.parse_args()
    chars = get_characters(args.font_path, args.ignore_blank)
    for char in chars:
        print(char)

if __name__ == "__main__":
    main()
    
    
# python FontOpsGetCharacters.py /path/to/fontfile.ttf
# python FontOpsGetCharacters.py /path/to/fontfile.ttf --ignore_blank
# python FontOpsGetCharacters.py C:\Fonts\MyFont.otf
# python /path/to/script/FontOpsGetCharacters.py /path/to/fontfile.ttf

