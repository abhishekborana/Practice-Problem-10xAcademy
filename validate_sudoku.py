# your code goes here
from collections import defaultdict
def checksudoku(arr):
	rows=defaultdict(set)
	col=defaultdict(set)
	three=defaultdict(set)
	for r in range(9):
		for c in range(9):
			if(arr[r][c]=="."):
				continue
			if((arr[r][c] in rows[r]) or (arr[r][c] in col[c]) or (arr[r][c] in three[(r//3,c//3)])):
				return False
			rows[c].add(arr[r][c])
			rows[r].add(arr[r][c])
			three[(r//3,c//3)].add(arr[r][c])
	return True

arr=[]
for i in range(9):
	a=list(input().split())
	arr.append(a)
print(checksudoku(arr))

		