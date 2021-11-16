# your code goes here
def multiply(n):
	if(n==0):
		return 0
	if(n>0 and n<10):
		return int(n)
	else:
		rem=n%10
		n=n//10
		return rem*(multiply(n))
		
t=int(input())
for i in range(t):
    n=int(input())
    print(multiply(n))