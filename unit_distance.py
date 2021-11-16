def isEditDistanceOne(string1, string2): 
    # Complete this function, and return True/False
    s1=string1
    s2=string2
    diff = len(s1)-len(s2)
    if abs(diff)>1:
        return False
    i,j=0,0
    count=0
    while  i < len(s1) and j < len(s2):
        if s1[i]!=s2[j]:
            #print(count)
            count+=1
            if count>1:
                return False
            elif diff>0:
                i+=1
            elif diff<0:
                j+=1
            else:
                i+=1
                j+=1
        else:
            i+=1
            j+=1
    if i<len(s1) or j<len(s2):
        count+=1
    #print(count)
    if count==1:
        return True
    return False
    			
    		

for _ in range(int(input())):
    input_string1, input_string2 = input().split()
    print(isEditDistanceOne(input_string1, input_string2))