size = int(input())
arr =[]
res=0
for i in range(size+1):
    arr.append(input())
for i in range(size):
    if(arr[i]==arr[size]):
        res+=1
print(res)