# your code goes here

for i in range(int(input())):
	arr=[]
	angerSum=0
	size=int(input())
	for i in range(size):
		fav,anger=map(int,input().split())
		angerSum+=anger
		arr.append((fav,anger))
	arr.sort(key=lambda  x:(x[0]+x[1]),reverse=True)
	print(arr)
	res=arr[0][0]+arr[0][1]+arr[1][0]+arr[1][1]-angerSum
	print(res)