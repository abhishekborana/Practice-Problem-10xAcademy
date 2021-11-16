# your code goes here
n1,n2=map(int,input().split())
n1=n1+n2
if(n1<0 or n2<0):
	print(0)
if(n1<=12):
    print(n1)
else:
    if(n1%12==0):
        print(n1//12)
    else:
        print(n1%12)