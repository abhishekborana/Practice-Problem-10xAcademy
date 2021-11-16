# your code goes here
size=int(input())
res=0

arr=list(map(int,input().split()))
arr.sort()
for i in range(0,len(arr),2):
	res+=arr[i]
print(res)
