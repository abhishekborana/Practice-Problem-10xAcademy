size,testCase=map(int,input().split())
s=input()
for i in range(testCase):
    start,end=map(int,input().split())
    if(start>end or end>size):
        print("no")
    else:
        curr=s[start-1:end]
        one=curr.count("1")
        zero=curr.count("0")
        if(one==zero):
            print("yes")
        else:
            print("no")