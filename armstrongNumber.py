# your code goes here
number  = int(input())

n = number 
sum =0
while(number!=0):
	s = number%10
	sum = sum + (s**3)
	number = number//10
if(n==sum):
	print("Yes")
else:
	print("No")