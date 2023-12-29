import fontforge
import sys
import os
from os import path

if len(sys.argv) < 2:
        print("Usage : {0} file.ttf".format(sys.argv[0]))
        exit(1)

input_file = sys.argv[1]
ttf_file = os.path.splitext(input_file)[0]+'.ttf'

def check_file(filePath):
    if path.exists(filePath):
        numb = 1
        while True:
            newPath = "{0}_{2}{1}".format(*path.splitext(filePath) + (numb,))
            if path.exists(newPath):
                numb += 1
            else:
                return newPath
    return filePath

safe_path = check_file(ttf_file)
font = fontforge.open(input_file)
font.generate(safe_path)
font.close()