# your code goes here
size=int(input())
arr=[]
for i in range(size):
	n=int(input())
	if(n<0):
		n=n*-1
	n=n*n
	arr.append(n)
print(arr)
arr.sort()
for i in range(len(arr)):
	print(arr[i])