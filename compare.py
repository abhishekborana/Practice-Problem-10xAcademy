# your code goes here
size,query=map(int,input().split())
A=input()
B=input()
queryList=[]
for i in range(query):
	queryList.append(int(input()))


l=0
r=size-1
res=-1
def check(mid):
	bList=list(B)
	for i in range(mid+1):
		bList[queryList[i]-1]="1"
	b="".join(bList)
	return b>=A
while(l<=r):
	mid=l+(r-l)//2
	if(check(mid)):
		res=mid
		r=mid-1
	else:
		l=mid+1
		
finalRes=["NO"]*query
if(res!=-1):
	for i in range(res,query):
		finalRes[i]="YES"
for i in range(query):
	print(finalRes[i])