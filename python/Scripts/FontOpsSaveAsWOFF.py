import argparse
import sys
from fontbro import Font

def save_as_woff(font_path, filepath, overwrite):
    """
    Saves font as woff.

    :param font_path: Path to the font file.
    :param filepath: The filepath where the woff file will be saved.
    :param overwrite: If True, the font file can be overwritten.
    :returns: The filepath where the font has been saved to.
    :rtype: str
    """
    font = Font(font_path)
    return font.save_as_woff(filepath, overwrite)

def main():
    parser = argparse.ArgumentParser(description='Save the font as WOFF format.')
    parser.add_argument('font_path', type=str, help='The path to the font file')
    parser.add_argument('file_path', type=str, help='The filepath where to save the WOFF file')
    parser.add_argument('--overwrite', action='store_true', help='Allow overwriting the file if it already exists')
    
    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)
        
    args = parser.parse_args()

    # Save the font as WOFF and print the path where it's saved
    saved_font_path = save_as_woff(args.font_path, args.file_path, args.overwrite)
    print(saved_font_path)

if __name__ == "__main__":
    main()


# python FontOpsSaveAsWOFF.py /path/to/fontfile.ttf /path/to/save/fontfile.woff
# python FontOpsSaveAsWOFF.py /path/to/fontfile.ttf /path/to/save/fontfile.woff --overwrite
# python FontOpsSaveAsWOFF.py C:\Fonts\MyFont.otf C:\Fonts\MyFont.woff
# python /path/to/script/FontOpsSaveAsWOFF.py /path/to/fontfile.ttf /path/to/save/fontfile.woff
# python FontOpsSaveAsWOFF.py /path/to/fontfile.otf /otherpath/save/fontfile.woff --overwrite
