#! python3
# p_passwordLocker.py - An insecure password locker program.
# Programmed by Mark from Automate the Boring Stuff with Python
# 29 Jan 2020

PASSWORDS = {'email': 'emailPassword', 'blog': 'blogPassword', 'luggage': '12345'}

import sys, pyperclip

if len(sys.argv) < 2: # sys.argv refers to the arguments passed when starting the program
    print("Usage: python3 p_passwordLocker.py [account] - copy account password.")
    # argv needs 2 arguments; the name of the program, and the account
    sys.exit()

account = sys.argv[1] # first command line argument is the account

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print("Password for " + account + " copied to clipboard.")
else:
    print("There is no account named " + account)

""" This doesn't have to be passwords.  It could be used to copy
and paste standard blocks of text or similar. """
