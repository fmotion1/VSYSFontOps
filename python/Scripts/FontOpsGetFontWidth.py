import sys
from sys import argv
from sys import exit
import json
from fontbro import Font

if len(argv)!=2:
    print("Usage: FontOpsGetFontWidth.py [FONT]")
    sys.exit(1)

font = Font(argv[1])
width = font.get_width()

print(json.dumps(width, indent=2))