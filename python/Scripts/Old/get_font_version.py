import os
import sys
import pathlib
import json
from contextlib import redirect_stderr
from fontTools import ttLib
from fontmeta import FontMeta

# Check for commandline argument
if len(sys.argv) == 1:
    print('No argument was supplied.')
    exit(0)

fontfile = sys.argv[1]
ttLibFont = ttLib.TTFont(fontfile)

meta_instance = FontMeta(fontfile)
metadata = meta_instance.get_full_data()

fontVers = metadata[5]['value']

fontVers = fontVers.replace('Version ',"")

delim = ";"
parts = fontVers.split(delim, 1)

fontVers = parts[0]

print(fontVers)

