# your code goes here
def multiply(n):
    p=1
    for i in range(len(n)):
        p*=n[i]
testCase=int(input())
for i in range(testCase):
	size=int(input())
	l=list(map(int,input().split()))
	if(len(l)==1):
		print("1")
	else:
		le=[1]*len(l)
		ri=[1]*len(l)
		res=[]
		for i in range(1,len(l)):
			le[i]=le[i-1]*l[i-1]
			print(le[i],"=",le[i-1],"*",l[i-1])
		for i in range(len(l)-2,-1,-1):
			ri[i]=ri[i+1]*l[i+1]
			print(ri[i],"=",ri[i+1],"*",l[i+1])
		for i in range(len(l)):
			res.append(le[i]*ri[i])
		print(*le)
		print(*ri)
		print(*res)
		
			