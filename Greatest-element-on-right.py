def replaceElements(arr):
    # Implement this function
    maxi=arr[-1]
    for i in range(len(arr)-2,-1,-1):
    	n=arr[i]
    	arr[i]=maxi
    	if(n>maxi):
    		maxi=n
    arr[-1]=-1
    return (arr)

# Do not edit anything below
if __name__=="__main__":
    num_elems = int(input())
    arr = []
    for index in range(num_elems):
        arr.append(int(input()))
    
    for elem in replaceElements(arr):
        print(elem)