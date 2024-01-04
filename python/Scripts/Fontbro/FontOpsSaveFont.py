import argparse
import sys
from fontbro import Font

def save_font(font_path, filepath, overwrite):
    """
    Saves the font at filepath.

    :param font_path: Path to the font file.
    :param filepath: The filepath where the font will be saved. If None, the source filepath will be used.
    :param overwrite: If True, the source font file can be overwritten.
    :returns: The filepath where the font has been saved to.
    :rtype: str
    :raises ValueError: If the filepath is the same as the source font and overwrite is not allowed.
    """
    font = Font(font_path)
    return font.save(filepath=filepath if filepath != 'None' else None, overwrite=overwrite)

def main():
    parser = argparse.ArgumentParser(description='Save the font to a file.')
    parser.add_argument('font_path', type=str, help='The path to the font file')
    parser.add_argument('file_path', type=str, help='The filepath where to save the font, "None" for source filepath')
    parser.add_argument('--overwrite', action='store_true', help='Allow overwriting the file if it already exists')

    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)

    args = parser.parse_args()

    # Save the font and print the path where it's saved
    saved_font_path = save_font(args.font_path, args.file_path, args.overwrite)
    print(saved_font_path)

if __name__ == "__main__":
    main()
    

# python FontOpsSaveFont.py /path/to/original/fontfile.ttf /path/to/save/newfontfile.ttf
# python FontOpsSaveFont.py /path/to/fontfile.ttf /path/to/fontfile.ttf --overwrite
# python FontOpsSaveFont.py C:\Fonts\MyFont.otf C:\Fonts\Saved\MyFont_Modified.otf
# python /path/to/script/FontOpsSaveFont.py /path/to/fontfile.ttf /path/to/save/newfontfile.ttf
# python FontOpsSaveFont.py /path/to/fontfile.otf None --overwrite
