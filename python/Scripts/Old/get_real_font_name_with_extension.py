import os
import sys
import pathlib
from contextlib import redirect_stderr
from fontTools import ttLib

# Check for commandline argument
if len(sys.argv) == 1:
    print('No argument was supplied.')
    exit(0)


def font_name(font_path):
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
    return details[4]


dirname = os.path.dirname(os.path.abspath(sys.argv[1]))
originalfile = os.path.abspath(sys.argv[1])
originalext = pathlib.Path(sys.argv[1]).suffix
newfilename = font_name(sys.argv[1]) + originalext
newfile = os.path.join(dirname, newfilename)

print(newfilename)
