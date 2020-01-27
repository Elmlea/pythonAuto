def printPicnic(itemsDict, leftWidth, rightWidth):
    print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
    for k, v in itemsDict.items():
        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))

picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
printPicnic(picnicItems, 12, 5)
printPicnic(picnicItems, 20, 6)

"""This takes an input of a dictionary with all the items coming to the picnic.
The number parameters are the width of the left and right columns.
Line 2 adds the 2 lengths together, then centre-justifies the title.

We then iterate through the values in the dictionary, printing each key left
justified over the defined length, and repeating with the right column."""
