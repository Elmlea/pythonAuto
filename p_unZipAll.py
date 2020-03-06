#! python3
# p_unZipAll.py - a short program to unzip all archives in a directory
# and delete the original files

import zipfile, os, send2trash, re

# Establish the zip checking regex
zipCheck = re.compile(r'\w*.zip$')

# Get a list of files in the directory
for root, dirs, files in os.walk(os.getcwd()):
    for eachFile in files:
        if zipCheck.search(eachFile) != None:
            print(eachFile + " is a zip, and will be unpacked and deleted.")
            print("It is at " + str(os.path.abspath(eachFile)))
            fileWithPath = os.path.abspath(eachFile)
            currentZip = zipfile.ZipFile(fileWithPath, 'r')
            print("Loaded " + eachFile + " into a zip object")
            print("Extracting...")
            # currentZip.extractall()
            print("Closing...")
            # currentZip.close()
            print("Deleting " + eachFile)
            # send2trash.send2trash(eachFile)
