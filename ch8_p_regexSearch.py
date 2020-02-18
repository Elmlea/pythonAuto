#! python3

# Regex Search Project
# Automate the Boring Stuff with Python, Chapter 8
# 17 Feb 20

# Opens all the text files in a folder, and searches each one for
# a match to a user-entered text string, printing the results to screen.

import os, pprint, re

print("Regex Search")
searchString = input("Please enter the string to search for :> ")
searchRegEx = re.compile(searchString)
print("\nString received.  Now searching " + os.getcwd() + " for your requested string.")

print("\nListing directory contents: ")
fileList = os.listdir(os.getcwd())
pprint.pprint(fileList)

print("\nInitialising list of results & successful matches:")
resultsList = []
matchList = []
print("\nSearching for text files: ")
textFileRegex = re.compile('txt')
for file in fileList:
    if textFileRegex.search(file) != None:
        print(file + ' found!')
        resultsList.append(file)

print("\nDisplaying results found: ")
pprint.pprint(resultsList)

for result in resultsList:
    print("\nNow opening " + result)
    resultFileObj = open(result, 'r')
    textData = resultFileObj.read()

    print("\nSearching the file for your string:")
    matchObj = searchRegEx.search(textData)
    if matchObj == None:
        print("No match found")
    elif matchObj != None:
        print("MATCH FOUND!")
        print("Your string\n" + '\'' + searchString + '\'' + "\nwas found in the file " + result)
        matchList.append(result)

print("\nSearch complete")
print("Your string\n" + '\'' + searchString + '\'' + "\nwas found in the following " + str(len(matchList)) + " file(s):")
pprint.pprint(matchList)
