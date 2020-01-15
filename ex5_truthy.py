name = "" # establish name as a blank variable

while not name: # blank variables are considered FALSE
    print("Enter your name")
    name = input() # when a value for name goes here, name is no longer FALSE

print("How many guests will you have?")
numOfGuests = int(input())

if numOfGuests: # this is like saying "if numOfGuests has a valid value".  Zero is considered false, any number is considered true.
    print("Be sure to have enough room for all those guests!")

print("done!")
