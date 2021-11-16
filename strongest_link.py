# your code goes here

size=int(input())
arr=list(map(int,input().split()))
maxi=float("-inf")
currMax=0
start=0
end=0
f=0
for i in range(size):
	currMax+=arr[i]
	if(maxi<currMax):
		maxi=currMax
		start=f
		end=i
		#end=size-arr
	if(currMax<=0):
		currMax=0
		f=i+1

print(start,end,maxi)