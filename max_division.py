# your code goes here
size=int(input())
arr=list(map(int,input().split()))
res=float("-inf")
for i in range(size):
	if(arr[i]==i):
		continue
	for j in range(size):
		if(j==i):
			continue
		x = abs(arr[i]-i)
		y=abs(arr[j]-j)
		res=max(res,x/y)
print(res)