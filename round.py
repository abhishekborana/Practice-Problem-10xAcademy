# your code goes here
# your code goes here
testCase=int(input())
for i in range(testCase):
	size=int(input())
	arr=list(map(int,input().split()))
	if(len(arr)<=1):
		print(-1)
	else:
		res=[]
		f=0
		for i in range(0,len(arr)-1):
			if(arr[i]==0):
				f=1
				break
			else:
				j = arr[i+1]/arr[i]
				j =round(j)
				res.append(j)
		if(f):
			print(-1)
		else:
			print(" ".join(map(str,res)))