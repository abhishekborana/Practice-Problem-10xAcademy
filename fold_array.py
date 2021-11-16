# your code goes here
size=int(input())
arr=[]
res=[]
for i in range(size):
    arr.append(int(input()))
fold=int(input())
res=[]
for i in range(fold):
	if(len(arr)%2!=0):
		for j in range(len(arr)//2+1):
			if(j==(len(arr)-1-j)):
				res.append(arr[j])
			else:
				res.append(arr[j]+arr[len(arr)-1-j])
	elif(len(arr)%2==0):
		for j in range(len(arr)//2):
			if(j==(len(arr)-1-j)):
				res.append(arr[j])
			else:
				res.append(arr[j]+arr[len(arr)-1-j])
	arr=res
	res=[]
print(len(arr))
for i in range(len(arr)):
	print(arr[i])
			
			
		
