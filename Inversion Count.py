# your code goes here
def merge_sort(arr,left,right):
	con=0
	if(right>left):
		mid=(left+right)//2
		
		con+=merge_sort(arr,left,mid)
		
		con+=merge_sort(arr,mid+1,right)
		
		con+=merge(arr,left,mid,right)
	return con

def merge(arr,left,mid,right):
	
	temp=[0]*(right-left+1)
	con=0
	start=left
	end=mid+1
	i=0
	
	while(start<=mid and end<=right):
		if(arr[start]<=arr[end]):
			temp[i]=arr[start]
			con+=(mid-i+1)
			start+=1
		else:
			temp[i]=arr[end]
			end+=1
		i+=1
	while(start<=mid):
		temp[i]=arr[start]
		start+=1
		i+=1
	while(end<=right):
		temp[i]=arr[end]
		end+=1
		i+=1
	i=left
	for i in temp:
		arr[i]=i
		i+=1
	return con
	

size=int(input())
arr=list(map(int,input().split()))
print(merge_sort(arr,0,size-1))
	