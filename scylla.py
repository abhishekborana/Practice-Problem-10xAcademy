# your code goes here
size,k=map(int,input().split())
arr=list(map(int,input().split()))
res=float("inf")
arr.sort()
for i in range(0,size-k+1):
	res=min(res,(arr[i+k-1]-arr[i]))
print(res)