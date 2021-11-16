size=int(input())
arr=[]
for i in range(size):
    arr.append(int(input()))
res=[]
con=0
for i in range(size):
    for j in range(size):
        if(arr[i]>arr[j]):
            con+=1
    res.append(con)
    con=0
for i in range(size):
    print(res[i])