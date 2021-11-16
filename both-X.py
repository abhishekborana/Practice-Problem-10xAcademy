def bothCountX(string1, string2, x):
    # Complete this function, and return the list of resultant characters in sorted order
    d1,d2={},{}
    for i in string1.lower():
    	if(i not in d1):
    		d1[i]=1
    	else:
    		d1[i]+=1
    for i in string2.lower():
    	if(i not in d2):
    		d2[i]=1
    	else:
    		d2[i]+=1
    res=[]
    for i in d1:
    	if i in d2:
    		if(d1[i]==x and d2[i]==x):
    			res.append(i)
    res.sort()
    return res
    		

for _ in range(int(input())):
    string1, string2, x = input().split()
    x = int(x)
    print(*bothCountX(string1, string2, x))