#! Python3
# *** Phone Number & Email Extractor ***
# Find all the phone numbers and emails in a long document.
# From Automate the Boring Stuff with Python

# 7 Feb 2020

# NOTE: Program needs to do the following:
# - Get text off the clipboard
# - Find all phone numbers and email addresses in the text
# - Paste them back to the clipboard

# NOTE: Next Steps:
# - Use pyperclip to copy & paste strings
# - Create 2 x regex - one for phone numbers and one for emails
# - Find all matches, not just the first match, of both regexes
# - Neatly format the matched strings into a single string
# - Display a message if there are no matches

import pyperclip, re

# NOTE: Setup phone number regex

phoneRegex = re.compile(r"""(
(\d{3}|\(\d{3}\))?             # area code
(\s|-|\.)?                     # separator
(\d{3})                        # first 3 digits
(\s|-|\.)                      # separator
(\d{4})                        # last 4 digits
(\s*(ext|x|ext.)\s*(\d{2,5}))? # extension
)""", re.VERBOSE)

# NOTE: Setup email regex

emailRegex = re.compile(r"""(
[a-zA-Z0-9.%+-]+                # username
@                               # at symbol
[a-zA-Z0-9.-]+                  # domain name
(\.[a-zA-Z]{2,4})               # dot something
)""", re.VERBOSE)

# NOTE: Find matches in the clipboard text

text = str(pyperclip.paste()) # paste 'pastes' from the clipboard
matches = [] # sets up an empty list

for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)

for groups in emailRegex.findall(text):
    matches.append(groups[0])

# Copy results to the clipboard

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print("Copied to clipboard:")
    print('\n'.join(matches))
else:
    print("No phone numbers or email addresses found.")
