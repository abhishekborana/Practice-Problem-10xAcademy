# your code goes here
def target_Sum(arr,i,k):
	if(k==0 and i==len(arr)):
		return 1
	if(i>=len(arr)):
		return 0
	return (target_Sum(arr,i+1,k)+target_Sum(arr,i+1,k-arr[i])+target_Sum(arr,i+1,k+arr[i]))

target=int(input())
size=int(input())
arr=list(map(int,input().split()))
print(target_Sum(arr,0,target))