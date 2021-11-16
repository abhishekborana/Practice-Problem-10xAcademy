# your code goes here
size=int(input())
arr=list(map(int,input().split()))
con=1
res=0
end=0
for i in range(1,size):
        if(arr[i]>arr[i-1]):
            con+=1
        else:
            if(con>res):
                res=con
                end=i
            con=1
    if(con>res):
        res=con
        end=size
start=end-res+1
print(res,start,end)
    
        
	