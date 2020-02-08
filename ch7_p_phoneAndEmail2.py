#! Python3
# *** Phone Number & Email Extractor ***
# Find all the phone numbers and emails in a long document.
# From Automate the Boring Stuff with Python

# 7 Feb 2020

# More verbose version, to make inner workings clearer

import pyperclip, re

# NOTE: Setup phone number regex

phoneRegex = re.compile(r"""
(\d{3}|\(\d{3}\))?             # area code
(\s|-|\.)?                     # separator
(\d{3})                        # first 3 digits
(\s|-|\.)                      # separator
(\d{4})                        # last 4 digits
(\s*(ext|x|ext.)\s*(\d{2,5}))? # extension
""", re.VERBOSE)

# NOTE: Setup email regex

emailRegex = re.compile(r"""(
[a-zA-Z0-9.%+-]+                # username
@                               # at symbol
[a-zA-Z0-9.-]+                  # domain name
(\.[a-zA-Z]{2,4})               # dot something
)""", re.VERBOSE)

# NOTE: Find matches in the clipboard text

print("\nStarting Phone & Email Extractor")
print("***\n")
print("Copying from the clipboard...")
text = str(pyperclip.paste()) # paste 'pastes' from the clipboard
print("Initialising a blank matches list...")
matches = [] # sets up an empty list

print("\nBeginning phone number search...")
for groups in phoneRegex.findall(text):
    print("Found " + str(groups[0]))
    print("The raw data found is " + str(groups))
    print("\nSplitting into component groups:")
    for index in range(1,8):
        print("Part "+ str(index) + ": " + str(groups[index]))

    print("\nCombining into set syntax...")
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    print(phoneNum)
    print("Checking for extension...")
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
        print("Extension found")
        print("phoneNum")
    else:
        print("No extension found.")
    print("\nAdding match to list of matches so far...")
    matches.append(phoneNum)
    print("\nCurrent matches:")
    print(matches)

print("\nBeginning email search...")
for groups in emailRegex.findall(text):
    print("Match found: " + str(groups[0]))
    print("Adding to list of matches so far...")
    matches.append(groups[0])
    print("\nCurrent matches: " + str(matches) + "\n")

# Copy results to the clipboard

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print("Matching Complete!\n")
    print("Copied to clipboard:")
    print('\n'.join(matches))
else:
    print("No phone numbers or email addresses found.")
