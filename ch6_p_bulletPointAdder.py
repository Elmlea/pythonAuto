#! python3
# bulletPointAdder.py - Adds Wikipedia bullet points to the start
# of each line of text on the clipboard.

# from Automate the Boring Stuff with Python
# 30 Jan 2020

import pyperclip
text = pyperclip.paste() ## NOTE: imagine this as 'pasting' into the variable

## NOTE: separate lines and add stars
lines = text.split('\n')
for i in range(len(lines)): # loop through all indices in the new 'lines' list
    lines[i] = '* ' + lines[i] # adds the stars

text = '\n'.join(lines)

pyperclip.copy(text)
