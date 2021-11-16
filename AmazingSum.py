n =int(input())
prevNum=0
f=0
for i in range(n):
    n1 = int(input())
    if(n1+prevNum>100):
        f=1
    else:
        prevNum=n1

if(f):
    print("True")
else:
    print("False")
