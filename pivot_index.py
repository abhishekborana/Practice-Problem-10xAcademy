def pivotIndex(arr):
    # Implement this function
    mainSum=sum(arr)
    res=-1
    currSum=0
    if(len(arr)<=1):
    	return -1
    else:
    	mainSum-=arr[0]
    	for i in range(1,len(arr)-1):
    		currSum+=arr[i-1]
    		mainSum-=arr[i]
    		print(mainSum,currSum)
    		if(mainSum==currSum):
    			return i
    	return res


# Do not edit anything below
if __name__ == "__main__":
    num_elems = int(input())
    nums = []
    for i in range(num_elems):
        nums.append(int(input()))
        
    print(pivotIndex(nums))