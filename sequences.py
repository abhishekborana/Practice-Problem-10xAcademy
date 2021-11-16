# your code goes here
from collections import Counter
size=int(input())
arr=list(map(int,input().split()))
arr.sort()
flag=1
count=Counter(arr)
for i in range(2,arr[-1]+1):
    if count[i]>count[i-1]:
        flag=2
        break
if flag==1:
    res=[]
    for i in range(arr[-1],0,-1):
        temp=[]
        val=count[i]
        if val>0:
            for j in range(1,i+1):
                temp.append(j)
                count[j]-=val
            for k in range(val):
                res.append(temp)
    print(len(res))
    [print(*i) for i in reversed(res)]
else:
    res=0
    th=0
    for i in range(arr[-1],0,-1):
        if count[i]>=th:
            th=count[i]
        else:
            d=(th-count[i])
            res+=d
            count[i]+=d
    print(res)
        
        
	
			
			
		
	