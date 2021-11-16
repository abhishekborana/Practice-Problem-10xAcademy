# your code goes here
# your code goes here
days=int(input())
arr=[]
diff=[]
for i in range(days):
	arr.append(int(input()))
for i in range(1,days):
	diff.append(arr[i]-arr[i-1])
maxi=float("-inf")
currMaxi=0
for i in diff:
	currMaxi +=i
	maxi=max(maxi,currMaxi)
	if(currMaxi<0):
		currMaxi=0

if(maxi<0):
	print(0)
else:
	print(maxi)
	
		

		