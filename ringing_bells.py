# your code goes here
def gcd(a,b):
	if(a==0):
		return b
	return gcd(b%a,a):
def lcm(a,b):
	return (a*b//(gcd(a,b)))

size=int(input())
arr=list(map(int,input().split()))
res=1
for i in arr:
	res=lcm(res,i)
print(res)