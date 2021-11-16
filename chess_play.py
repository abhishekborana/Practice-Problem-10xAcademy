def chess(n,i,j,arr):
    if i<0 or i>9 or j<0 or j>9:
        return 0
    if n==0:
        if(arr[i][j]==0):
            arr[i][j] = 1
            return 1
        else:
            return 0
    return (chess(n-1,i+2,j+1,arr) + chess(n-1,i+2,j-1,arr) + chess(n-1,i+1,j+2,arr) + chess(n-1,i+1,j-2,arr) + chess(n-1,i-1,j+2,arr) + chess(n-1,i-1,j-2,arr) + chess(n-1,i-2,j+1,arr) + chess(n-1,i-2,j-1,arr))


row,col,N=map(int,input().split())
arr=[[0 for row in range(10)] for col in range(10)]
print(chess(N,row-1,col-1,arr))