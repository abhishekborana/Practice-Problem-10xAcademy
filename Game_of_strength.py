# your code goes here
testCases=int(input())
for i in range(testCases):
    size=int(input())
    arr=list(map(int,input().split()))
    arr.sort(reverse=True)
    m=1000000007
    diff=0
    size=size-1
    for i in arr:
        diff+=i*size
        size-=2
    res=((diff%m)*(arr[0]%m))%m
    print(res)
            