# this follows on from the description of string methods

while True: # an infinite loop!
    print("Enter your age:")
    age = input() # this takes input as a string
    if age.isdecimal(): # check if it's purely numbers
        break # exit the loop
    print("Please enter a number for your age.")
    # the final print statement COULD go in an else: clause

while True:
    print("Select a new password - letters and numbers only:")
    password = input()
    if password.isalnum(): # instead of always doing if/else, think of
        break # if clauses as self-contained?
    print("Passwords can only be alphanumeric.")
