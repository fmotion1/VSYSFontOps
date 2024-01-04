import argparse
import json
import sys
from fontbro import Font

def get_variable_instances(font_path):
    """
    Gets the variable instances for the given font.

    :param font_path: Path to the font file.
    :returns: The list of instances if the font is a variable font otherwise None.
    :rtype: list of dict or None
    """
    font = Font(font_path)
    return font.get_variable_instances()

def main():
    # Create the parser and add argument
    parser = argparse.ArgumentParser(description='Process some fonts.')
    parser.add_argument('font_path', type=str, help='The path to the font file')

    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)

    # Parse the arguments
    args = parser.parse_args()

    # Get variable instances and print
    variable_instances = get_variable_instances(args.font_path)
    print(variable_instances)

if __name__ == "__main__":
    main()



# python FontOpsGetVariableInstances.py /path/to/variablefont.ttf
# python FontOpsGetVariableInstances.py /path/to/anotherVariableFont.otf
# python FontOpsGetVariableInstances.py C:\Fonts\MyVariableFont.ttf
# python /path/to/script/FontOpsGetVariableInstances.py /path/to/variablefont.ttf
# python FontOpsGetVariableInstances.py /specific/directory/fonts/VariableFontName.otf
