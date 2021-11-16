def rowcheck(arr,n):
    k=0
    j=n-1
    for i in range(n//2):
        if(arr[k]!=arr[j]):
            return False
        k+=1
        j-=1
    return True
def colcheck(arr,n):
    for i in range(n):
        for j in range(n//2):
            if(arr[i][j]!=arr[i][n-j-1]):
                return False
    return True

for i in range(int(input())):
    size=int(input())
    arr=[]
    for i in range(size):
        m=input()
        g=[]
        for i in m:
            g.append(int(i))
        arr.append(g)
    #print(arr)
    if(colcheck(arr,size) and rowcheck(arr,size)):
        print("YES")
    else:
        print("NO")