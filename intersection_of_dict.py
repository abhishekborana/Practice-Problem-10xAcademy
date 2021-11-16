def intersect(nums1, nums2):
    # implement this function
    a1=0
    a2=0
    arr=[]
    while(a1<len(nums1) and a2<len(nums2)):
    	if(nums1[a1]<nums2[a2]):
    		a1+=1
    	elif(nums1[a1]>nums2[a2]):
    		a2+=1
    	else:
    		arr.append(nums2[a2])
    		a1,a2=a1+1,a2+1
    if(len(arr)==0):
    	return [-1]
    else:
    	return arr



# DO NOT change anything below this line
if __name__ == "__main__":
    num1_len = int(input())
    nums1 = []
    for index in range(num1_len):
        nums1.append(int(input()))
    num2_len = int(input())
    nums2 = []
    for index in range(num2_len):
        nums2.append(int(input()))

    for element in intersect(nums1, nums2):
        print(element)