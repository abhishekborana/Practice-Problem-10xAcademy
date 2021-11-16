def cutRope(A):
    # Complete this function
    res=[]
    A.sort()
    con=0
    for i in range(len(A)):
    	if(A[i]==0):
    		continue
    	a=A[i]
    	for j in range(i,len(A)):
    		A[j]=A[j]-a
    		#print(A[j])
    		if(A[j]>0):
    			con+=1
    	if(con!=0):
    		res.append(con)
    	con=0
    return res
    
    	

# Do not change anything below this line
if __name__ == '__main__':
    input_numbers = []
    for _ in range(int(input())):
        input_numbers.append(int(input()))

    for i in cutRope(input_numbers):
        print(i)