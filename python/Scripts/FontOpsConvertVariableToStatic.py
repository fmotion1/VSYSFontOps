import argparse
import json
import sys
from fontbro import Font

def convert_to_static(font_path, coordinates_json, style_name, update_names, update_style_flags, options_json):
    """
    
    Converts the variable font to a static one pinning the variable axes at the given coordinates.
    If an axis value is not specified, the axis will be pinned at its default value.
    If coordinates are not specified each axis will be pinned at its default value.
    
    :param font_path: Path to the font file.
    :param coordinates_json: The coordinates in JSON format. eg. {'wght':500, 'ital':50}
    :type coordinates: dict or None
    :param style_name: The existing instance style name, eg. 'Black'
    :type style_name: str or None
    :param update_names: If True, the name records will be updated based on closest instance.
    :type update_names: bool
    :param update_style_flags: If True, the style flags will be updated based on closest instance.
    :type update_style_flags: bool
    :param options_json: The options for the fontTools.varLib.instancer in JSON format.
    :type options_json: dictionary
    
    :raises TypeError: If the font is not a variable font
    :raises ValueError: If the coordinates axes are not all pinned
    
    """
    font = Font(font_path)
    coordinates = json.loads(coordinates_json) if coordinates_json else None
    options = json.loads(options_json) if options_json else {}
    font.to_static(coordinates=coordinates, style_name=style_name, update_names=update_names, update_style_flags=update_style_flags, **options)

def main():
    parser = argparse.ArgumentParser(description='Convert a variable font to a static one at given coordinates.')
    parser.add_argument('font_path', type=str, help='The path to the font file')
    parser.add_argument('--coordinates', type=str, help='The coordinates in JSON format (e.g., \'{"wght":500, "ital":50}\')', default=None)
    parser.add_argument('--style_name', type=str, help='The existing instance style name (e.g., "Black")', default=None)
    parser.add_argument('--update_names', type=bool, default=True, help='Update name records based on closest instance (True/False)')
    parser.add_argument('--update_style_flags', type=bool, default=True, help='Update style flags based on closest instance (True/False)')
    parser.add_argument('--options', type=str, help='The options for the fontTools.varLib.instancer in JSON format', default=None)

    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)

    args = parser.parse_args()

    # Convert the variable font to a static one
    convert_to_static(args.font_path, args.coordinates, args.style_name, args.update_names, args.update_style_flags, args.options)
    print(f"Converted {args.font_path} to static font.")

if __name__ == "__main__":
    main()

# python FontOpsConvertVariableToStatic.py /path/to/fontfile.ttf
# python FontOpsConvertVariableToStatic.py /path/to/fontfile.ttf --coordinates '{"wght": 700, "wdth": 100}'
# python FontOpsConvertVariableToStatic.py /path/to/fontfile.ttf --style_name "Bold" --update_names true --update_style_flags true
# python FontOpsConvertVariableToStatic.py /path/to/fontfile.ttf --coordinates '{"wght": 500}' --options '{"someOption": "someValue"}'
# python FontOpsConvertVariableToStatic.py /path/to/fontfile.ttf --update_names false --update_style_flags false
