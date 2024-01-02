import argparse
import sys
from fontTools.ttLib import TTFont

def get_upm(font_path):
    """
    Retrieves the units per em (UPM) value from a font.

    :param font_path: Path to the font file.
    :return: The UPM value.
    """
    font = TTFont(font_path)
    upm = font['head'].unitsPerEm
    return upm

def main():
    # Initialize parser
    parser = argparse.ArgumentParser(description="Retrieve a font's UPM value.")
    
    # Adding required argument
    parser.add_argument('font_path', type=str, help='Path to the font file')
    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)
    # Parse arguments
    args = parser.parse_args()
    
    # Get the UPM value and print it
    upm_value = get_upm(args.font_path)
    print(f"The UPM of the font is: {upm_value}")

if __name__ == "__main__":
    main()


# python FontOpsGetUPM.py C:/path/to/your/fontfile.ttf
