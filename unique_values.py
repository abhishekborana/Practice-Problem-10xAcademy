# Algorithm:
# 1. Create 2 variables, max_key and max_val, and initialize them with 0 and None respectively
#    - max key stores the key that we have come across the dict which has the max number of unique
#    elements in its value list. Since intially we have not come across any keys, we have initialised it to None

#     - max_val stores the actual number of unique elements that are present for max_key

# 2. Take a key from inputDict: current key

# 3. Find the number of unique elements present in the value list for the current key

# 4. Compare with max_val and if current number is greater than max_val, update max_val with
#    the current number, and update max_key with the current key

# 5. Otherwise move on to the next key in the inputDict

# 6. Repeat steps 2 - 5 for eack key present in the inputDict

# Sample Input
# {
#     "Soap": [5, 7, 5, 4, 5], # 3
#     "Cheese": [6, 7, 4, 3, 3], # 4
#     "Curd": [9, 9, 6, 5, 5] # 3
# }

# Time complexity: O(n) time

def findKey(inputDict):
    max_key = None
    max_val = 0

    for currentKey in inputDict:
        currentValList = inputDict[currentKey] # [5, 7, 5, 4, 5]
        currentUniqueVal = len(set(currentValList))
        # set operator has been used to remove the duplicates from the value list
        # and find the number of unique elements
        if currentUniqueVal > max_val:
            # Update the max_key and max_val
            max_val = currentUniqueVal
            max_key = currentKey
    
    return max_key


testcases = [
        {
            "Soap": [5, 7, 5, 4, 5],
            "Cheese": [6, 7, 4, 3, 3],
            "Curd": [9, 9, 6, 5, 5]
        },
        {
            "TV": [2, 9, 5, 3, 3, -1],
            "Fridge": [10, 7, 3, 6, 0, 3],
            "Sofa": [12, 67, 12, 4],
            "Washing Machine": [9, 13, 6, 2, 13, 9]
        }
    ]

for inputDict in testcases:
    result = findKey(inputDict)
    print(f"\nThe key with max unique values is: {result}")


