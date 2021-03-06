# “Fantasy Game Inventory
# You are creating a fantasy video game.
# The data structure to model the player’s inventory will be a dictionary
# where the keys are string values describing the item in the inventory
# and the value is an integer value detailing how many of that item the
# player has. For example, the dictionary value
# {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
# means the player has 1 rope, 6 torches, 42 gold coins, and so on.”

# Write a function named displayInventory() that would take any possible
# “inventory” and display it like the following:
# Inventory:
# 12 arrow
# 42 gold coin
# 1 rope
# 6 torch
# 1 dagger

# Total number of items: 63

playerInventory = {'arrow': 12, 'gold coin': 42, 'rope': 1,
                   'torch': 6, 'dagger': 1}

def displayInventory(inventory):
    print("\nYou are carrying:\n")
    totalItems = 0

    for k, v in inventory.items(): # assigns keys to K and values to V
        print(str(v) + ' ' + k) # each iteration prints the value, then the key
        totalItems += v 
    print("\nTotal Items: " + str(totalItems))

displayInventory(playerInventory)
