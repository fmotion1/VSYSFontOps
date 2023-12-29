import os
import sys
import pathlib
import json
import lib.fonthelpers as fhelpers
from contextlib import redirect_stderr

# Check for commandline argument
# if len(sys.argv) == 1:
#     print('No argument was supplied.')
#     exit(0)

# fontfile = sys.argv[1]

fontfile = r"C:\Users\futur\Desktop\Test\PP Mori Bold.ttf"

print(fhelpers.get_full_naming_table_fontmeta(fontfile))