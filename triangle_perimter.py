# your code goes here
t=int(input())
for _ in range(t):
	i=0
	res=0
	arr=list(map(int,input().split()))
	arr.sort(reverse=True)
	while(i<len(arr)-2):
		a=arr[i]
		b=arr[i+1]
		c=arr[i+2]
		if(a+b>c and b+c>a and c+b>a):
			res=max(a+b+c,res)
		i+=1
	print(res)
	