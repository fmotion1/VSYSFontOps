import argparse
import sys
from fontbro import Font

def set_style_flags(font_path, bold, italic, underline, outline):
    """
    Sets the style flags, flags set to None will be ignored.

    :param font_path: Path to the font file.
    :param bold: The bold flag value.
    :type bold: bool or None
    :param italic: The italic flag value.
    :type italic: bool or None
    :param underline: The underline flag value.
    :type underline: bool or None
    :param outline: The outline flag value.
    :type outline: bool or None
    """
    font = Font(font_path)
    font.set_style_flags(bold=bold, italic=italic, underline=underline, outline=outline)

def main():
    parser = argparse.ArgumentParser(description='Set style flags on a font.')
    parser.add_argument('font_path', type=str, help='The path to the font file')
    parser.add_argument('--bold', type=lambda x: (str(x).lower() == 'true'), help='The bold flag value (True/False)', default=None)
    parser.add_argument('--italic', type=lambda x: (str(x).lower() == 'true'), help='The italic flag value (True/False)', default=None)
    parser.add_argument('--underline', type=lambda x: (str(x).lower() == 'true'), help='The underline flag value (True/False)', default=None)
    parser.add_argument('--outline', type=lambda x: (str(x).lower() == 'true'), help='The outline flag value (True/False)', default=None)

    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)

    args = parser.parse_args()

    # Set the style flags
    set_style_flags(args.font_path, args.bold, args.italic, args.underline, args.outline)
    print(f"Style flags updated for {args.font_path}")

if __name__ == "__main__":
    main()

# python FontOpsSetStyleFlags.py /path/to/fontfile.ttf --bold true
# python FontOpsSetStyleFlags.py /path/to/fontfile.ttf --bold true --italic true --underline false
# python FontOpsSetStyleFlags.py /path/to/fontfile.ttf --outline true
