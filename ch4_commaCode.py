# This program should take a list, and print all the values separated with commas then an 'and'

spam = ["apples", "bananas", "cats", "dogs"]

def commaCode(chosenList):
    for i in range(len(spam) - 1):
        print(spam[i] + ",", end = " ")
    print("and " + spam[-1])

commaCode(spam)
