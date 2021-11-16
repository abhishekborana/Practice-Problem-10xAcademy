# your code goes here
size = int(input())
mat=[]
sum1=0
for i in range(size):
	mat.append(list(map(int,input().split())))
for row in range(size):
    col=row
    sum1+=mat[row][col]
for row in range(size):
    col=size-row-1
    sum1+=mat[row][col]
print(sum1)