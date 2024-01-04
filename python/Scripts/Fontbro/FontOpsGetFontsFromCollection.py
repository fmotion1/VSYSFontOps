import argparse
import sys
from fontbro import Font

def get_fonts_from_collection(collection_path):
    """
    Gets a list of Font objects from a font collection file (.ttc / .otc)

    :param collection_path: The filepath to the font collection.
    :returns: A list of Font objects.
    :rtype: list
    """
    return Font.from_collection(filepath=collection_path)

def save_fonts(fonts, output_font_path, overwrite):
    """
    Saves each font from the collection to the specified directory.

    :param fonts: A list of Font objects.
    :param output_font_path: The directory path where the fonts will be saved.
    :param overwrite: Boolean indicating whether to overwrite existing files.
    """
    for font in fonts:
        filename = font.get_filename()
        font.save(f"{output_font_path}/{filename}", overwrite)

def main():
    parser = argparse.ArgumentParser(description='Get fonts from a font collection file and save them.')
    parser.add_argument('collection_path', type=str, help='The path to the font collection file (.ttc / .otc)')
    parser.add_argument('output_font_path', type=str, help='The directory path where the fonts will be saved')
    parser.add_argument('--overwrite', type=lambda x: (str(x).lower() == 'true'), default=False, help='Whether to overwrite existing files (True/False)')

    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)

    args = parser.parse_args()
    fonts = get_fonts_from_collection(args.collection_path)
    save_fonts(fonts, args.output_font_path, args.overwrite)
    print(f"Fonts saved to {args.output_font_path} (overwrite={args.overwrite})")

if __name__ == "__main__":
    main()



# python FontOpsGetFontsFromCollection.py /path/to/fontcollection.ttc /path/to/save/fonts --overwrite true
# python FontOpsGetFontsFromCollection.py /path/to/fontcollection.ttc /path/to/save/fonts
# python FontOpsGetFontsFromCollection.py /path/to/fontcollection.ttc /path/to/save/fonts --overwrite true
# python FontOpsGetFontsFromCollection.py C:\Fonts\MyCollection.otc C:\Fonts\SavedFonts
# python /path/to/script/FontOpsGetFontsFromCollection.py /path/to/fontcollection.ttc /path/to/save/fonts
# python FontOpsGetFontsFromCollection.py /path/to/fontcollection.otc /otherpath/save/fonts --overwrite true
