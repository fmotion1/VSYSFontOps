import argparse
import sys
from fontbro import Font

def get_features(font_path):
    """
    Gets the font opentype features.

    :param font_path: Path to the font file.
    :returns: The features.
    :rtype: list of dict
    """
    font = Font(font_path)
    return font.get_features()

def main():
    # Create the parser
    parser = argparse.ArgumentParser(description='Get the OpenType features of a font file.')
    # Add an argument for the font path
    parser.add_argument('font_path', type=str, help='The path to the font file')
    
    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)
    
    # Parse the arguments
    args = parser.parse_args()

    # Get and print the OpenType features
    features = get_features(args.font_path)
    print("OpenType features:")
    for feature in features:
        print(feature)

if __name__ == "__main__":
    main()


# python FontOpsGetFeatures.py /path/to/fontfile.ttf
# python FontOpsGetFeatures.py C:\Fonts\MyFont.otf
# python /path/to/script/FontOpsGetFeatures.py /path/to/fontfile.ttf
