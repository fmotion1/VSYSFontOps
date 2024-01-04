import argparse
import json
import sys
from fontbro import Font

# Style Flags:
# https://docs.microsoft.com/en-us/typography/opentype/spec/head
# https://docs.microsoft.com/en-us/typography/opentype/spec/os2#fsselection
# STYLE_FLAG_REGULAR   = "regular"
# STYLE_FLAG_BOLD      = "bold"
# STYLE_FLAG_ITALIC    = "italic"
# STYLE_FLAG_UNDERLINE = "underline"
# STYLE_FLAG_OUTLINE   = "outline"
# STYLE_FLAG_SHADOW    = "shadow"
# STYLE_FLAG_CONDENSED = "condensed"
# STYLE_FLAG_EXTENDED  = "extended"


def get_variable_instance_by_style_name(font_path, style_name):
    """
    Gets the variable instance by style name.

    :param font_path: Path to the font file.
    :param style_name: The style name to match.
    :returns: The variable instance matching the given style name.
    :rtype: dict or None
    """
    font = Font(font_path)
    return font.get_variable_instance_by_style_name(style_name)

def main():
    parser = argparse.ArgumentParser(description='Get a variable instance by style name from a font.')
    parser.add_argument('font_path', type=str, help='The path to the font file')
    parser.add_argument('style_name', type=str, help='The style name to match')
    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)
    args = parser.parse_args()

    # Retrieve and print the variable instance
    instance = get_variable_instance_by_style_name(args.font_path, args.style_name)
    print(json.dumps(instance, indent=2))

if __name__ == "__main__":
    main()


# python FontOpsGetVariableInstanceByStyleName.py /path/to/fontfile.ttf Bold
# python FontOpsGetVariableInstanceByStyleName.py /path/to/fontfile.ttf Italic
# python FontOpsGetVariableInstanceByStyleName.py /path/to/anotherfontfile.otf Condensed
# python FontOpsGetVariableInstanceByStyleName.py C:\Fonts\MyVariableFont.otf BoldItalic
