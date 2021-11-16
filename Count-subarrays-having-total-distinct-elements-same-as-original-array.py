size=int(input())
arr=list(map(int,input().split()))
distinctEle=len(set(arr))
d={}
right=0
ans=0
window=0

for i in range(size):
    while(right < size and window < distinctEle):
        if(arr[right] in d.keys()):
            d[arr[right]]+=1
        else:
            d[arr[right]]=1
        if(d[arr[right]]==1):
            window +=1
        #print(d)
        right+=1

    if(window==distinctEle):
        ans+=(size-right+1)
    d[arr[i]]-=1
    if(d[arr[i]]==0):
        window-=1
    
    #print("after",d,"d[arr[i]]",d[arr[i]],"arr[i]",arr[i],"i",i,"ans",ans,"window",window)
print(ans)