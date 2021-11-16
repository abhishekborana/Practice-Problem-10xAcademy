# your code goes here
size=int(input())
price=list(map(int,input().split()))
quality=list(map(int,input().split()))
arr=[]
for i in range(size):
	arr.append([price[i],quality[i]])
maxPr=max(price)
mxQua=max(quality)

f=0
for i in range(size):
	if(arr[i][0]==maxPr and arr[i][1]==mxQua):
		f=1

if(f==1):
	print("Lucy")
else:
	print("Mark")
	