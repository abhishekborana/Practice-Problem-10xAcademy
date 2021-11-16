# your code goes here
size=int(input())
arr=[]
for i in range(size):
	arr.append(int(input()))
max1=arr[len(arr)-1]
for i in range(len(arr)-1,0,-1):
	if(max1<=arr[i]):
		max1=arr[i]
		print(max1)