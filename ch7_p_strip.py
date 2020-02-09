#! Python3
# Automate the Boring Stuff with Python
# Chapter 7 Project - RegEx Version of strip()

# 9 Feb 2020

# NOTE: Take an input for the main string and for the characters to strip
# maybe consider a backup of pyperclip?

# Strip whitespace with ^\s* and \s*$

import re, pyperclip

def stripWhite(string):
    stripWhiteLeft = re.compile(r'^\s*')
    stripWhiteRight = re.compile(r'\s*$')

    return stripWhiteRight.sub('', (stripWhiteLeft.sub('', string)))

def stripSpecific(string, chars):
    stripRegex = re.compile(chars)

    return stripRegex.sub('', string)

inputString = input("Please input the string to strip.  Press enter to copy from the clipboard :> ")
stripChars = input("Please input the characters to remove.  Press enter to strip white space :> ")

if inputString == "":
    inputString = pyperclip.paste()

print("The string input is \n\n" + "-" + inputString + "-" + "\n")

if stripChars == "":
    print("White space will be stripped from the beginning and end.\n")
    print("It will be copied to the clipboard. Output is: ")
    print(stripWhite(inputString))
    pyperclip.copy(stripWhite(inputString))

else:
    print("The characters to be removed are: " + stripChars + '\n')
    print("It will be copied to the clipboard. Output is: ")
    print(stripSpecific(inputString, stripChars))
    pyperclip.copy(stripSpecific(inputString, stripChars))