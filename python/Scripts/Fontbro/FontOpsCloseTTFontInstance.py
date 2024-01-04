import argparse
import sys
from fontbro import Font

def close_font(font_path):
    """
    Close the wrapped TTFont instance.

    :param font_path: Path to the font file.
    """
    font = Font(font_path)
    font.close()

def main():
    # Create the parser
    parser = argparse.ArgumentParser(description='Close the wrapped TTFont instance of a font file.')
    # Add an argument for the font path
    parser.add_argument('font_path', type=str, help='The path to the font file')
    
    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)
        
    # Parse the arguments
    args = parser.parse_args()

    # Close the font
    close_font(args.font_path)
    print(f"Closed font file: {args.font_path}")

if __name__ == "__main__":
    main()



# Since this script's main action is to close the font, it's mainly useful for
# ensuring resources are properly released, especially when used as part of a larger
# script or application where you're doing multiple operations on fonts.

# python FontOpsCloseTTFontInstance.py /path/to/fontfile.ttf
# python FontOpsCloseTTFontInstance.py /path/to/anotherfontfile.otf
# python FontOpsCloseTTFontInstance.py C:\Fonts\MyFont.ttf
