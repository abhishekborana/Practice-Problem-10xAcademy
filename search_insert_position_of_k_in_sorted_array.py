# your code goes here
def insert(arr,k):
	s=0
	e=len(arr)-1
	res=-1
	while(s<=e):
		mid=s+(e-s)//2
		if(arr[mid]>=k):
			res=mid
			e=mid-1
		elif(arr[mid]>k):
			e=mid-1
		else:
			s=mid+1
	if res==-1:
		return len(arr)
	else:
		return res


for _ in range(int(input())):
	arr=list(map(int,input().split()))
	totELEInserted=int(input())
	ele=list(map(int,input().split()))
	for i in range(totELEInserted):
		res=insert(arr,ele[i])
		print(res)
	