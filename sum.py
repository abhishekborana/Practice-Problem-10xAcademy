# Algorithm:
# 1. Take an item from the input list and let that be the first number num1
# 2. Go through the list of items and find a number in the array num2 that satisfies: num1 + num2 == target sum
# 3. If we find num2 that sums with num1 to result in target sum, then return the pair and exit
# 4. Otherwise move on to the next item in the input list
# 5. Repeat 1 - 4 for each item in the input list

# Input:
# non empty array = [3, 6, -4, 8, 11, -1, 6]
# 10 = target sum

# Time complexity: O(n^2)

# Dry run:

"""
1st iteration:
    firstNum = 3
    In the second loop - [7 , -4, 8, 11, -2, 6]

2nd Iteration:
    firstNum: 7
    In the second loop - [-4, 8, 11, -2, 6]

"""

def twoNumberSum(inputList, targetSum):
    for index in range(len(inputList)):
        firstNum = inputList[index]
        for j in range(index + 1, len(inputList)):
        # for j in range(len(inputList)):
        #     if index != j:
                secondNum = inputList[j]
                if firstNum + secondNum == targetSum:
                    return [firstNum, secondNum]
    
    return []


# if __name__ == "__main__":
testcases = [
    ([3, 5, -4, 8, 11, -1, 6], 10),
    ([4, 6], 10),
    ([4, 6, 1, -3], 3),
    ([1, 2, 3], 9)
]

for testcase in testcases:
    # ([3, 5, -4, 8, 11, -1, 6], 10)
    inputList = testcase[0]
    targetSum = testcase[1]
    result = twoNumberSum(inputList, targetSum)
    if result:
        print(f"Found pair: {result}")
    else:
        print("No such pair found")
