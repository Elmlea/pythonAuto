import zipfile, os

exampleZip = zipfile.ZipFile('ziptest.zip')
print(exampleZip.namelist())

zipInfo = exampleZip.getinfo('ziptest.txt')
print(zipInfo.file_size)
print(zipInfo.compress_size)

print("Compressed file is %sx smaller!" % (round(zipInfo.file_size / zipInfo.compress_size, 2)))
# use exampleZip.extractall() to open the archive
# to open to a folder, exampleZip.extractall('/Users/markwharry')
# extract a single file with exampleZip.extract('ziptest.txt', '/Users/markwharry')
# folders will be created if they don't exist.
# This method returns an absolute path.
exampleZip.close()

# To create a zip, we open it like any other file to create a zipfile object
newZip = zipfile.ZipFile('newZip.zip', 'a') # use the same formatting as writing to any file
newZip.write('_dictionaries.py', compress_type=zipfile.ZIP_DEFLATED)
newZip.close()
