import argparse
import sys
from fontbro import Font

def clone_font(font_path):
    """
    Creates a new Font instance reading the same binary file.

    :param font_path: Path to the font file.
    :returns: Cloned Font instance.
    """
    font = Font(font_path)
    return font.clone()

def main():
    # Create the parser
    parser = argparse.ArgumentParser(description='Clone a font file into a new Font instance.')
    # Add an argument for the font path
    parser.add_argument('font_path', type=str, help='The path to the font file')
    
    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)
    
    # Parse the arguments
    args = parser.parse_args()

    # Clone the font and print a success message
    font_clone = clone_font(args.font_path)
    print(f"Font file cloned from: {args.font_path}")

if __name__ == "__main__":
    main()

# The script will create a clone of the specified font in memory and print a success
# message indicating the source of the cloned font. 

# python FontOpsCloneFont.py /path/to/fontfile.ttf
