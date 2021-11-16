def conSubtring(s):
    con=0
    for i in range(len(s)):
        j=i
        k=i
        while(j>=0 and k<len(s) and s[j]==s[k]):
            j-=1
            k+=1
            con+=1
        j=i
        k=i+1
        while(j>=0 and k<len(s) and s[j]==s[k]):
            j-=1
            k+=1
            con+=1
    return (con)


for i in range(int(input())):
    s=input()
    if(len(s)==0 or len(s)==1):
        print(len(s))
    else:
        print(conSubtring(s))