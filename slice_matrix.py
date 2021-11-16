n,m=map(int,input().split())
arr=[]
for i in range(n):
    arr.append(list(map(int,input().split())))
left,right,top,bottom=map(int,input().split())
left,top=left-1,top-1
r=right-left+1
for i in range(top, bottom):
    if i<=n:
        for j in range(left-1, right):
            if j<=m:
                print(arr[i][j], end=" ")  