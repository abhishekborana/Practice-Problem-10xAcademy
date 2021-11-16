# your code goes here
size=int(input())
arr=[]
for i in range(size):
	arr.append(input())
l1=len(arr[0])
n=""
for i in arr:
	if(len(i)<l1):
		n=i
		break
n1=0
for i in n:
	n1+=int(i)
if(n1%2!=0):
	print("0")
else:
	print("1")
	