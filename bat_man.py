# your code goes here
for _ in range(int(input())):
	size,k=map(int,input().split())
	arr=list(map(int,input().split()))
	res=[0]*size
	for i in range(size):
		res[(size-k+i)%size]=arr[i]
	print(*res)