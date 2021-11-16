# your code goes here
size =int(input())

if(size<2):
	print("-1")
else:
    arr=[]
    for i in range(size):
        arr.append(int(input()))
    res=-1
    for i in range(size):
        con=0
        for j in range(size):
            if(arr[i]<arr[j]):
                con+=1
        if(arr[i]==con):
            res=1
            break
    print(res)
    