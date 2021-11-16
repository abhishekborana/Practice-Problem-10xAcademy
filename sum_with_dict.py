# Algorithm: O(n)
# 1. Create and maintain a hashtable nums
# 2. Take an item from the inputList and consider it to be num1
# 3. Check if the difference between the target sum and num1 is present as a key in the hashtable
# 4. If it is present, we can print the pair and exit our program
# 5. Otherwise, add the first number num1 to the hashtable nums, i.e num1: True
# 6. Repeat steps 2 - 5 for each and every element in the inputList


"""
Dry run
[3, 5, -4, 8, 11, -1, 6]
10

nums = {}

1st iteration
 - nums = {}, firstNum = 3, secondNum = 7
   nums = {3: True}

2nd iteration
 - nums = {3: True}, firstNum = 5, secondNum = 5
   nums = {3: True, 5: True}

3rd Iteration
- nums = {3: True, 5: True}, firstNum = -4, secondNum = 14
  nums = {3: True, 5: True, -4: True}

4th Iteration
- nums = {3: True, 5: True, -4: True}, firstNum = 8, secondNum = 2
  nums = {3: True, 5: True, -4: True, 8: True}

5th Iteration
- nums = {3: True, 5: True, -4: True, 8: True}, firstNum = 11, secondNum = -1
  nums = {3: True, 5: True, -4: True, 8: True, 11: True}

6th Iteration
- nums = {3: True, 5: True, -4: True, 8: True, 11: True}, firstNum = -1, secondNum = 11
  return [-1, 11]
  

"""

def twoNumberSum(inputList, targetSum):
    nums = {}
    for firstNum in inputList:
        secondNum = targetSum - firstNum
        if secondNum in nums:
            # This means that we have a second number such that first number + second == target sum
            return [firstNum, secondNum]
        else:
            nums[firstNum] = True
    return []

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