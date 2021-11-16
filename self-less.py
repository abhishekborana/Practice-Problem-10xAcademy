# your code goes here
for i in range(int(input())):
	n=int(input())
	arr=list(map(int,input().split()))
	res=[1]*n
	temp=1
	for i in range(n):
		 res[i]=temp
		 temp=temp*arr[i]
	temp=1
	for i in range(n-1,-1,-1):
    	 res[i]*=temp
    	 temp*=arr[i]
	for i in res:
         print(i,end=" ")
    	