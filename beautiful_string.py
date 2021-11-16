# your code goes here
from collections import defaultdict

testCase=int(input())
for i in range(testCase):
    currStr=input()
    a,b,c=0,0,0
    d=defaultdict(int)
    d[(0,0)]=1
    res=0
    for i in currStr:
        if(i=='a'):
            a+=1
        elif(i=='b'):
            b+=1
        elif(i=='c'):
            c+=1
        m=(a-b,b-c)
        res+=d[m]
        d[m]+=1
    print(res)