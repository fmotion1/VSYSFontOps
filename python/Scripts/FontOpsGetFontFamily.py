import argparse
import sys
from sys import argv
from sys import exit
from fontbro import Font

if len(argv)!=2:
    print("Usage: FontOpsGetFontFamily.py [FONT]")
    sys.exit(1)

def get_font_family_name(font_path):
    try:
        # Load the font using FontBro
        font = Font(font_path)
        
        # Retrieve the family name
        value = font.get_family_name()
        
        # Return the value or a message if not found
        return value or f"No family name found."
    except Exception as e:
        return f"An error occurred: {e}"

def main():
    # Create argument parser
    parser = argparse.ArgumentParser(description='Retrieves the family name by parsing the name records with priority order (16, 21, 1).')

    # Add arguments for the font file and name ID
    parser.add_argument('font_file', type=str, help='Path to the font file')

    # Parse arguments
    args = parser.parse_args()

    # Retrieve and print the value for the specified name ID
    family_name = get_font_family_name(args.font_file)
    print(family_name)


if __name__ == "__main__":
    main()

