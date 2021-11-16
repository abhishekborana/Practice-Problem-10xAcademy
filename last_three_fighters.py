# your code goes here
n=int(input())
if(n==0):
	print(0)
elif(n==1):
	print(0)
elif(n==3):
	print(1)
elif(n==4):
	print(2)
else:
	a=1
	b=2
	c=4
	for i in range(4,n):
		d=a+b+c
		a=b
		b=c
		c=d
	print(b)