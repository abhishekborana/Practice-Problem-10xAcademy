def sumOfFirstN(n):
    # Implement this function
    if(n==1):
    	print(n,n)
    	return n
    else:
    	sum1 = n + sumOfFirstN(n-1)
    	print(n,sum1)
    	return sum1
# Do not edit anything below
if __name__ == "__main__":
    n = int(input())
    sumOfFirstN(n)