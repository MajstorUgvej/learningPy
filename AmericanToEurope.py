#! /usr/bin/python3
import re, os, shutil
AmDateRegex = re.compile(r'''
                ^(.*?)
                ([01]?\d-)     # za mesece
                ([0123]?\d-)   # za dane
                (\d{4}          # za godine
                .*)$
''', re.VERBOSE)
os.chdir(os.path.abspath('./datum'))    # iz orginalnog u potrebni
for file in os.listdir():
    mo = AmDateRegex.search(file)
    if(mo != None):
        print('Date before:' + file)
        eur = mo.group(1) + mo.group(3) + mo.group(2) + mo.group(4)
        shutil.move(file,eur)

os.chdir(os.path.abspath('../')) # samo za mene da mi vrati u orginalni direktorijum