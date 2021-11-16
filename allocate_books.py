# your code goes here
def conditions(arr,size,students,pagesTillNow):
	curr_students=1
	curr_pages=0
	for i in range(len(arr)):
		if(arr[i]>pagesTillNow):
			return False
		if((curr_pages +arr[i]) > pagesTillNow):
			curr_pages=arr[i]
			curr_students+=1
			if(curr_students>students):
				return False
		else:
			curr_pages+=arr[i]
	return True
def books(arr,size,students):
	if(students>size):
		return -1
	pages=0
	for i in arr:
		pages+=i
	start=0
	end=pages
	res=float("inf")
	while(start<=end):
		mid=start+(end-start)//2
		if(conditions(arr,size,students,mid)):
			res=mid
			end=mid-1
		else:
			start=mid+1
	return res

arr=list(map(int,input().split()))
students=int(input())
print(books(arr,len(arr),students))