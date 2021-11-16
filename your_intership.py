# your code goes here
for i in range(int(input())):
	rangee,step=map(int,input().split())
	if(step>rangee):
		print(1)
		continue
	arr=[]
	for i in range(rangee):
		arr.append(i+1)
	while(1):
		print(*arr)
		arr=arr[step-1::step]
		print(*arr)
		if(len(arr)<step):
			break
	print(arr[0])