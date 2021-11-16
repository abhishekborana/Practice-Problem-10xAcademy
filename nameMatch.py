size =int(input())
str1 =input()
arr = list(input().split())
res =0
if(size<=0):
    print('false')
else:
    for i in str1:
        if(i in arr):
            res+=1
    if(res==len(str1)):
        print('true')
    else:
        print('false')
    
