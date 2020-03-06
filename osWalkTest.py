import os

for folderName, subfolders, files in os.walk(os.getcwd()):
    print("Current folder: " + folderName)

    for subfolder in subfolders:
        print("Found subfolder: " + subfolder)

        for filename in files:
            print("Found file: " + filename)
