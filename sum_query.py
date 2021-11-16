# your code goes here
N,query=map(int,input().split())
arr=list(map(int,input().split()))
if(N<=0):
	print(0)
else:
	arr2=[]
	for i in range(N):
		if(i==0):
			arr2.append(arr[0])
			continue
		else:
			arr2.append(arr[i]+arr2[i-1])
	print(arr2)
	for i in range(query):
		sum1=0
		start,end=map(int,input().split())
		if(start==1):
			sum1=arr2[end-1]
		else:
			sum1=arr2[end-1]-arr2[start-1]
		print(sum1)
		
		