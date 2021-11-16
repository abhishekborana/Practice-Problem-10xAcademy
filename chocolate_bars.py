# your code goes here
from collections import defaultdict
import math
def check_division(n):
    con=0
    sq=int(math.sqrt(n))+1
    for i in range(1,sq):
        if(n%i==0):
            con+=1
            if(n//i!=i):
            	con+=1
    return con

size=int(input())
arr=list(map(int,input().split()))
res=defaultdict(int)
for i in arr:
	f=check_division(i)
	res[f]+=1
pair=0
for i in res:
	pair+=(res[i]*(res[i]-1))//2
		
print(pair)