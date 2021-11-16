# your code goes here
size=int(input())
arr=list(map(int,input().split()))
arrSet=list(set(arr))
res=[]
for i in arrSet:
	res.append(arr.count(i))
pair=0
for i in res:
	pair+=i//2
print(pair)