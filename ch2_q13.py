type = "" # initialise the variable because it gets checked shortly

print("That's the variable initialised.") # so I know the program has started!

while ("for" or "while") not in type:
    type = input("Would you like to print your numbers using a FOR loop, or a WHILE loop? :>  ")

    if "for" in type:
        # for loop practice
        print("Here's a list of numbers!")
        for num in range (1,11):
            print(num)
        print("These numbers were brought to you using a for loop.")

    elif "while" in type:
        # using a while loop
        print("Have some numbers!")
        num = 1
        while num < 11:
            print(num)
            num += 1
        print("These ones were made using a while loop.")

    else:
        print("Be nice if you specified a loop type pls?")
        #as FOR or WHILE weren't entered, this will restart the external WHILE loop
