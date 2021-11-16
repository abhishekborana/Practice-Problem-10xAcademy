s = input()
res=0
temp=1
for i in range((len(s)-1)):
    if(s[i]==s[i+1]):
        temp+=1
    else:
        res=max(temp,res)
        temp=1
        continue
if(res>0):
    print(res)
else:
    print("-1")