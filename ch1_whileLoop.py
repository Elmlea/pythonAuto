# another quick test
# Use a while loop only if you want to keep looping until something happens.

spam = 0
if spam < 5:
    print("Hello world")
    spam += 1

eggs = 0
while eggs < 5:
    print("Eggs " + str(eggs))
    eggs += 1

name = ""
while name != "your name":
    print("Please type your name.")
    name = input(":> ")
print("Thank you!")
