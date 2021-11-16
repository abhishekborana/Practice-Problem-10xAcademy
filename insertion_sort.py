# Algorithm: (Ascending order)
# 1. It is the 1st element, then assume that it is sorted
# 2. Pick the next element
# 3. Compare the element with the sorted part of the list, i.e the elements on the left
# 4. Shift all the elements in the sorted part that are greater than the current element
# 5. Insert the value
# 6. Repeat steps 2 - 5 for each element in the list

# Input:      |
# 8, 4, 6, 3, 1, 9, 5

"""
Dry run
Input: [6, 3, 9, 8, 4, 5, 2]

1st for loop iteration:
    i = 1, j = 1, current element = 3
    While loop 1st iteration
    1 > 0 True
    3 < 6 True
    Go swap
    [3, 6, 9, 8, 4, 5, 2]
    j = 0

2nd for loop iteration:
    i = 2, j = 2, current element = 9
    while loop 1st iteration
    2 > 0 True
    9 < 3 False
    [3, 6, 9, 8, 4, 5, 2]

3rd for loop iteration:
    i = 3, j = 3, current element = 8
    while loop 1st iteration
    3 > 0 True
    8 < 9 True
    Go swap
    [3, 6, 8, 9, 4, 5, 2]
    j = 3-1 = 2
    While loop 2nd iteration
    2 > 0 True
    8 < 6 False

4th for loop iteration:
    i = 4, j = 4, current element = 4
    while loop 1st iteration
    4 > 0 True
    4 < 9 True
    Go swap
    [3, 6, 8, 4, 9, 5, 2]
    j = 4 - 1 = 3
    while loop 2nd iteration
    3 > 0 True
    4 < 8 True
    Go swap
    [3, 6, 4, 8, 9, 5, 2]
    j = 3 - 1 = 2
    while loop 3rd iteration
    2 > 0 True
    4 < 6 True
    Go swap
    [3, 4, 6, 8, 9, 5, 2]
    j = 2 - 1 = 1
    while loop 4th iteration
    1 > 0 True
    4 < 3 False

5th for loop iteration:
    i = 5, j = 5, current element = 5
    while loop 1st iteration:
    5 > 0 True
    5 < 9 True
    Go swap
    [3, 4, 6, 8, 5, 9, 2]
    j = 5 - 1 = 4
    while loop 2nd iteration:
    4 > 0 True
    5 < 8 True
    Go swap 
    [3, 4, 6, 5, 8, 9, 2]
    j = 4 - 1 = 3
    while loop 3rd iteration:
    3 > 0 True
    5 < 6 True
    Go swap
    [3, 4, 5, 6, 8, 9, 2]
    j = 3 - 1 = 2
    while loop 4th iteration:
    2 > 0 True
    5 < 4 False

6th for loop iteration:
    i = 6, j = 6, current element = 2
    while loop 1st iteration:
    6 > 0 True
    2 < 9 True
    Go swap
    [3, 4, 5, 6, 8, 2, 9]
    j = 6-1 = 5

    [2, 3, 4, 5, 6, 8, 9]


"""

# Time complexity of worst case: O(n^2)

def insertionSortAsc(array):
    for i in range(1, len(array)):
        # Go through each element in the list
        j = i
        while j > 0 and array[j] < array[j - 1]:
            # Start from the element on the left and continuw till you either reach
            # the first element or you found the correct place for the current element
            # swap elements
            # decrement j
            array[j], array[j - 1] = array[j - 1], array[j]
            j -= 1
    return array

def insertionSortDesc(array):
    for i in range(1, len(array)):
        # Go through each element in the list
        j = i
        while j > 0 and array[j] > array[j - 1]:
            # Start from the element on the left and continuw till you either reach
            # the first element or you found the correct place for the current element
            # swap elements
            # decrement j
            array[j], array[j - 1] = array[j - 1], array[j]
            j -= 1
    return array

if __name__ == "__main__":
    testcases = [
        [6, 3, 9, 8, -4, 5, 2],
        [8, -1, 6, 3, -8, -9, 5]
    ]

    for testcase in testcases:
        result = insertionSortDesc(testcase)
        print(f"Sorted array: {result}")