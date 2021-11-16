# your code goes here
def seating(res,s,b,a,n,l):
	if(l==n and b<3 and a<3):
		res.append(s)
		return
	if(a>2 or b>2 or l>n):
		return 
	seating(res,s+"a",0,a+1,n,l+1)
	seating(res,s+"b",b+1,0,n,l+1)
	return 
size=int(input())
res=[]
seating(res,"",0,0,size,0)
res.sort()
for i in res:
	print(i)