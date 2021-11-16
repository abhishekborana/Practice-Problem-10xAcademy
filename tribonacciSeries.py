n =int(input())
a=0
b=0
c=1
if(n==1):
    res=a
elif(n==2):
    res=b
elif(n==3):
    res=c
else:
    for i in range(n-3):
        res=a+b+c
        a=b
        b=c
        c=res
print(res)
    