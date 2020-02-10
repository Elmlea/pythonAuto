#! Python3
# Automate the Boring Stuff with Python
# Chapter 7 Project - RegEx Version of strip()

# 9 Feb 2020

# NOTE: Take an input for the main string and for the characters to strip
# maybe consider a backup of pyperclip?

import re, pyperclip

def stripWhite(string):
# This function takes a string input, then defines 2 regexes
# to identify whitespace at the beginning and end of the string.

    stripWhiteLeft = re.compile(r'^\s*')
    stripWhiteRight = re.compile(r'\s*$')

    return stripWhiteRight.sub('', (stripWhiteLeft.sub('', string)))

def stripSpecific(string, chars):
# This sets up a simple regex to look for the character
# string that has been input and removes it.

    stripRegex = re.compile(chars)

# TODO: Can you change the regex so it takes EACH character...?
    return stripRegex.sub('', string)

# NOTE: Main body starts here.  We take 2 inputs; hitting return will revert to defaults
inputString = input("Please input the string to strip.  Press enter to copy from the clipboard :> ")
stripChars = input("Please input the characters to remove.  Press enter to strip white space :> ")

if inputString == "": # If return is pressed, it pulls from pyperclip
    inputString = pyperclip.paste()

# NOTE: Regardless of where the input comes from, it is displayed.  The '-'
# characters are used to show where whitespace currently exists.
print("The string input is \n\n" + "-" + inputString + "-" + "\n")

if stripChars == "":
# This section is used if the user hits return when asked what to cut.
# It defaults to whitespace; an explanation is printed, and then it
# runs the appropriate function, prints the output, and copies to clipboard.

    print("White space will be stripped from the beginning and end.\n")
    print("It will be copied to the clipboard. Output is: ")
    print(stripWhite(inputString))
    pyperclip.copy(stripWhite(inputString))

else:
# If the user specifies chars to remove, this section confirms the characters
# and explains what will happen with the output.  It is then printed and
# copied to clipboard.
    print("The characters to be removed are: " + stripChars + '\n')
    print("It will be copied to the clipboard. Output is: ")
    print(stripSpecific(inputString, stripChars))
    pyperclip.copy(stripSpecific(inputString, stripChars))
