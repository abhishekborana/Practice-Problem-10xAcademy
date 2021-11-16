num = int(input())
n=num
revNum="0"
if(num == 0):
    print("True")
else:
    revNum = ""
    while(num !=0):
        s = num%10
        revNum = revNum +str(s)
        num = num //10
    if(n==int(revNum)):
        print("True")
    else:
        print("False")