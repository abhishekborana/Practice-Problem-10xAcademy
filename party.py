# your code goes here
for i in range(int(input())):
	size=int(input())
	d=[]
	res=0
	for i in range(size):
		h,m=map(int,input().split())
		d.append((h,m))
	d.sort()
	res=1
	m=1
	for i in range(1,len(d)):
		if(d[i]==d[i-1]):
			m+=1
		else:
			res=max(res,m)
			m=1
	print(max(res,m))