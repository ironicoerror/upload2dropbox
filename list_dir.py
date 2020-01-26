#!/usr/bin/python

import os
from os.path import isdir, relpath

log_path = r"/home/rogx/repositories/upload2dropbox/temperature_logs/"
filelist = os.listdir(log_path)

for files in filelist:
    if os.path.isdir(log_path + files) is False:
        print(files + " is a file and will be uploaded")
    else:
        print(files + " is a directory and not uploaded")
