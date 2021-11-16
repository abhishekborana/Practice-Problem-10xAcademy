size=int(input())
def pascalTriangle(size):
    arr=[0]*size
    curr=[1,1]
    if(size==1 or size==2):
        if(size==1):
            arr[0]=1
        else:
            arr =[1]*2
    else:
        for i in range(size+1):
            crr=[j for j in arr if i != 0]
            for j in range(i):
                if(j==0 or j==i-1):
                    arr[j]=1
                else:
                    arr[j]=crr[j-1]+crr[j]
    return arr

for i in range(size):
    print(" ".join(map(str, pascalTriangle(i))))
                