#! python3
# renameDates.py - Renames filennames with US MM-DD-YYY date format
# to European DD-MM-YYY

import shutil, os, re

# Create a regext that matches files with US date format.
datePattern = re.compile(r"""
^(.*?)                  # all text before the date
((0|1)?\d)-             # 1 or 2 digits for the month
((0|1|2|3)?\d)-         # 1 or 2 digits for the day
((19|20)\d\d)           # 4 digits for the year
(.*?)$                  # all text after the date
""", re.VERBOSE)

# loop over files in the working directory
for amerFilename in os.listdir('.'): # remember . means current dir!
    mo = datePattern.search(amerFilename)

# skip files with no date
    if mo == None:
        continue # remember to use this to restart loops

# get the different parts of the filenames
    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)

# form the EU style filename
    euroFilename = beforePart + dayPart + '-' + monthPart + '-' +yearPart + afterPart

# get the full, absolute file paths
    absWorkingDir = os.path.abspath('.')
    amerFilename = os.path.join(absWorkingDir, amerFilename)
    euroFilename = os.path.join(absWorkingDir, euroFilename)

# TODO: rename the files
    print("Renaming 's' to 's'..." % (amerFilename, euroFilename))
    # DEBUG: shutil.move(amerFilename, euroFilename)  
