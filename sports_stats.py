# your code goes here
from collections import defaultdict
size=int(input())
name={}
sports=defaultdict(int)

for i in range(size):
    name1,game=input().split()
    if name1 in name:
    	continue
    else:
    	name[name1]=game
    	sports[game]+=1
res=0
resSport=""
for i in sports:
    if sports[i]>res:
        res=sports[i]
        resSport=i
    elif sports[i]==res:
        if i< resSport:
            resSport=i
        
print(resSport)
print(sports['football'])