import argparse
import json
import sys
from fontbro import Font

# Example Coordinates:

# {"wght": 1000, "slnt": 815, "wdth": 775}
# {'wdth':100, 'wght':(100,600), 'ital':(30,65,70)} or
# {'wdth':100, 'wght':[100,600], 'ital':[30,65,70]} or
# {'wdth':100, 'wght':{'min':100,'max':600}, 'ital':{'min':30,'default':65,'max':70}}

def get_variable_instance_closest_to_coordinates(font_path, coordinates_json):
    """
    Gets the variable instance closest to coordinates.

    :param font_path: Path to the font file.
    :param coordinates_json: The coordinates in JSON format.
    :returns: The variable instance closest to coordinates.
    :rtype: dict or None
    """
    font = Font(font_path)
    coordinates = json.loads(coordinates_json)
    return font.get_variable_instance_closest_to_coordinates(coordinates=coordinates)

def main():
    parser = argparse.ArgumentParser(description='Get a variable instance closest to given coordinates from a font.')
    parser.add_argument('font_path', type=str, help='The path to the font file')
    parser.add_argument('coordinates_json', type=str, help='The coordinates in JSON format (e.g., \'{"wght": 1000, "slnt": 815, "wdth": 775}\')')
    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)
    args = parser.parse_args()

    # Retrieve and print the variable instance
    instance = get_variable_instance_closest_to_coordinates(args.font_path, args.coordinates_json)
    print(json.dumps(instance, indent=2))

if __name__ == "__main__":
    main()


# python FontOpsGetVariableInstanceClosestToCoordinates.py /path/to/fontfile.ttf '{"wght": 1000, "slnt": 815, "wdth": 775}'
# python FontOpsGetVariableInstanceClosestToCoordinates.py /path/to/fontfile.ttf '{"wdth":100, "wght":500}'
# python FontOpsGetVariableInstanceClosestToCoordinates.py C:\Fonts\MyVariableFont.otf '{"wdth":100, "wght":{"min":100,"max":600}, "ital":{"min":30,"default":65,"max":70}}'
# python FontOpsGetVariableInstanceClosestToCoordinates.py /path/to/fontfile.otf '{"wght": 700, "slnt": -15}'
# python FontOpsGetVariableInstanceClosestToCoordinates.py C:\Fonts\AnotherVariableFont.ttf '{"wght": 200}'
# python FontOpsGetVariableInstanceClosestToCoordinates.py /path/to/differentfont.otf '{"wdth": {"min": 75, "max": 125}, "wght": 400}'
# python FontOpsGetVariableInstanceClosestToCoordinates.py /path/to/specialfont.otf '{"opsz": 14, "ital": 1}'
# python FontOpsGetVariableInstanceClosestToCoordinates.py /path/to/complexfont.ttf '{"wght": 900, "wdth": {"min": 50, "max": 150}, "opsz": 12, "ital": {"min":0, "max":1}}'
