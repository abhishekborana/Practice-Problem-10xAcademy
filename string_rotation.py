def isSubstring(s1, s2):
    if s1.find(s2) != -1:
        return True
    if s2.find(s1) != -1:
        return True
    return False

## Do not change anything above
def isRotation(s1,s2):
    ## You can only call isSubstring function from this function once. Use this function to check if s2 is a rotation of s1.
    res=s1+s1
    if(s2 in res):
    	print(True)
    else:
    	print(False)
    
## Do not change anything below
t = int(input()) 
for i in range(t):
    s1 = input() 
    s2 = input()
    isRotation(s1,s2)