import argparse
import sys
from fontbro import Font

def get_glyphs_count(font_path):
    """
    Gets the font glyphs count.

    :param font_path: Path to the font file.
    :returns: The glyphs count.
    :rtype: int
    """
    font = Font(font_path)
    return font.get_glyphs_count()

def main():
    # Create the parser
    parser = argparse.ArgumentParser(description='Get the glyphs count of a font file.')
    # Add an argument for the font path
    parser.add_argument('font_path', type=str, help='The path to the font file')
    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)
    # Parse the arguments
    args = parser.parse_args()

    # Get and print the glyphs count
    glyphs_count = get_glyphs_count(args.font_path)
    print(f"The font has {glyphs_count} glyphs.")

if __name__ == "__main__":
    main()

# python FontOpsGetGlyphsCount.py /path/to/fontfile.ttf
# python FontOpsGetGlyphsCount.py C:\Fonts\MyFont.otf
# python /path/to/script/FontOpsGetGlyphsCount.py /path/to/fontfile.ttf
