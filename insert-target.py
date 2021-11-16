# your code goes here
for i in range(int(input())):
	size,k=map(int,input().split())
	arr=list(map(int,input().split()))
	if(k>=arr[-1]):
		print(*arr,k)
	else:
		res=-1
		for i in range(size):
			if(k<arr[i]):
				res=i
				break
		print(*arr[:res],k,*arr[res:])
		