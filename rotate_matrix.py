# your code goes here
size=int(input())
mat=[]
for i in range(size):
	c = list(map(int,input().split()))
	mat.append(c)
res=[]
for col in range(len(mat[0])):
	c=[]
	for row in range(len(mat)):
		c.append(mat[row][col])
	res.append(c[::-1])
print(len(res))
for i in range(len(res)):
	for j in range(len(res[0])):
		print(res[i][j],end=" ")
	print("")
		