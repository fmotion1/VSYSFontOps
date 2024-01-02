import argparse
import sys
from fontbro import Font

def get_font_format(font_path, ignore_flavor):
    """
    Gets the font format: otf, ttf, woff, woff2.

    :param font_path: Path to the font file.
    :param ignore_flavor: If True, the original format without compression will be returned.
    :returns: The format.
    :rtype: str or None
    """
    font = Font(font_path)
    return font.get_format(ignore_flavor=ignore_flavor)

def main():
    # Create the parser
    parser = argparse.ArgumentParser(description='Get the font format of a font file.')
    # Add an argument for the font path
    parser.add_argument('font_path', type=str, help='The path to the font file')
    # Add an optional argument for ignore_flavor with default as False
    parser.add_argument('--ignore_flavor', action='store_true', help='Return original format without compression if set to True')
    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)
    # Parse the arguments
    args = parser.parse_args()
    
    # Get and print the font format
    format = get_font_format(args.font_path, args.ignore_flavor)
    print(format)

if __name__ == "__main__":
    main()

# python FontOpsGetFontFormat.py /path/to/fontfile --ignore_flavor
# python FontOpsGetFontFormat.py /Users/username/fonts/MyFont.ttf --ignore_flavor
# python FontOpsGetFontFormat.py /Users/username/fonts/MyFont.ttf
