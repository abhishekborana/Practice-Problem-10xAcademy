# Soap - 1 + 1 = 2
# Milk - 1
# Cheese - 1
# Curd - 1
# Mask - 1

# Algorithm:

# 1. Maintain a list of items and initially lets keep it empty
# 2. Take an item
# 3. If item is already present in the list, then increment its count
# 4. Otherwise, add it to the list of items and initialize count to 1
# 5. Repeat steps 2 - 4 until there are no items left in the cart

# Time 

# Input: Cheese
items = [] # ['Soap', 'Milk', 'Curd', 'Cheese'] 
counts = [] # [3, 1, 1, 1]

# items = [['Soap', 2], ['Milk', 1], ['Curd', 2]]


def findIndex(queryItem, allItems):
    # Take target item and list of all items
    # Returns the index of the found item, else -1
    numItems = len(allItems)
    for index in range(numItems):
        if allItems[index] == queryItem:
            return index
    return -1


numItems = int(input())
for index in range(numItems):
    currItem = input()
    itemIndex = findIndex(currItem, items)
    if itemIndex >= 0:
        # increment its count
        counts[itemIndex] += 1
    else:
        # add it to list of items
        # intialize count to 1
        items.append(currItem)
        counts.append(1)

for index in range(len(items)):
    print(items[index] + " - " + str(counts[index]))

