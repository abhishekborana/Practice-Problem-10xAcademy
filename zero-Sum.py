def zeroSum(matrix, rows, cols):
	
	res=0
	for i in range(rows):
		r=0
		for j in range(cols):
			r+=matrix[i][j]
		if(r==0):
			res+=1
	for i in range(cols):
		c=0
		for j in range(rows):
			c+=matrix[j][i]
		if(c==0):
			res+=1
	return (res)
			
	
	return res
	
			


for _ in range(int(input())):
    n,m = map(int, input().split())
    arr = [[int(x) for x in input().split()] for i in range(n)]
    print(zeroSum(arr, n, m))