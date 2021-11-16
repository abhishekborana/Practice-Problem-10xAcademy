size = int(input())
arr=[]
for i in range(size+1):
    arr.append(int(input()))
n = arr[-1]
sum=0
for i in range(n-1,size,n):
    sum+=arr[i] 
print(sum) 