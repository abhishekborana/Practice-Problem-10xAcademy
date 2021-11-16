n,k = map(int,input().split())
arr =input().split()

temp =arr[k-1]
arr[k-1] =arr[n-k]
arr[n-k] =temp
print(" ".join(arr))

    