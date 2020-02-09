#! Python3

# Strong Password Checker
# ATBSWP Ch 7 Project - 8 Feb 20

# NOTE: Generate multiple regexes, compare to each in turn?

import re

userPass = input("Please enter the password to check :> ")

paramsMet = [0,0,0,0]

passLength = re.compile(r'\w{8,}')
if bool(passLength.search(userPass)) == True:
    paramsMet[0] = 1

passUpper = re.compile(r'[A-Z]')
if bool(passUpper.search(userPass)) == True:
    paramsMet[1] = 1

passLower = re.compile(r'[a-z]')
if bool(passLower.search(userPass)) == True:
    paramsMet[2] = 1

passDigit = re.compile(r'\d')
if bool(passDigit.search(userPass)) == True:
    paramsMet[3] = 1

if paramsMet == [1,1,1,1]:
    print("The password meets all requirements.")

if paramsMet[0] == 0:
    print("Your password is not long enough.  It must be at least 8 characters.")
if paramsMet[1] == 0:
    print("Your password must contain at least one upper case character.")
if paramsMet[2] == 0:
    print("Your password must contain at least one lower case character.")
if paramsMet[3] == 0:
    print("Your password must contain at least one digit.")
