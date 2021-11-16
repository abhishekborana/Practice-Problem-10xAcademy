testCases=int(input())
for i in range(testCases):
    size=int(input())
    arr=list(map(int,input().split()))
    res=sorted(arr)
    first=set()
    second=set()
    for i in range(0,size,2):
        first.add(arr[i])
        second.add(res[i])
    print(len(first-second))