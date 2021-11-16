testCase=int(input())
for i in range(testCase):
    size=int(input())
    arr=list(map(int,input().split()))
    avg=sum(arr)/size
    con=0
    for i in arr:
        if(i>avg):
            con+=1
    print(con)