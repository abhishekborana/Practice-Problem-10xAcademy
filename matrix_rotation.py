def right90(arr,n):
    for i in range(n):
        for j in range(i):
            arr[i][j],arr[j][i]=arr[j][i],arr[i][j]
    for i in range(n):
        for j in range(n//2):
            arr[i][j],arr[i][n-j-1] =arr[i][n-j-1],arr[i][j]   
def left90(arr,n):
    for i in range(n):
        for j in range(i):
            arr[i][j],arr[j][i]=arr[j][i],arr[i][j]
    for i in range(n//2):
        for j in range(n):
            arr[i][j],arr[n-i-1][j] =arr[n-i-1][j],arr[i][j]


size=int(input())
arr=[]
for i in range(size):
    arr.append(list(map(int,input().split())))
r=input()
if(r=="RLR"):
    right90(arr,size)
    for i in arr:
        print(*i)
else:
    left90(arr,size)
    for i in arr:
        print(*i)

