def calSumUtil( A , B , n , m ):
	a,b,i,j=0,0,0,0
	while(i<n or j<m):
		if(i<n):
			a=a*10+A[i]
			i+=1
		if(j<m):
			b=b*10+B[j]
			j+=1
	a=a+b
	res = [int(x) for x in str(a)]
	return res
   # Implement this 
   # A is the first array
   # n is size of array A
   # B is the second array
   # m is size of array B
   
  
# Wrapper Function 
def calSum(a, b, n, m ): 
  
    # Making first array which have 
    # greater number of element
    # A is the first array
    # n is size of array A
    # B is the second array
    # m is size of array B 
    if n >= m: 
        return calSumUtil(a, b, n, m) 
    else: 
        return calSumUtil(b, a, m, n) 
  
# Driven Code 
testCase = int(input())
for _ in range(testCase):
	A = list(map(int,input().split()))
	B = list(map(int,input().split()))
	res = calSum(A, B, len(A), len(B))
	print(*res)