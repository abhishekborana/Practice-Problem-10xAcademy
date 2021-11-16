# your code goes here
X=[]
Y=[]

size1=int(input())
for i in range(size1):
	X.append(list(map(int,input().split())))
size2=int(input())
for i in range(size2):
	Y.append(list(map(int,input().split())))
result=[[0]*len(Y[0])]*size1
result = [[sum(a*b for a,b in zip(X_row,Y_col)) for Y_col in zip(*Y)] for X_row in X]
print(len(result))
for i in result:
	print(*i)
			
		