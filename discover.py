def find_k(arr, x):
	left=0
	right=len(arr)-1
	while left <= right:
		mid = left + (right - left) // 2
		if arr[mid] == x:
			return "YES"
		elif arr[mid] < x:
			left = mid + 1
		else:
			right = mid - 1
	return "NO"
    
from sys import stdin
N,Q = input().split()
a = list(map(int,input().split(' ')))
a.sort() 
for i in range(int(Q)):
    k = int(input())
    print(find_k(a, k))