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

numItems = int(input())
itemsDict = {}

for index in range(numItems):
    currItem = input()
    if currItem in itemsDict:
        # Item is present. Increment count
        itemsDict[currItem] += 1
    else:
        # Item not present. Add item and initialize count to 1
        itemsDict[currItem] = 1

for bill_item, quantity in itemsDict.items():
    print(bill_item + " - " + str(quantity))