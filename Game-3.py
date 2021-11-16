# your code goes here
def check(g,b):
	mini=min(g,b)
	res=mini
	if(g==mini):
		b=b-mini
		if(b%2==0):
			res+=b//2
		else:
			res+=b//2+1
	else:
		g=g-mini
		if(g%2==0):
			res+=g//2
		else:
			res+=g//2+1
	return res
for _ in range(int(input())):
	r,g,b=map(int,input().split())
	if(r==g and g==b):
		print(r)
		continue
	res=0
	mini=min(r,g,b)
	res+=mini
	if(mini==r):
		res+=check(g-mini,b-mini)
	elif(mini==g):
		res+=check(r-mini,b-mini)
	else:
		res+=check(r-mini,g-mini)
	print(res)
		