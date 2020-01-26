#!/usr/bin/python

import os

print(os.curdir)
filelist = os.listdir()
print(filelist)

for files in filelist:
    print(files)