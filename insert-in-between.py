size,nums=map(int,input().split())
arr=list(map(int,input().split()))
res=[]
if (nums<=arr[0]):
    res=[nums]+arr
elif (nums>=arr[-1]):
    res=arr+[nums]
else:
    for i in range(nums):
        if(nums<=arr[i]):
            res= arr[:i]+[nums]+arr[i:]
print(*res)