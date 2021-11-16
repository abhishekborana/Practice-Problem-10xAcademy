# your code goes here
for _ in range(int(input())):
	size=int(input())
	valley=input()
	res=0
	tVal=0
	if valley[0]=="U":
		tVal+=1
	else:
		tVal-=1
	for i in range(1,size):
		if(valley[i]=="U"):
			tVal+=1
		else:
			tVal-=1
		if(tVal==0):
			if(valley[i]=="U"):
				res+=1
	print(res)
	