import os
import sys
import pathlib
import json
from contextlib import redirect_stderr
from fontTools import ttLib
from fontmeta import FontMeta


def get_from_naming_table(font_path, name_idx):
    # https://learn.microsoft.com/en-us/typography/opentype/spec/name#name-ids
    # details[1] = Family Name
    # details[2] = Style Name
    # details[4] = Full Name

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
    return details[name_idx]

def get_full_naming_table(font_path):
    # https://learn.microsoft.com/en-us/typography/opentype/spec/name#name-ids
    # details[1] = Family Name
    # details[2] = Style Name
    # details[4] = Full Name

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

    json_formatted_str = json.dumps(details, indent=2)
    return json_formatted_str



def get_full_naming_table_fontmeta(font_file, indent_num=2):
    meta_instance = FontMeta(font_file)
    metadata = meta_instance.get_full_data()
    json_formatted_str = json.dumps(metadata, indent=indent_num)
    return json_formatted_str


def get_full_naming_table_fontmeta_streamlined(font_file, indent_num=2):
    meta_instance = FontMeta(font_file)
    metadata = meta_instance.get_data()
    json_formatted_str = json.dumps(metadata, indent=indent_num)
    return json_formatted_str


def get_font_name_full(font_path):
    return get_from_naming_table(font_path, 4)


def get_font_name_family(font_path):
    return get_from_naming_table(font_path, 1)


def get_font_name_style(font_path):
    return get_from_naming_table(font_path, 2)


def get_font_format(font_path):
    font = ttLib.TTFont(font_path, ignoreDecompileErrors=True)
    if 'glyf' in font:
        outlineFormat = "TrueType"
    elif 'CFF ' in font or 'CFF2' in font:
        outlineFormat = "OpenType/CFF"
    else:
        outlineFormat = "Unknown/Invalid"
    return outlineFormat
