size=int(input())
namesDict={}
arr=[]
for i in range(size):
    n=input()
    arr.append(n)
for i in arr[0]:                        #abb
    con=0
    for j in range(1,len(arr)):         #aab
        if(i in arr[j]):
            con+=1
            arr[j]=arr[j].replace(i,"",1)
    if(con==len(arr)-1):
        if i not in namesDict:
            namesDict[i]=1
        else:
            namesDict[i]+=1
        

for i in sorted (namesDict.keys()) :
    print(i,namesDict[i])
