# your code goes here
def insert(arr,k):
	if(len(arr)==1):
		return arr[0]
	if(k<arr[0]):
		return arr[0]
	if(k>=arr[-1]):
		return arr[-1]
	s=0
	e=len(arr)-1
	while(s<=e):
		mid=s+(e-s)//2
		prev=(mid-1+len(arr))%len(arr)
		if(arr[mid]==k):
			return arr[mid]
		if(k>arr[prev] and k<arr[mid]):
			ld=k-arr[prev]
			rd=arr[mid]-k
			if(ld==rd or rd<ld):
				return arr[mid]
			else:
				return arr[prev]
		if(arr[mid]>k):
			e=mid-1
		else:
			s=mid+1
size,q=map(int,input().split())
arr=list(map(int,input().split()))
query=list(map(int,input().split()))
for i in range(q):
	print(insert(arr,query[i]),end=" ")