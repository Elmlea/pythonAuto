while True: # sets up an infinite loop
    print("Who are you?")
    name = input()
    if name != "Joe":
        continue # if wrong name entered, leap back to the start of the while loop
    print("Hello Joe, what is the password? (It is a fish)")
    password = input()
    if password == "swordfish":
        break # if the correct answer is given, jumps out of the while loop
print("Access granted!")
