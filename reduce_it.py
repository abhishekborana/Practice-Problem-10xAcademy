# your code goes here
n =int(input())
f=1
while(f):
	if(n<0):
		f=0
	elif(n%2==0):
		n-=11
	else:
		n-=21
print(n)