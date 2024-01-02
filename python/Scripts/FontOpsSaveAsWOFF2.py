import argparse
import sys
from fontbro import Font

def save_as_woff2(font_path, filepath, overwrite):
    """
    Saves font as woff2.

    :param font_path: Path to the font file.
    :param filepath: The filepath where the woff2 file will be saved.
    :param overwrite: If True, the font file can be overwritten.
    :returns: The filepath where the font has been saved to.
    :rtype: str
    """
    font = Font(font_path)
    return font.save_as_woff2(filepath, overwrite)

def main():
    parser = argparse.ArgumentParser(description='Save the font as WOFF2 format.')
    parser.add_argument('font_path', type=str, help='The path to the font file')
    parser.add_argument('file_path', type=str, help='The filepath where to save the WOFF2 file')
    parser.add_argument('--overwrite', type=bool, default=False, help='Allow overwriting the file if it already exists (True/False)')

    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)
        
    args = parser.parse_args()

    # Save the font as WOFF2 and print the path where it's saved
    saved_font_path = save_as_woff2(args.font_path, args.file_path, args.overwrite)
    print(saved_font_path)

if __name__ == "__main__":
    main()

# python FontOpsSaveAsWOFF2.py /path/to/fontfile.ttf /path/to/save/fontfile.woff2
# python FontOpsSaveAsWOFF2.py /path/to/fontfile.ttf /path/to/save/fontfile.woff2 --overwrite True
# python FontOpsSaveAsWOFF2.py C:\Fonts\MyFont.otf C:\Fonts\MyFont.woff2
# python /path/to/script/FontOpsSaveAsWOFF2.py /path/to/fontfile.ttf /path/to/save/fontfile.woff2
# python FontOpsSaveAsWOFF2.py /path/to/fontfile.otf /otherpath/save/fontfile.woff2 --overwrite False
