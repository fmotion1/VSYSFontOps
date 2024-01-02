import argparse
import sys
from fontbro import Font

def get_features_tags(font_path):
    """
    Gets the font opentype features tags.

    :param font_path: Path to the font file.
    :returns: The features tags list.
    :rtype: list of str
    """
    font = Font(font_path)
    return font.get_features_tags()

def main():
    # Create the parser
    parser = argparse.ArgumentParser(description='Get the OpenType features tags of a font file.')
    # Add an argument for the font path
    parser.add_argument('font_path', type=str, help='The path to the font file')
    
    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)
    
    # Parse the arguments
    args = parser.parse_args()

    # Get and print the OpenType features tags
    features_tags = get_features_tags(args.font_path)
    print("OpenType features tags:")
    for tag in features_tags:
        print(tag)

if __name__ == "__main__":
    main()


# python FontOpsGetFeaturesTags.py /path/to/fontfile.ttf
# python FontOpsGetFeaturesTags.py C:\Fonts\MyFont.otf
# python /path/to/script/FontOpsGetFeaturesTags.py /path/to/fontfile.ttf
