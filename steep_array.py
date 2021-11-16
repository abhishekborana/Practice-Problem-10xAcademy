# your code goes here
size=int(input())
arr=list(map(int,input().split()))
sum1=0
max1=0
for i in range(size-1,-1,-1):                                   #[9 4 7 2 1 4 5]
	max1=max(max1,arr[i])
	sum1+=(max1-arr[i])
print(sum1)
	