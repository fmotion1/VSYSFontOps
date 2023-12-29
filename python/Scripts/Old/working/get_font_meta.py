import os.path
import sys
from fontTools import ttLib
from fontmeta import FontMeta

print(sys.argv[0])

if len(sys.argv) > 2:
    print("Usage: Only one argument required: [FONT]")
    exit(1)

fontfile = sys.argv[1]
meta_instance = FontMeta(fontfile)
metadata = meta_instance.get_full_data()

print(metadata)

