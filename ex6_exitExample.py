import sys # imports the sys module

while True: # sets up an infinite loop
    print("Type exit to exit.")
    response = input()
    if response == "exit": # don't forget ==!
        sys.exit() # only if exit is typed
    print("You typed " + response + ".")
    # program comes back to line 8 if the 'if' isn't true

# With no break statement, the prog will never end without sys.exit()
