from sys import stdin,stdout
def Which_Day(a, x):
	print(a)
	l=0
	r=len(a)-1
	res=-1
	while(l<=r):
		mid=l+(r-l)//2
		if(a[mid]>=x):
			res=mid
			r=mid-1
		elif(a[mid]>x):
			r=mid-1
		else:
			l=mid+1
	return res
# Implement This
    
    
    
n,q = map(int,stdin.readline().split())
a = list(map(int,stdin.readline().split()))
for i in range(n):
    if i!=0:
        a[i] = a[i-1]+a[i]
k = list(map(int,stdin.readline().split()))
for i in range(q):
    ans = Which_Day(a,k[i])+1
    stdout.write(str(ans)+"\n")