from random import randint

name = input("Enter name :> ")
print("The first character is " + name[0])
randNumber = randint(0,(len(name)-1))
print("I've randomly chosen the character " + name[randNumber])
print("It was character number " + str(randNumber + 1))
print("I like to print the name vertically too!")

for i in name:
    print("*** " + i + " ***")
