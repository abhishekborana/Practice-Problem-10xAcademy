import math
def sumofproduct(n):
    # Code here
    for i in range(1,n+1):
    	sum1=0
    	n1=n
    	x=i
    	y=n1//i
    	sum1 = x*y+sum1
    return sum1

n = int(input())
print(sumofproduct(n))