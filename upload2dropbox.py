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

try:
    # connect to dropbox
    db_client = dropbox.Dropbox("zpAbOclWSRUAAAAAAAAEelZenv-Ae8W-zXeTeSUqdiVQNpb9bBbF3o8DHR3OVSGb")
    # open file
    item = "test123.txt"
    fileHandle = open(item, "rb")
    fileBytes = fileHandle.read()
    # upload file to dropbox
    upload_response = db_client.files_upload(fileBytes, "/" + item, autorename=True)
    print(upload_response)
except Exception as e:
    print(e)
finally:
    fileHandle.close()
