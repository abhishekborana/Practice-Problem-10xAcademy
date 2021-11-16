# your code goes here
def pemu(n,r):
	fact = 1
	i = 1
	while i<=n:
		fact = i*fact
		i = i+1
	numerator = fact          # n!
	sub = n - r               # (n-r)
	fact = 1
	i = 1
	while i<=sub:
		fact = i*fact
		i = i+1
	denominator = fact        # (n-r)!
	perm = numerator/denominator
	return (int(perm))
n=int(input())
arr=[]
m=pemu(n,n//3)
print((m*2)+1)
	