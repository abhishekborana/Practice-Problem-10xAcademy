# your code goes here 
for _ in range(int(input())):
	x1,v1,x2,v2=map(int,input().split())
	f=0
	for i in range(10**3):
		x1+=v1
		x2+=v2
		if(x1==x2):
			f=1
			break
	if(f==1):
		print("YES")
	else:
		print("NO")
	

