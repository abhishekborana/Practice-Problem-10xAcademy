def Where_to_place(l, x):
   # Implement This
   le=0
   r=len(l)-1
   res=0
   while(le<=r):
   		mid = le+(r-le)//2
   		if(l[mid]<=x):
   			res=mid
   			mid=le+1
   		elif(l[mid]<x):
   			r=mid-1
   		else:
   			le=mid+1
   return res
   #print(l)
n=int(input())
l=list(map(int,input().split()))[:n]
sum=0
l.sort()
for i in range(n):
    sum+=l[i]
    avg=sum//(i+1)
    l[i]=avg   
t=int(input())    
for k in range(t):
    x=int(input())
    print(Where_to_place(l,x))