#! python3
# Take a list of lists, and print them out nicely!

myTable = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose'],
             ['please', 'help', 'me', 'Reddit!'],
             ['how', 'about', 'another', 'list']]
tableData = myTable # until it's changed to a function

colWidths = [0] * len(tableData)
colWidthsIndex = 0

for innerList in tableData:
    print("The list in use is: " + str(innerList))
    print("This equates to colWidths index " + str(colWidthsIndex))

    for element in innerList:
        print("Working on '" + element + "'")
        print("Checking the length of '" + element +"'")
        print("'" + element + "' is " + str(len(element)) + " characters long.\n")

        if len(element) > colWidths[colWidthsIndex]:
            colWidths[colWidthsIndex] = len(element)
            print("Updated colWidths: ", end='')
            print(colWidths)

    colWidthsIndex += 1

print()
print("Final Output".center((sum(colWidths) + len(colWidths)), '*'))

for y in range(len(tableData[0])):
    for x in range(len(tableData)):
        print(tableData[x][y].rjust(colWidths[x]), end = ' ')
    print()

print("*" * (sum(colWidths) + len(colWidths)))
