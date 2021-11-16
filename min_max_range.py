## This function should return single integer. The integer should be maximum value of input list
## Please fill the following function
def maximum_value(input_numbers):
    # write below this here
    maxVal=input_numbers[0]
    for i in input_numbers:
    	if(i>maxVal):
    		maxVal=i
    return maxVal


## This function should return single integer. 
## The integer should be minimum value of input list
def minimum_value(input_numbers):
    # Please write below this
    minVal=input_numbers[0]
    for i in input_numbers:
    	if(i<minVal):
    		minVal=i
    return minVal


## This function should return list of integer which lies between m1 and m2. 
## if m1 <= m2 return list off numbers between m1 and m2
## if m2 <= m1 return list off numbers between m2 and m1
def get_numbers_in_range(input_numbers, m1, m2):
    # Please write below this line
    res=[]
    rangeRes=m1-m2
    if(rangeRes<0):
    	for i in input_numbers:
    		if(i>=m1 and i<=m2):
    			res.append(i)
    	if(len(res)==0):
    		res.append(-1)
    	return res
    if(rangeRes>=0):
    	for i in input_numbers:
    		if(i<=m1 and i>=m2):
    			res.append(i)
    	if(len(res)==0):
    		res.append(-1)
    	return res
    res.append(-1)
    return res
    	





### Please do not change anything below this line.
if __name__ == "__main__":
    list1 = [int(i) for i in input().split(' ')]
    list2 = [int(i) for i in input().split(' ')]
    list3 = [int(i) for i in input().split(' ')]
    m1 = minimum_value(list1)
    m2 = maximum_value(list2)
    min_max_range = get_numbers_in_range(list3, m1, m2)
    [print(i) for i in min_max_range]