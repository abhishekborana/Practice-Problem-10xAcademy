# your code goes here
def Sum(arr,size,target,i):
	print(target,i)
	if target==0:
		return 1
	if(target<0 or i==size):
		return 0
	return Sum(arr,size,target-arr[i],i) + Sum(arr,size,target,i+1)
	


size,target=map(int,input().split())
arr=list(map(int,input().split()))

print(Sum(arr,size,target,0))