import argparse
import sys
from fontbro import Font

# Style Flags:
# https://docs.microsoft.com/en-us/typography/opentype/spec/head
# https://docs.microsoft.com/en-us/typography/opentype/spec/os2#fsselection
# STYLE_FLAG_REGULAR = "regular"
# STYLE_FLAG_BOLD = "bold"
# STYLE_FLAG_ITALIC = "italic"
# STYLE_FLAG_UNDERLINE = "underline"
# STYLE_FLAG_OUTLINE = "outline"
# STYLE_FLAG_SHADOW = "shadow"
# STYLE_FLAG_CONDENSED = "condensed"
# STYLE_FLAG_EXTENDED = "extended"

# _STYLE_FLAGS = {
#     STYLE_FLAG_REGULAR: {"bit_head_mac": None, "bit_os2_fs": 6},
#     STYLE_FLAG_BOLD: {"bit_head_mac": 0, "bit_os2_fs": 5},
#     STYLE_FLAG_ITALIC: {"bit_head_mac": 1, "bit_os2_fs": 0},
#     STYLE_FLAG_UNDERLINE: {"bit_head_mac": 2, "bit_os2_fs": None},
#     STYLE_FLAG_OUTLINE: {"bit_head_mac": 3, "bit_os2_fs": 3},
#     STYLE_FLAG_SHADOW: {"bit_head_mac": 4, "bit_os2_fs": None},
#     STYLE_FLAG_CONDENSED: {"bit_head_mac": 5, "bit_os2_fs": None},
#     STYLE_FLAG_EXTENDED: {"bit_head_mac": 6, "bit_os2_fs": None},
# }
# _STYLE_FLAGS_KEYS = _STYLE_FLAGS.keys()


def set_style_flag(font_path, flag_key, value, output_font_path, output_overwrite):
    """
    Sets the style flag and saves the font.

    :param font_path: Path to the font file.
    :param flag_key: The flag key (e.g., Font.STYLE_FLAG_BOLD).
    :param value: The value (True/False).
    :param output_font_path: Path to save the modified font file.
    :param output_overwrite: Whether to overwrite the file if it already exists.
    
    """
    font = Font(font_path)
    font.set_style_flag(flag_key, value)
    font.save(output_font_path, output_overwrite)

def main():
    parser = argparse.ArgumentParser(description='Set a style flag on a font and save it.')
    parser.add_argument('font_path', type=str, help='The path to the font file')
    parser.add_argument('flag_key', type=str, help='The flag key (e.g., "STYLE_FLAG_BOLD")')
    parser.add_argument('value', type=lambda x: (str(x).lower() == 'true'), help='The value (True/False)')
    parser.add_argument('output_font_path', type=str, help='The path to save the modified font file')
    parser.add_argument('--output_overwrite', type=lambda x: x.lower() == 'true', default=False, help='Whether to overwrite the file if it already exists (True/False)')

    if len(sys.argv)==1:
        parser.print_help(sys.stderr)
        sys.exit(1)

    args = parser.parse_args()

    # Convert flag_key to the actual Font attribute
    flag_key = getattr(Font, args.flag_key, None)
    if flag_key is None:
        print(f"Invalid flag key: {args.flag_key}")
        sys.exit(1)

    # Set the style flag and save the font
    set_style_flag(args.font_path, flag_key, args.value, args.output_font_path, args.output_overwrite)
    print(f"Set {args.flag_key} to {args.value} and saved to '{args.output_font_path}' (overwrite={args.output_overwrite})")

if __name__ == "__main__":
    main()


# python FontOpsSetStyleFlag.py /path/to/fontfile.ttf STYLE_FLAG_BOLD true /path/to/save/newfontfile.ttf
# python FontOpsSetStyleFlag.py /path/to/fontfile.ttf STYLE_FLAG_ITALIC true /path/to/save/newfontfile.ttf --output_overwrite true
# python FontOpsSetStyleFlag.py C:\Fonts\MyFont.otf STYLE_FLAG_UNDERLINE false C:\Fonts\Saved\MyFont_Modified.otf
# python /path/to/script/FontOpsSetStyleFlag.py /path/to/fontfile.ttf STYLE_FLAG_EXTENDED true /path/to/save/newfontfile.ttf --output_overwrite false
# python FontOpsSetStyleFlag.py /path/to/fontfile.otf STYLE_FLAG_CONDENSED true /otherpath/save/condensedfont.otf --output_overwrite true
