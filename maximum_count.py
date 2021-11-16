size=int(input())
res=[]
cot=0   
cot2=[]
temp=1
f=0
for i in range(size):
    n=int(input())
    res.append(n)
for i in range(size-1):
    if(res[i]==res[i+1]):
        temp+=1
    else:
        cot=max(temp,cot)
        cot2.append(res[i-1])
        f=1
        temp=1
if(f==1):
    for i in cot2:
        print(i)
else:
    print("-1")