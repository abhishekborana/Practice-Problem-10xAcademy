# your code goes here
size=int(input())
arr=list(map(int,input().split()))
l=0
r=size-1
res=-1
while(l<=r):
	mid=l+(r-l)//2
	prev=(mid-1+size)%size
	next1=(mid+1)%size
	if((arr[mid]<arr[prev]) and (arr[mid]<=arr[next1])):
		res=arr[mid]
		break
	elif(arr[mid]<arr[l]):
		r=mid
	elif(arr[mid]>arr[r]):
		l=mid
	else:
		res=arr[0]
		break
print(res)