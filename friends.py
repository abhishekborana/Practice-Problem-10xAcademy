
for i in range(int(input())):
	size,k=map(int,input().split())
	arr=list(map(int,input().split()))
	i=0
	j=size
	temp=[]
	for i in arr:
		while(k and temp and temp[-1] < i):
			print(temp,i)
			temp.pop()
			k-=1
		temp.append(i)
			
	print(*temp)