import sys
from sys import argv
from sys import exit
import json
from fontbro import Font

if len(argv)!=2:
    print("Usage: FontOpsIsVariableFont.py [FONT]")
    sys.exit(1)

font = Font(argv[1])
variable = font.is_variable()
print(variable)