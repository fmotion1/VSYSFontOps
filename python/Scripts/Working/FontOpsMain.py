import os
import sys
import pathlib
import json
from sys import argv
from sys import exit
from fontbro import Font
from contextlib import redirect_stderr
from fontTools import ttLib
from fontmeta import FontMeta

if len(argv)!=2:
    print("Usage: font_info_all_in_one.py [FONT]")
    sys.exit(1)


def get_font_info(font_path):

    fontfile = font_path
    font = Font(fontfile)
    fontIsVariable = font.is_variable()
    fontFormat = font.get_format()

    ttLibFont = ttLib.TTFont(fontfile, ignoreDecompileErrors=True)

    variableInstances = {}
    if(fontIsVariable):
        family = ttLibFont["name"].getName(16, 3, 1, 0x409)
        if family is None:
            family = ttLibFont["name"].getName(1, 3, 1, 0x409)
        idx = 0
        for instance in ttLibFont["fvar"].instances:
            style = ttLibFont["name"].getName(instance.subfamilyNameID, 3, 1, 0x409)
            variableInstances[idx] = (f"{family} {style}")
            idx = idx + 1
    else:
        variableInstances = "None"

    numGlyphs = ttLibFont['maxp'].numGlyphs
    unitsPerEm = ttLibFont['head'].unitsPerEm

    PreferredFamily          = ttLibFont['name'].getDebugName(16)

    familyName               = ttLibFont['name'].getDebugName(1)
    styleName                = ttLibFont['name'].getDebugName(2)
    uniqueFontIdentifier     = ttLibFont['name'].getDebugName(3)
    fullName                 = ttLibFont['name'].getDebugName(4)
    fontVersion              = ttLibFont['name'].getDebugName(5)
    postScriptName           = ttLibFont['name'].getDebugName(6)
    typographicSubfamilyName = ttLibFont['name'].getDebugName(17)
    designer                 = ttLibFont['name'].getDebugName(9)
    vendorURL                = ttLibFont['name'].getDebugName(11)
    designerURL              = ttLibFont['name'].getDebugName(12)
    licenseDescription       = ttLibFont['name'].getDebugName(13)


    usWidthClass = ttLibFont['OS/2'].usWidthClass
    usWeightClass = ttLibFont['OS/2'].usWeightClass



    font_info = {
        "fontIsVariable": fontIsVariable,
        "variableInstances": variableInstances,
        "fontFormat": fontFormat,
        "numGlyphs": numGlyphs,
        "UPM": unitsPerEm,
        "postScriptName": postScriptName,
        "fontVersion": fontVersion,
        "familyName": familyName,
        "styleName": styleName,
        "fullName": fullName,
        "typographicFamilyName": typographicFamilyName,
        "typographicSubfamilyName": typographicSubfamilyName,
        "usWidthClass": usWidthClass,
        "usWeightClass": usWeightClass,
        "fontDesigner": designer,
        "vendorURL": vendorURL,
        "designerURL": designerURL,
        "licenseDescription": licenseDescription
    }
    print(json.dumps(font_info))
    # return font_info

if __name__ == '__main__':
    path = sys.argv[1]
    get_font_info(path)
    # print(json.dumps(info))  # Printing the info as a JSON string





