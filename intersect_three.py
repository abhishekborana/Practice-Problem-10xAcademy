# your code goes here
arr1Len=int(input())
arr1=[]
for i in range(arr1Len):
	arr1.append(int(input()))
arr2Len=int(input())
arr2=[]
for i in range(arr2Len):
	arr2.append(int(input()))
arr3Len=int(input())
arr3=[]
for i in range(arr3Len):
	arr3.append(int(input()))
res=[]
for i in arr1:
	if((i in arr2) and (i in arr3)):
		res.append(i)
if(len(res)==0):
	print("-1")
else:
	res.sort()
	for i in res:
		print(i)