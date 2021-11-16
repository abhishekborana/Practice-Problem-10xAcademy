# your code goes here
def printA(l):
	for i in range(len(l)):
		print(l[i])
arr=list(map(int,input().split()))
l=len(arr)
M=int(input())
if(M<=0 or l<=0):
	printA(arr)
for i in range(M):
	for j in range(l-1):
		t=arr[j]
		arr[j]=arr[j+1]
		arr[j+1]=t
printA(arr)
		
	