import sys
from sys import argv
from sys import exit
from fontbro import Font

if len(argv)!=2:
    print("Usage: FontOpsGetFontFormat.py [FONT]")
    sys.exit(1)

font = Font(argv[1])
format = font.get_format()
print(format)

