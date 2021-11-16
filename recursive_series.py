# your code goes here
def series(n):
	if(n<=9):
		print(n)
		return n
	if(n%2!=0):
		print(n)
		return series(n-9)
	else:
		print(n)
		return series(n-10)
t= int(input())
for i in range(t):
	n=int(input())
	print(series(n))