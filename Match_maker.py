# your code goes here
testCases=int(input())
for i in range(testCases):
    sizes=input()
    girlsH=list(map(int,input().split()))
    boysH=list(map(int,input().split()))
    girlsH.sort()
    boysH.sort(reverse=True)
    res=0
    for i in range(int(sizes)):
        if(girlsH[i]%boysH[i]==0 or boysH[i]%girlsH[i]==0):
            res+=1
    print(res)    