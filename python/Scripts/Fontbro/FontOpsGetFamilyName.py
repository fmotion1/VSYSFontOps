import argparse
import sys
from fontbro import Font

def get_family_name(font_path):
    """
    Gets the family name reading the name records with priority order (16, 21, 1).

    :param font_path: Path to the font file.
    :returns: The font family name.
    :rtype: str
    """
    font = Font(font_path)
    return font.get_family_name()

def main():
    # Create the parser
    parser = argparse.ArgumentParser(description='Get the family name of a font.')
    # Add an argument for the font path
    parser.add_argument('font_path', type=str, help='The path to the font file')
    
    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)
    
    # Parse the arguments
    args = parser.parse_args()
    # Get and print the family name
    family_name = get_family_name(args.font_path)
    print(family_name)

if __name__ == "__main__":
    main()


# python FontOpsGetFamilyName.py /path/to/fontfile.ttf
# python FontOpsGetFamilyName.py /path/to/anotherfontfile.otf
# python FontOpsGetFamilyName.py C:\Fonts\MyFont.ttf
# python /path/to/script/FontOpsGetFamilyName.py /path/to/fontfile.ttf
# python FontOpsGetFamilyName.py /specific/directory/fonts/FontName.otf
