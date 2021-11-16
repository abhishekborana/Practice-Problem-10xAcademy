# your code goes here
aSize=int(input())
bSize=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
maxA=0
maxB=0
for i in a:
	if(i<0):
		i=i*-1
	if(i>=maxA):
		maxA=i
for i in b:
	if(i<0):
		i=i*-1
	if(i>=maxB):
		maxB=i
print(maxA*maxB)
		