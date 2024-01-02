import argparse
import sys
from fontbro import Font

def get_fingerprint_match(font_path, other_font_path, tolerance, text):
    """
    Gets the fingerprint match between this font and another one
    by checking if their fingerprints are equal (difference <= tolerance).

    :param font_path: Path to the font file.
    :param other_font_path: Path to the other font file or a Font instance.
    :param tolerance: The diff tolerance.
    :param text: The text used for generating the fingerprint.
    :returns: A tuple containing the match info (match, diff, hash, other_hash).
    :rtype: tuple
    """
    font = Font(font_path)
    other_font = Font(other_font_path) if isinstance(other_font_path, str) else other_font_path
    return font.get_fingerprint_match(other=other_font, tolerance=tolerance, text=text)

def main():
    parser = argparse.ArgumentParser(description='Get the fingerprint match between two fonts.')
    parser.add_argument('font_path', type=str, help='The path to the font file')
    parser.add_argument('other_font_path', type=str, help='The path to the other font file')
    parser.add_argument('--tolerance', type=int, default=3, help='The diff tolerance, default 3')
    parser.add_argument('--text', type=str, default="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789", help='The text used for generating the fingerprint')

    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)

    args = parser.parse_args()

    # Get and print the fingerprint match
    match_info = get_fingerprint_match(args.font_path, args.other_font_path, args.tolerance, args.text)
    print(f"Match: {match_info[0]}, Diff: {match_info[1]}, Hash: {match_info[2]}, Other Hash: {match_info[3]}")

if __name__ == "__main__":
    main()

# python FontOpsGetFingerprintMatch.py /path/to/font1.ttf /path/to/font2.ttf
# python FontOpsGetFingerprintMatch.py /path/to/font1.ttf /path/to/font2.ttf --tolerance 5 --text "Custom Text 123!"
# python FontOpsGetFingerprintMatch.py C:\Fonts\FontOne.otf C:\Fonts\FontTwo.otf
# python /path/to/script/FontOpsGetFingerprintMatch.py /path/to/font1.ttf /path/to/font2.ttf --tolerance 10
