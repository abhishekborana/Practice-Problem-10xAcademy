# your code goes here
size=int(input())
arr=list(map(int,input().split()))
arr.sort()
res=1
for i in range(1,size):
	if(arr[i]==arr[i-1]):
		continue
	res+=1
print(res)