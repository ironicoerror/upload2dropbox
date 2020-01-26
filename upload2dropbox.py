#!/usr/bin/python3
"""
upload data to personal dropbox account
token: zpAbOclWSRUAAAAAAAAEelZenv-Ae8W-zXeTeSUqdiVQNpb9bBbF3o8DHR3OVSGb
app name: temperature_logs
permission: App Folder
app key: tl2zdb5oi7y1t6i
app secret: 0ts4ugff2lp57up
"""
import dropbox 
import os
from os.path import isdir
from shutil import move
import datetime

the_date = str(datetime.datetime.now())[0:10]
log_path = r"/home/rogx/repositories/upload2dropbox/temperature_logs/"
filelist = os.listdir(log_path)
filelist.remove(the_date.replace("-", "") + ".log") #do not copy todays log it might be changed 

try: 
    arc_path = log_path + "archive"
    os.mkdir(arc_path)
except FileExistsError:
    print("Archive already exists")
try:
    # connect to dropbox
    db_client = dropbox.Dropbox("zpAbOclWSRUAAAAAAAAEelZenv-Ae8W-zXeTeSUqdiVQNpb9bBbF3o8DHR3OVSGb")
    for files in filelist:
        if os.path.isdir(log_path + files) is False:
            print("Uploading: " + files)
            # open file
            fileHandle = open(log_path + files, "rb")
            fileBytes = fileHandle.read()
            # upload file to dropbox
            upload_response = db_client.files_upload(fileBytes, "/templ/" + files, autorename=True)
            move(log_path + files, arc_path)
            print(upload_response)
        else:
            print(files + " is a directory and not uploaded")
except Exception as e:
    print(e)
finally:
    fileHandle.close()
