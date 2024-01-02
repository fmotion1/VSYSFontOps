import argparse
import sys
from fontbro import Font

def get_font_fingerprint(font_path, text):
    """
    Gets the font fingerprint: a hash calculated from an image representation of the font.
    Changing the text option affects the returned fingerprint.

    :param font_path: Path to the font file.
    :param text: The text used for generating the fingerprint.
    :returns: The fingerprint hash.
    :rtype: imagehash.ImageHash
    """
    font = Font(font_path)
    return font.get_fingerprint(text=text)

def main():
    # Create the parser
    parser = argparse.ArgumentParser(description='Get the fingerprint of a font file.')
    # Add an argument for the font path
    parser.add_argument('font_path', type=str, help='The path to the font file')
    # Add an optional argument for the text
    parser.add_argument('--text', type=str, default="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789", help='The text used for generating the fingerprint')
    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)
    # Parse the arguments
    args = parser.parse_args()

    # Get and print the font fingerprint
    fingerprint_hash = get_font_fingerprint(args.font_path, args.text)
    print(f"Fingerprint hash: {fingerprint_hash}")

if __name__ == "__main__":
    main()

# python FontOpsGetFontFingerprint.py /path/to/fontfile.ttf
# python FontOpsGetFontFingerprint.py /path/to/fontfile.ttf --text "Custom Text 123!"
# python FontOpsGetFontFingerprint.py C:\Fonts\MyFont.otf
# python /path/to/script/FontOpsGetFontFingerprint.py /path/to/fontfile.ttf --text "Another Example"
