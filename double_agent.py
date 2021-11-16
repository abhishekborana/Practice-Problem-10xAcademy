# your code goes here
from collections import Counter
size=int(input())
arr=list(input().split())
arr = [''.join(sorted(ele)) for ele in arr]
print(arr)
arr=Counter(arr)
print(arr)
print(max(arr.values()))