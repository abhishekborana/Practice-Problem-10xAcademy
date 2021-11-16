def decreasingArrCheack(arr):
    con=0
    for i in range(len(arr)-1):
        if(arr[i]>=arr[i+1]):
            con+=1
    if(con==len(arr)-1):
        return True
    else:
        return False
def increasingArrCheack(arr):
    con=0
    for i in range(len(arr)-1):
        if(arr[i]<=arr[i+1]):
            con+=1
    if(con==len(arr)-1):
        return True
    else:
        return False

size=int(input())
arr=[]
for i in range(size):
    arr.append(int(input()))
if(len(arr) <= 1):
    print("false")
else:
    if(arr[0]>=arr[1]):
        print(decreasingArrCheack(arr))
    else:
        print(increasingArrCheack(arr))
        
        
    