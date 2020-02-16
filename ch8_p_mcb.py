#! python3
# mcb.pyw - Saves and loads pieces of text to the clipboard
# Usage:
# python3 mcb.pyw save <keyword> - saves clipboard to keyboard
# python3 mcb.pyw <keyword> - loads keyword to clipboard
# python3 mcb.pyw list - loads all keywords to clipboard

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'del':
    del mcbShelf[sys.argv[2]]
elif len(sys.argv) == 2:
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
mcbShelf.close()
