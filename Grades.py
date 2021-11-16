# your code goes here
size=int(input())
arr=[]
for i in range(size):
	n=int(input())
	if(n<=37):
		arr.append(n)
	else:
		rem=n%5
		if(rem<3):
			arr.append(n)
		else:
			rem=5-rem
			n=n+rem
			arr.append(n)
for i in arr:
	print(i)