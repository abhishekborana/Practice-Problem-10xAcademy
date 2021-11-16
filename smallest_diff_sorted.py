# Algorithm (Approach with sorting):
# 1. Sort both the input lists
# 2. Take two markers and position them at the beginning of the inputs lists
# 3. Maintain a list of two integers and a variable. The list of integers will store the pair of numbers that have the smallest difference and the variable will store the actual value of the difference
# 4. Pick the integer marked by the first marker as first number and pick the integer marked by the second marker as the second number
# 5. Check if the current difference is less than the smallest difference we have yet encountered, in that case go ahead and store the pair of the first and second elements in the list and their difference in the variable
# 6. if the first number is greater than the second number then move the pointer in 2nd list by 1 place
# 7. Otherwise if second number is greater than the first number then move the pointer in the 1st list by 1 place
# 8. Otherwise if first number is equal to second number then we have found a pair with 0 absolute difference.
#    There cannot be any pair that will have a difference lesser than 0. Thus we break the loop and return 
#    the [first number, second number]
# 9. Repeat steps 4 - 8 until any of the markers reach a position greater than the end of the lists

# a = [-1, 5, 10, 20, 28, 3]

      
# b = [26, 134, 135, 15, 17]

# smallest difference = 0
# smallest difference pair = [-1, 15]

#               |
# sorted(a) = [-1, 3, 5, 10, 20, 28] idxOne = 6

#              |
# sorted(b) = [15, 17, 26, 134, 135]

# Python uses a sorting algorithm called tim sort that has the time complexity: O(nlog(n))

# O(n) < O(nlog(n)) < O(n^2)

# Time complexity: O(nlog(n)) time
# Space complexity: O(1) space

def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    idxOne = 0
    idxTwo = 0
    smallestDiff = abs(arrayOne[idxOne] - arrayTwo[idxTwo])
    smallestDiffPair = [arrayOne[idxOne], arrayTwo[idxTwo]]
    while idxOne < len(arrayOne) and idxTwo < len(arrayTwo):
        firstNum = arrayOne[idxOne]
        secondNum = arrayTwo[idxTwo]
        currentDiff = abs(firstNum - secondNum)
        if currentDiff < smallestDiff:
            smallestDiff = currentDiff
            smallestDiffPair = [firstNum, secondNum]
        if firstNum > secondNum:
            idxTwo += 1
        elif secondNum > firstNum:
            idxOne += 1
        else:
            # Case where the absolute difference is 0
            # and first number == second number
            return [firstNum, secondNum]
    return smallestDiffPair


if __name__ == "__main__":
    testcases = [
        [
            [-1, 5, 10, 20, 28, 3],
            [26, 134, 135, 15, 17]
        ],
        [
            [-1, 5, 10, 20, 3],
            [26, 134, 135, 15, 17]
        ],
        [
            [10, 0, 20, 25],
            [1005, 1006, 1014, 1032, 1031]
        ]
    ]

    for testcase in testcases:
        arrayOne = testcase[0]
        arrayTwo = testcase[1]

        result = smallestDifference(arrayOne, arrayTwo)

        print(f"Smallest difference pair is: {result}")
