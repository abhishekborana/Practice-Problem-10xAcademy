# your code goes here
n,k=map(int,input().split())
arr=list(map(int,input().split()))
chargedMoney=int(input())
actualMoney=(sum(arr)-arr[k])//2
if(actualMoney==chargedMoney):
	print("It is Correct!")
else:
	print(chargedMoney-actualMoney)