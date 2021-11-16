# Python 3 program to find the number of
# ways to calculate a target number using
# only array elements and addition or
# subtraction operator.

# Function to find the number of ways to
# calculate a target number using only
# array elements and addition or
# subtraction operator.
def findTotalWays(arr, i, k):

	# If target is reached, return 1
	if (k == 0 and i == len(arr)):
		return 1

	# If all elements are processed and
	# target is not reached, return 0
	if (i >= len(arr)):
		return 0

	# Return total count of three cases
	# 1. Don't consider current element
	# 2. Consider current element and
	# subtract it from target
	# 3. Consider current element and
	# add it to target
	return (findTotalWays(arr, i + 1, k) +
			findTotalWays(arr, i + 1, k - arr[i]) +
			findTotalWays(arr, i + 1, k + arr[i]))

# Driver Code
if __name__ == '__main__':
	arr = [3, 2, -4, 4 ]

	# target number
	k = 5

	print(findTotalWays(arr, 0, k))
	
# This code is contributed by
# Surendra_Gangwar
