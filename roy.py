# your code goes here
def check(arr):
	start=0
	end=len(arr)-1
	while(start<end):
		i,j=0,0
		while(i!=len(arr)):
			if(arr[start][i]!=arr[end][j]):
				return -1
			i+=1
			j+=1
		start+=1
		end-=1
	return 1
def check2(arr):
	start=0
	end=len(arr[0])-1
	while(start!=len(arr)):
		i,j=0,len(arr[0])-1
		while(i<j):
			if(arr[start][i]!=arr[start][j]):
				return -1
			i+=1
			j-=1
		start+=1
	return 1
for _ in range(int(input())):
	size=int(input())
	arr=[]
	for i in range(size):
		n=list(input())
		arr.append(n)
	n1=check(arr)
	n2=check2(arr)
	if(n1==1 and n2==1):
		print("YES")
	else:
		print("NO")
		
	