num = int(input())

res =""
n=num 
if(num>0):
    while(num!=0):
        if(num==n):
            if(num%10==0):
                num =num//10
        s = num%10
        res +=str(s)
        num = num//10
if(num<0):
    num = num + (-2*num)
    n=num
    res = "-"
    while(num!=0):
        if(num==n):
            if(num%10==0):
                num = num//10
        s=num%10
        res = res+str(s)
        num = num//10
print(res)