# your code goes here
def prime_number(maxi,res):
	p=2
	while(p*p<=maxi):
		if(res[p]==1):
			for i in range(p*p,maxi+1,p):
				res[i]=0
		p+=1

maxi,q=map(int,input().split())
res=[1]*(maxi+1)
res[0],res[1]=0,0
prime_number(maxi,res)

for i in range(1,maxi+1):
	print(res)
	res[i]+=res[i-1]

for i in range(q):
	q=int(input())
	print(res[q])
	
	