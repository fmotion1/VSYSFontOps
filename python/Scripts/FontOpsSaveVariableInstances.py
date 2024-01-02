import argparse
import json
import sys
from fontbro import Font

def save_variable_instances(font_path, dirpath, woff2, woff, overwrite, options):
    """
    Save all instances of a variable font to specified directory in one or more format(s).

    :param font_path: Path to the font file.
    :param dirpath: The directory path where the instances will be saved.
    :param woff2: Whether to save instances also in WOFF2 format.
    :param woff: Whether to save instances also in WOFF format.
    :param overwrite: Whether to overwrite existing files in the directory.
    :param options: Additional options to be passed to the instancer.
    :returns: A list containing dictionaries for each saved instance.
    :raises TypeError: If the font is not a variable font.
    """
    font = Font(font_path)
    return font.save_variable_instances(dirpath, woff2=woff2, woff=woff, overwrite=overwrite, **options)

def main():
    parser = argparse.ArgumentParser(description='Save all instances of a variable font.')
    parser.add_argument('font_path', type=str, help='The path to the font file')
    parser.add_argument('dirpath', type=str, help='The directory path where the instances will be saved')
    parser.add_argument('--woff2', action='store_true', default=True, help='Save in WOFF2 format')
    parser.add_argument('--woff', action='store_true', default=True, help='Save in WOFF format')
    parser.add_argument('--overwrite', action='store_true', default=True, help='Overwrite existing files')
    parser.add_argument('--options', type=json.loads, default={}, help='Additional options as a JSON string')

    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)

    args = parser.parse_args()

    saved_fonts = save_variable_instances(args.font_path, args.dirpath, args.woff2, args.woff, args.overwrite, args.options)
    print(saved_fonts)

if __name__ == "__main__":
    main()


# python FontOpsSaveVariableInstances.py /path/to/fontfile.ttf /path/to/save/dir --woff2 --woff
# python FontOpsSaveVariableInstances.py /path/to/fontfile.ttf /path/to/save/dir --woff --overwrite False
# python FontOpsSaveVariableInstances.py /path/to/fontfile.ttf /path/to/save/dir --woff2 --options '{"someOption": "someValue"}'
# python FontOpsSaveVariableInstances.py C:\Fonts\MyVariableFont.otf C:\Fonts\SavedInstances --woff2 --woff
# python /path/to/script/FontOpsSaveVariableInstances.py /path/to/fontfile.ttf /path/to/save/dir --woff
