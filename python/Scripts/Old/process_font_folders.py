import os
import sys
import pathlib
import json
from contextlib import redirect_stderr
from fontTools import ttLib
from fontmeta import FontMeta

try:
    directory_name=sys.argv[1]
except:
    print('Please pass directory_name')

obj = os.scandir(directory_name)

for entry in obj :
    if entry.is_file():
        first_file = entry.name
        file_extension = pathlib.Path(first_file).suffix
        break
    
full_font_file = os.path.join(directory_name, first_file)


fontfile = full_font_file
ttLibFont = ttLib.TTFont(fontfile)
meta_instance = FontMeta(fontfile)
metadata = meta_instance.get_full_data()
fontVers = metadata[5]['value']
fontVers = fontVers.replace('Version ',"")
delim = ";"
parts = fontVers.split(delim, 1)
font_version = parts[0]

os.rename(directory_name,directory_name + " " + font_version)

