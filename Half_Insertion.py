str=input()
arr=[]
chr=len(str)//2
for i in range(chr,len(str)):
    arr.append(str[i])
for i in range(1,len(arr)):
    j=i
    while(j>0 and ord(arr[j])<ord(arr[j-1])):
        arr[j],arr[j-1]=arr[j-1],arr[j]
        j=j-1
s="".join(arr)
str=str[0:chr]
print(str+s)