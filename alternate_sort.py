testCase=int(input())
for i in range(testCase):
    arr=list(map(int,input().split()))
    if(len(arr)<0):
        print(0)
    elif(len(arr)==1):
        print(arr[0])
    elif(len(arr)==2):
        print(arr[0],arr[1])
    else:
        e,o=[],[]
        for i in range(len(arr)):
            if(i%2==0):
                e.append(arr[i])
            else:
                o.append(arr[i])
        e.sort(reverse=True)
        o.sort()
        for i in range(len(e)):
            arr[2*i]=e[i]
        for i in range(len(o)):
            arr[2*i+1]=o[i]
        print(*arr)

                