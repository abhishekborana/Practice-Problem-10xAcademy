for _ in range(int(input())):
    size=int(input())
    arr=list(map(int,input().split()))
    arr2=[x for x in arr]
    arr2.sort()
    #print(arr2,arr)
    res=0
    if(len(arr2)==2):
        res=(abs(arr[0]-arr[1]))
    elif(arr[0]==arr2[-1] and arr[-1]==arr2[0]):
        res=max(arr2[-2]-arr2[0],arr2[-1]-arr2[1])
    else:
        res=arr2[-1]-arr2[0]
    print(res)