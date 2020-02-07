#!/usr/bin/python3

import dropbox 
import os
from os.path import isdir
from shutil import move
import datetime

the_date = str(datetime.datetime.now())[0:10]
log_path = r"/home/pi/Desktop/temperature_logs/waeschekeller_ug/"
status_path = r"/home/pi/Desktop/"
filelist = os.listdir(log_path)
status_file_list = os.listdir(status_path)
print("Timestamp: " + str(datetime.datetime.now())[0:19])
try: 
    archive_path = log_path + "archive"
    os.mkdir(archive_path)
except FileExistsError:
    pass
try:
    # connect to dropbox
    db_client = dropbox.Dropbox("zpAbOclWSRUAAAAAAAAEelZenv-Ae8W-zXeTeSUqdiVQNpb9bBbF3o8DHR3OVSGb")
    print("Starting handle for templogs: ")
    count = 0
    for log_file in filelist:
        if os.path.isdir(log_path + log_file) is False:
            try:
                print("Uploading: " + log_file)
                # open templog
                log_file_handle = open(log_path + log_file, "rb")
                log_file_bytes = log_file_handle.read()
                # upload tempplog to dropbox
                log_file_upload_response = db_client.files_upload(log_file_bytes, "/waeschekeller_ug/" + log_file, autorename=True, mode=dropbox.files.WriteMode.overwrite)
                print(log_file_upload_response)
                if the_date.replace("-", "") in log_file:
                    print("todays templog has been updated.")
                else:
                    move(log_path + log_file, archive_path)
                    count += 1
            except Exception as e:
                print("Following error with file: " + log_file)
                print(e)
                count -= 1 
            finally:
                log_file_handle.close()
    print(str(count) + " templog_files have been uploaded to Dropbox.")
    print("Starting handle for statuslogs: ")
    count = 0
    for status_file in status_file_list:
        if os.path.isdir(status_path + status_file) is False:
            if "last_" in status_file:
                count += 1
                try:
                    # open statuslog
                    print("Uploading status file :" + status_file)
                    status_file_handle = open(status_path + status_file, "rb")
                    status_file_bytes = status_file_handle.read()
                    # upload statuslog to dropbox
                    status_file_upload_response = db_client.files_upload(status_file_bytes, "/" + status_file, autorename=True, mode=dropbox.files.WriteMode.overwrite)
                    print(status_file_upload_response)
                except Exception as e:
                    print("Following error with file: " + status_file)
                    print(e)
                    count -= 1
                finally:
                    status_file_handle.close()
    print(str(count) + " statuslog_files have been updated.")
except Exception as e:
    print(e)
