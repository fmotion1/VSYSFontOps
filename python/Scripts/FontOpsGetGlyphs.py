import argparse
import sys
from fontbro import Font

def get_glyphs(font_path):
    """
    Gets the font glyphs and their own composition.

    :param font_path: Path to the font file.
    :returns: The glyphs.
    :rtype: generator of dicts
    """
    font = Font(font_path)
    return font.get_glyphs()

def main():
    # Create the parser
    parser = argparse.ArgumentParser(description='Get the glyphs of a font file.')
    # Add an argument for the font path
    parser.add_argument('font_path', type=str, help='The path to the font file')
    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)
    # Parse the arguments
    args = parser.parse_args()

    # Get and print the glyphs
    glyphs = get_glyphs(args.font_path)
    for glyph in glyphs:
        print(glyph)

if __name__ == "__main__":
    main()


# python FontOpsGetGlyphs.py /path/to/fontfile.ttf
# python FontOpsGetGlyphs.py /path/to/anotherfontfile.otf
# python FontOpsGetGlyphs.py C:\Fonts\MyFont.ttf
# python /path/to/script/FontOpsGetGlyphs.py /path/to/fontfile.ttf
# python FontOpsGetGlyphs.py /specific/directory/fonts/FontName.otf
