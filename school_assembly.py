# your code goes here
size=int(input())
arr=list(map(int,input().split()))
d={}
d2={}
for i in range(len(arr)):
	d[i]=True
	d2[arr[i]]=True
res=float("inf")
for i in d:
	if i in d2:
		if(res>i):
			res=i
print(res)
	