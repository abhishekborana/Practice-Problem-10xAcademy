testCase=int(input())
for i in range(testCase):
    size=int(input())
    arr=list(map(int,input().split()))
    s=0
    for i in arr:
        if i<0:
            continue
        else:
            s+=i
    print(s)