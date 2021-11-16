# your code goes here


def check_palindrome(s1,n):
    start=0
    end=n-1
    charDel=0
    f=0
    while(start<end):
        if(s1[start]!=s1[end]):
            charDel+=1 
            if(charDel<=1):
                start+=1
            else:
                f=1
                break
        else:
            start+=1
            end-=1
    charDel=0
    g=0
    while(start<end):
        if(s1[start]!=s1[end]):
            charDel+=1
            if(charDel<=1):
                end-=1
            else:
                g=1
                break
        else:
            start+=1
            end-=1
    if(f==0 or g==0):
        return True
    else:
        return False
            
for _ in range(int(input())):
    s1=input()
    print(check_palindrome(s1,len(s1)))