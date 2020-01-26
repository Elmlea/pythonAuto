# “List to Dictionary Function for Fantasy Game Inventory
# Imagine that a vanquished dragon’s loot is represented
# as a list of strings like this:
# dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
# Write a function named addToInventory(inventory, addedItems),
# where the inventory parameter is a dictionary representing
# the player’s inventory (like in the previous project) and the
# addedItems parameter is a list like dragonLoot.

# The addToInventory() function should return a dictionary
# that represents the updated inventory.
# Note that the addedItems list can contain multiples of the same item.

import pprint

def addToInventory(inventory, addedItems):
    for item in addedItems:
        inventory.setdefault(item, 0)
        inventory[item] += 1

def displayInventory(inventory):
    print("\nYou are carrying:\n")
    totalItems = 0

    for k, v in inventory.items(): # assigns keys to K and values to V
        print(str(v) + ' ' + str(k)) # each iteration prints the value, then the key
        totalItems += v
    print("\nTotal Items: " + str(totalItems))

playerInventory = {'arrow': 12, 'gold coin': 42, 'rope': 1,
                   'torch': 6, 'dagger': 1}

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby', 'fish']

print("\nBefore the encounter:")
displayInventory(playerInventory)

addToInventory(playerInventory, dragonLoot)

print("\nAfter the encounter:")
displayInventory(playerInventory)
