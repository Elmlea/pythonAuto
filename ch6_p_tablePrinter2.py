#! python3
 # Take a list of lists, and print them out nicely!

myTable = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def tablePrinter(tableData):

    colWidths = [0] * len(tableData)

    for i in range(len(tableData)):
        for j in range(len(tableData[i])):
            if len(tableData[i][j]) > colWidths[i]:
                colWidths[i] = len(tableData[i][j])

    for y in range(len(tableData[0])): # y is the length of the first nested list
        for x in range(len(tableData)): # x is the number of lists
            print(tableData[x][y].rjust(colWidths[x]), end = ' ')
        print()
    ## BUG: This assumes all the nested lists are the same length.
    ## BUG: Can that be changed...?

tablePrinter(myTable)
