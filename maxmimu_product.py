# your code goes here
size =int(input())
res=[]
arr=[]
for i in range(size):
    n1=int(input())
    if(n1<0):
        n1=-1*n1
    arr.append(n1)
arr=list(sorted(arr))
print(arr)
if(size==3):
    res*=arr[2]
else:
    for i in range(size-2):
        res.append(arr[i]*arr[i+1]*arr[i+2])
print(max(res))