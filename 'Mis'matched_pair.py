# your code goes here
size=int(input())
arr=list(map(int,input().split()))
num1=0
num2=0
res=0
arr.sort()
for i in range(size-1):
	diff=0
	if(arr[i]!=arr[i+1]):
		diff=abs(arr[i]-arr[i+1])
	if(res>diff):
		res=diff
		num1=arr[i]
		num2=arr[i+1]
print(num2,num1,diff)
	