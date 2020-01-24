catNames = [] # initialises the empty list

while True: # sets up an infinite loop
    print("Enter the name of cat number " + str(len(catNames) + 1) + "(or enter nothing to stop.)")
    name = input()
    if name == "":
        break
    catNames = catNames + [name] # adds name to the list

print("The cat names are:")
for name in catNames: # steps through catNames, pulling each element out as name
    print(" " + name)

#for name in catnames takes the catnames list, and every iteration allocates
# the next element to name
# if you did for name in range(len(catNames)) you would get a loop that
# iterates once for each value in catNames but doesn't pull them out to operate.
