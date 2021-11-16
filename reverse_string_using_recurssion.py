def reverse(l,s):
    if(l==len(s)-1):
        print(s[l],end='')
        return
    else:
        reverse(l+1,s)
        print(s[l],end='')


testCase=int(input())
for i in range(testCase):
    s=input()
    if(len(s)==0):
        print("")
    else:
        reverse(int(0),s)
    print("")
    