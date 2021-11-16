# your code goes here
for i in range(int(input())):
	size=int(input())
	arr=list(map(int,input().split()))
	arr.sort()
	m=size//2
	a1=arr[:m]
	b1=arr[m::]
		#print(a,b)
	a=sum(a1)
	b=sum(b1)
	if(a==b):
		print(0)
	else:
		print((a-b))