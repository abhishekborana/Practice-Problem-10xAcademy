# your code goes here
size=int(input())
arr=list(map(int,input().split()))
x=0
y=0
for i in arr:
	x+=abs(i)
	y+=abs(i)**2
res=((x**2)-y)//2
print(res)