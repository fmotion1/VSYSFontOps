#!/usr/bin/env python3
import os
import io
import sys
from pathlib import Path
from typing import List
from sys import argv

import cchardet as chardet
from fontTools.ttLib import TTCollection
from fontTools.ttLib import TTFont
from fontTools.ttLib.tables._n_a_m_e import NameRecord
from fontTools.ttLib.tables._n_a_m_e import table__n_a_m_e as NameTable


PREFERRED_IDS = (
    (3, 1, 0x0C04),
    (3, 1, 0x0804),
    (3, 1, 0x0404),
    (3, 1, 0x0411),
    (1, 0, 0),
)

FAMILY_RELATED_IDS = dict(
    LEGACY_FAMILY=1,
    TRUETYPE_UNIQUE_ID=3,
    FULL_NAME=4,
    POSTSCRIPT_NAME=6,
    PREFERRED_FAMILY=16,
    WWS_FAMILY=21,
)
PREFERRED_NAME_IDS = (
    FAMILY_RELATED_IDS["FULL_NAME"],
    FAMILY_RELATED_IDS["POSTSCRIPT_NAME"],
    FAMILY_RELATED_IDS["PREFERRED_FAMILY"],
    FAMILY_RELATED_IDS["LEGACY_FAMILY"],
)


def decode_name(name: NameRecord) -> str:
    try:
        return name.toUnicode().strip()
    except:
        raw = name.toBytes()
        guess = chardet.detect(raw)
        return raw.decode(guess["encoding"]).strip()


def get_current_family_name(table: NameTable) -> str:
    for plat_id, enc_id, lang_id in PREFERRED_IDS:
        for name_id in PREFERRED_NAME_IDS:
            family_name_rec = table.getName(
                nameID=name_id, platformID=plat_id, platEncID=enc_id, langID=lang_id
            )
            if family_name_rec:
                return decode_name(family_name_rec)
    for name_id in PREFERRED_NAME_IDS:
        results: List[str] = []
        for name_record in table.names:
            if name_record.nameID == name_id:
                results.append(decode_name(name_record))
        if results:
            return sorted(results, key=len)[-1]
    raise ValueError("family name not found; can't add suffix")


def get_font_name(font: TTFont):
    return get_current_family_name(font["name"])


def print_font_name(filepath: Path) -> None:
    font = TTFont(str(filepath.resolve()))
    return get_font_name(font)


def main() -> None:
    path = argv[1]
    new_font_name = print_font_name(Path(path))
    print(new_font_name)


if __name__ == "__main__":
    main()