# your code goes here
def killGame(n,k):
	if(n==1):
		return 1
	return (killGame(n-1,k)+k-1)%n+1
		


for _ in range(int(input())):
	size,kill=map(int,input().split())
	print(killGame(size,kill))