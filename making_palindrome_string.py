strPa = input()
numbers =int(input())
s=""
if(len(strPa)==1):
    s=strPa
elif(numbers ==0):
    s=strPa+strPa[::-1]
elif(numbers ==1):
    str2=strPa[::-1]
    str2=str2[1:]
    s=strPa+str2
else:
    s=strPa+strPa[::-1]
    
print(s)