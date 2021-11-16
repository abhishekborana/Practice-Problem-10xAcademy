# your code goes here
size=int(input())
arr=list(map(int,input().split()))
mini,maxi=arr[0],arr[0]
minRes=0
maxRes=0
for i in arr:
	if(i<mini):			# 10   5   4   2  1
		mini=i			# 1+1+1+1
		minRes+=1
	elif(i>maxi):		# 10  20   25
		maxi=i			# 1+1
		maxRes+=1
print(maxRes,minRes)