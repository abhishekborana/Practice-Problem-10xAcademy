def findLuckyNumber(nums):
    # implement this function
    res={}
    for i in nums:
    	if i in res:
    		res[i]+=1
    	else:
    		res[i]=1
    for i in nums:
    	if res[i]==i:
    		return i
    					
    return -1

# DO NOT change anything below this line
if __name__ == "__main__":
    num_elems = int(input())
    input_arr = []
    for index in range(num_elems):
        input_arr.append(int(input()))
    
    print(findLuckyNumber(input_arr))