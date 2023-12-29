import sys
from sys import argv
from sys import exit
from fontbro import Font

if len(argv)!=3:
    print("Usage: FontOpsGetValueFromNameTable.py [FONT] [NAME-ID]")
    sys.exit(1)

font = Font(argv[1])
value = font.get_name(Font.NAME_SUBFAMILY_NAME)
print(value)
