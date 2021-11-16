# your code goes here
def check_strings(s1,s2):
    res=""
    i=0
    j=0
    while(i<len(s1) and j<len(s2)):
        if(s1[i]==s2[j]):
            res+=s1[i]
            i+=1
            j+=1
        else:
            j+=1
    if(res==s1):
        return True
    else:
        return False
	
t=int(input())
for _ in range(t):
	s1,s2=input().split()
	print(check_strings(s1,s2))
	