import os
import sys
import pathlib
import json
from contextlib import redirect_stderr
from fontTools import ttLib
from fontmeta import FontMeta

# Check for commandline argument
# if len(sys.argv) == 1:
#     print('No argument was supplied.')
#     exit(0)

# fontfile = sys.argv[1]

fontfile = "C:\\Users\\futur\\Desktop\\Test\\PP Mori Bold.ttf"

# Python3 Program to check whether a
# given key already exists in a dictionary.

def checkKey(dic, key):
    if key in dic.keys():
        print("Present, ", end =" ")
        print("value =", dic[key])
    else:
        print("Not present")


def font_name(font_path, name_idx):
    font = ttLib.TTFont(font_path, ignoreDecompileErrors=True)
    with redirect_stderr(None):
        names = font['name'].names

    details = {}
    for x in names:
        if x.langID == 0 or x.langID == 1033:
            try:
                details[x.nameID] = x.toUnicode()
            except UnicodeDecodeError:
                details[x.nameID] = x.string.decode(errors='ignore')
    # details[4] = Full Name
    # details[1] = Family Name
    # details[2] = Style Name
    return details[name_idx]


ttLibFont = ttLib.TTFont(fontfile)
meta_instance = FontMeta(fontfile)
metadata = meta_instance.get_full_data()

print(metadata)


# fontFullName           = font_name(fontfile,4)
# fontFamily             = font_name(fontfile,1)
# fontStyle              = font_name(fontfile,2)
# fontVers               = metadata[5]['value'];
# fontVers               = fontVers.replace('Version ',"v")
# fontLang               = metadata[1]['language']['value'];
# fontUniqueID           = metadata[3]['value']
# fontPostscriptName     = metadata[6]['value']
# fontPostscriptEncoding = metadata[6]['encoding']['value']
# fontDesigner           = metadata[9]['value']
# fontLicenseURL         = metadata[14]['value']
# fontGlyphNum           = ttLibFont['maxp'].numGlyphs
# fontWidth              = ttLibFont['OS/2'].usWidthClass
# fontVendID             = ttLibFont['OS/2'].achVendID