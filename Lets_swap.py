# your code goes here
size=int(input())
mini=[]
maxi=[]
arr=list(map(int,input().split()))
res=0
for i in range(len(arr)):
    res+=abs((i+1)-arr[i])
    mini.append(min(i+1,arr[i]))
    maxi.append(max(i+1,arr[i]))
res+=2*(abs(max(mini)-min(maxi)))
print(res)
	