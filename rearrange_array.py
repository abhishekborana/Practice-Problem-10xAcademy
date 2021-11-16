	# your code goes here
size=int(input())
nums=[]
index=[]
res=[]
for i in range(size):
	nums.append(int(input()))
for i in range(size):
	index.append(int(input()))
for i in range(size):
	res.insert(index[i],nums[i])
for i in range(size):
	print(res[i])