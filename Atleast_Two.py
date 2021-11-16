# your code goes here
size=int(input())
arr=list(map(int,input().split()))
arr=list(set(arr))
if(len(arr)<=2):
	print(-1)
else:
	arr.sort()
	for i in range(len(arr)-2):
		print(arr[i],end=" ")
		