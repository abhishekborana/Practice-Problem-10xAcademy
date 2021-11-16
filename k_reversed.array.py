# your code goes here
size=int(input())
arr=list(map(int,input().split()))
res=[]
for i in arr:
	res.append(i)
res.sort()
print(arr,res)
start=-1
end=0
for i in range(size):
	print("njh")
	if(res[i]!=arr[i]):
		print("hjh")
		if(start==-1):
			start=i
		end=i

print(start,end,end-start+1)