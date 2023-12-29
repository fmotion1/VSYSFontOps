import os
import sys
import pathlib
from contextlib import redirect_stderr
from fontTools import ttLib

if len(sys.argv) > 2:
    print("Usage: Only one argument required: [FONT]")
    exit(1)

fontfile = sys.argv[1]
font = ttLib.TTFont(fontfile)
width = font['OS/2'].usWidthClass

print(width)