gLen=int(input())
nList=list(input().split())
d={}
for i in nList:
    if(i not in d):
        d[i]=1
    elif(i in d):
        d[i]+=1
res=[]
for i in d:
    if(d[i]>gLen):
        res.append(i)
res.sort()
if(len(res)!=0):
    for i in res:
        print(i)
else:
    print("no such names in this town!!!")