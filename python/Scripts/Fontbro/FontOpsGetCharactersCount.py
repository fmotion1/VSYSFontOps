import argparse
import sys
from fontbro import Font

def get_characters_count(font_path, ignore_blank):
    """
    Gets the font characters count.

    :param font_path: Path to the font file.
    :param ignore_blank: If True, characters without contours will not be counted.
    :returns: The characters count.
    :rtype: int
    """
    font = Font(font_path)
    return font.get_characters_count(ignore_blank=ignore_blank)

def main():
    parser = argparse.ArgumentParser(description='Get the characters count of a font file.')
    parser.add_argument('font_path', type=str, help='The path to the font file')
    parser.add_argument('--ignore_blank', action='store_true', help='If set, characters without contours will not be counted')
    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)
    args = parser.parse_args()
    chars_count = get_characters_count(args.font_path, args.ignore_blank)
    print(f"Characters count: {chars_count}")

if __name__ == "__main__":
    main()

# python FontOpsGetCharactersCount.py /path/to/fontfile.ttf
# python FontOpsGetCharactersCount.py /path/to/fontfile.ttf --ignore_blank
# python FontOpsGetCharactersCount.py C:\Fonts\MyFont.otf
# python /path/to/script/FontOpsGetCharactersCount.py /path/to/fontfile.ttf
