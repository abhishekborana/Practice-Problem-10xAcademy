# your code goes here
for _ in range(int(input())):
	n,m=map(int,input().split())
	arr=[]
	for _ in range(n):
		j=list(map(int,input().split()))
		for i in j:
			arr.append(i)
	arr.sort()
	mid=(n*m)//2
	print(arr[mid])