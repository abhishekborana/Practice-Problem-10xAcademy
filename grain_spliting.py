# your code goes here
for t in range(int(input())):
	arr=list(map(int,input().split()))
	res=sum(arr)//2
	r=[]
	arr.sort(reverse=True)
	curSum=0
	for i in range(len(arr)):
		curSum+=arr[i]
		print(curSum)
		if(curSum>res):
			curSum-=arr[i]
		else:
			r.append(arr[i])
			if(curSum==res):
				break
	r.sort()
	print(t+1)
	print(*r)
			
		