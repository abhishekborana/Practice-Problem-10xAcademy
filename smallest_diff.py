# Algorithm:
# 1. Maintain a list of two integers and a variable. The list of integers will store the pair of numbers that have the smallest difference and the variable will store the actual value of the difference
# 2. Pick an element from the first array
# 3. For each element in the first array, pick a second element from the second array
# 4.  Find the absolute difference between the first number and the second number
# 5. Check if the current difference is less than the smallest difference we have yet encountered, in that case go ahead and store the pair of the first and second elements in the list and their difference in the variable
# 6. Repeat steps 2 - 5 until you reach the end of first array

# Time complexity of O(n^2)

def smallestDifference(arrayOne, arrayTwo):
    smallestDiff = abs(arrayOne[0] - arrayTwo[0])
    smallestDiffPair = [arrayOne[0], arrayTwo[0]]
    for el1 in arrayOne:
        for el2 in arrayTwo:
            currDiff = abs(el1 - el2)
            if currDiff < smallestDiff:
                smallestDiff = currDiff
                smallestDiffPair = [el1, el2]
    return smallestDiffPair


if __name__ == "__main__":
    testcases = [
        [[-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17]],
        [[-1, 5, 10, 20, 3], [26, 134, 135, 15, 17]],
        [[10, 0, 20, 25], [1005, 1006, 1014, 1032, 1031]]
    ]

    for testcase in testcases:
        arrayOne = testcase[0]
        arrayTwo = testcase[1]

        result = smallestDifference(arrayOne, arrayTwo)

        print(f"Smallest difference pair is: {result}")