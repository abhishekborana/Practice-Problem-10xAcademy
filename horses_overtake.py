# your code goes here
size=int(input())
arr=[0]*size
for i in range(size):
	posi,speed=map(int,input().split())
	arr[posi]=speed
overtakes=[0]*11
res=0
for i in range(len(arr)):
	for j in range(arr[i]+1,11):
		res+=overtakes[j]
	overtakes[arr[i]]+=1
print(res)
	

	