# your code goes here
def check(arr,mid,ans):
	wood=0
	for i in arr:
		if(i>mid):
			wood+=(i-mid)
	print("wood",wood)
	if(wood>=ans):
		return True
	return False

arr=list(map(int,input().split()))
ans=int(input())
low=0
res=0
high=sum(arr)
while(low<=high):
	mid=(low+high)//2
	print(mid)
	if(check(arr,mid,ans)):
		res=mid
		low=mid+1
	else:
		high=mid-1
print(res)