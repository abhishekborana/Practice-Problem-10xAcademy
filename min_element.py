# your code goes here
res=0
size=int(input())
arr=[1, 3, 50, 10, 9, 7, 6]
num=float("-inf")
l=0
r=size-1
while(l<=r):
    mid=l+(r-l)//2

    if((r==l+1) and (arr[l]>=arr[r])):
        res=arr[l]
        break
    if((r==l+1) and (arr[l]<arr[r])):
        res=r
        break
    if(arr[mid]>arr[mid+1]):
        res=mid
        break
    if(arr[mid]>arr[mid+1]):
        r=mid-1
    else:
        l=mid+1
print(res)
    