# your code goes here
res=0
size=int(input())
arr=list(map(int,input().split()))
arr1=[]
arr2=[]
for i in range(size):
	arr1.append(arr[i]*(i-1))
	arr2.append(arr[i]*(i+1))
res=max(arr1)-min(arr2)
print(res)