import sys
from sys import argv
from sys import exit
import json
from fontbro import Font

if len(argv)!=2:
    print("Usage: fontbro_get_format.py [FONT]")
    sys.exit(1)


font = Font(argv[1])
weight = font.get_weight()
print(weight)