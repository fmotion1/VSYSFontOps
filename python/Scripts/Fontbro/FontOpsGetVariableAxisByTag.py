import argparse
import json
import sys
from fontbro import Font

# _VARIABLE_AXES = [
# https://fonts.google.com/variablefonts#axis-definitions
# {"tag": "ital", "name": "Italic"},
# {"tag": "opsz", "name": "Optical Size"},
# {"tag": "slnt", "name": "Slant"},
# {"tag": "wdth", "name": "Width"},
# {"tag": "wght", "name": "Weight"},
# {"tag": "CASL", "name": "Casual"},
# {"tag": "CRSV", "name": "Cursive"},
# {"tag": "XPRN", "name": "Expression"},
# {"tag": "FILL", "name": "Fill"},
# {"tag": "GRAD", "name": "Grade"},
# {"tag": "MONO", "name": "Monospace"},
# {"tag": "SOFT", "name": "Softness"},
# {"tag": "WONK", "name": "Wonky"},
# ]

def get_variable_axis_by_tag(font_path, tag):
    """
    Gets a variable axis by tag.

    :param font_path: Path to the font file.
    :param tag: The tag representing the axis.
    :returns: The variable axis by tag.
    :rtype: dict or None
    """
    font = Font(font_path)
    return font.get_variable_axis_by_tag(tag)

def main():
    parser = argparse.ArgumentParser(description='Get a variable axis by tag from a font.')
    parser.add_argument('font_path', type=str, help='The path to the font file')
    parser.add_argument('tag', type=str, help='The tag representing the variable axis')
    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)
    args = parser.parse_args()

    # Retrieve and print the variable axis
    axis = get_variable_axis_by_tag(args.font_path, args.tag)
    print(json.dumps(axis, indent=2))

if __name__ == "__main__":
    main()


# python FontOpsGetVariableAxisByTag.py /path/to/fontfile.ttf wght
# python FontOpsGetVariableAxisByTag.py /path/to/fontfile.ttf ital
# python FontOpsGetVariableAxisByTag.py /path/to/anotherfontfile.otf opsz
# python FontOpsGetVariableAxisByTag.py C:\Fonts\MyVariableFont.otf wdth
