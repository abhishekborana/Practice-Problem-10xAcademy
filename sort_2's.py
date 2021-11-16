# your code goes here
size=int(input())
arr=list(map(int,input().split()))
arr.sort(reverse=True)
arr.sort(key=lambda x:(str(x).count('2')),reverse=True)
print(*arr)