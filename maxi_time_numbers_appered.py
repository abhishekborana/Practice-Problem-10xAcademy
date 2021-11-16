size=int(input())
arr=[]
for i in range(size):
	arr.append(int(input()))
con =arr.count(arr[0])
for i in range(1,size-1):
	if((arr.count(i))>=con):
		con=arr.count(i)
res=[]
for i in range(size):
	if((arr.count(i))==con):
		res.append(arr[i])
for i in res:
	print(i)