# your code goes here
size,k=map(int,input().split())
arr=list(map(int,input().split()))
d={}
prevSum=0
d[prevSum]=0
res=-1
for i in range(size):
	prevSum+=arr[i]
	
	currSum=prevSum-k
	if currSum in d:
		res=max(res,i-d[currSum])
	
	if prevSum not in d:
		d[prevSum]=i
		
print(res)