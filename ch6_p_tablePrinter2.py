#! python3
 # Take a list of lists, and print them out nicely!

myTable = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def tablePrinter(tableData):

    ## NOTE: initialise colWidths as a list of 0 integers for each list
    ## NOTE: entry in tableData
    colWidths = [0] * len(tableData)

    ## NOTE: iterate over the number of entries in tableData
    ## NOTE: we specify the range of the length of the list because we want to
    ## NOTE: iterate a number of times; NOT perform operations on the list items.
    ## NOTE: If we tried 'for i in tableData', it's not iterable.
    for i in range(len(tableData)):

        ## NOTE: Now we do the same for the list that's within the master list.
        ## NOTE: This will set up a loop that acts for the number of items
        ## NOTE: in the nested list.
        for j in range(len(tableData[i])):

            ## NOTE: i is the item within tableData, j is the item within that nested list.
            ## NOTE: so we can look at each individual item using [i][j], and compare
            ## NOTE: its length to the colWidths entry that matches the list index.
            if len(tableData[i][j]) > colWidths[i]:

                ## NOTE: sets the longest string's length as the appropriate
                ## NOTE: column width.
                colWidths[i] = len(tableData[i][j])


    ## NOTE: We use the same looping, but reversed, as the book wants us to print
    ## NOTE: in the order [0][0], [1][0], [2][0]; hence the first digit must be
    ## NOTE: iterated through on the nested for statement below.
    for y in range(len(tableData[0])): # y is the length of the first nested list
        for x in range(len(tableData)): # x is the number of lists
            print(tableData[x][y].rjust(colWidths[x]), end = ' ')
        print()
    ## BUG: This assumes all the nested lists are the same length.
    ## BUG: Can I change for y in range(len(tableData[0])) to be a variable??

tablePrinter(myTable)
