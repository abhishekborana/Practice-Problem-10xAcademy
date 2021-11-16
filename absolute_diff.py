# your code goes here
size=int(input())
arr=list(map(int,input().split()))
arr.sort()
arr=arr[::-1]
dif=float('inf')
for i in range(size):
	if(i==size-1):
		n=arr[i]-arr[i-1]
		if(n<dif):
			if(n<0):
				continue
			else:
				dif=n
	else:
		n=arr[i]-arr[i+1]
		if(n<dif):
			if(n<0):
				continue
			else:
				dif=n
print(dif)
	
	
	