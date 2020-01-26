allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
             'Bob': {'ham sandwiches': 3, 'apples': 2},
             'Carol': {'cups': 3, 'apple pies': 1}}

def totalBrought(guests, item):
    numBrought = 0
    for k, v in guests.items(): # this iterates over the key-value pairs in allGuests
    # the items in guests are assigned to k and v
    # guests names go in k
    # the dictionaries for items go in v
        numBrought = numBrought + v.get(item,0)
    # v is iterating through the items; this line runs the get function on v,
    # to see if the item specified is there.  
    return numBrought

print("Number of things being brought:")
print("- Apples         " + str(totalBrought(allGuests, 'apples')))
print("- Cups           " + str(totalBrought(allGuests, 'cups')))
print("- Cakes          " + str(totalBrought(allGuests, 'cakes')))
print("- Ham Sandwiches " + str(totalBrought(allGuests, 'ham sandwiches')))
print("- Apple Pies     " + str(totalBrought(allGuests, 'apple pies')))
