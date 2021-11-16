# your code goes here
dials=int(input())
maxDial=int(input())
inputs=int(input())
arr={}
res=0
for i in range(dials):
	arr[(i+1)]=0
for i in range(inputs):
	m=int(input())
	arr[m]+=1
	if(arr[m]==maxDial):
		res=m
		break
print(res)