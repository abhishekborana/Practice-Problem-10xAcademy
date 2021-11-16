# your code goes here
def rotate(arr,times):
	res=[0]*len(arr)
	for i in range(len(arr)):
		res[(i+times)%len(arr)]=arr[i]
	return res
N,Q=map(int,input().split())
arr=list(map(int,input().split()))
res=0	
for i in range(Q):
	a,times=input().split()
	if(a=="L"):
		res-=int(times)
	else:
		res+=int(times)
print(*rotate(arr,res))