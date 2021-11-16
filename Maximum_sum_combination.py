# your code goes here
size=int(input())
arr=list(map(int,input().split()))
num1=""
num2=""
arr.sort(reverse=True)
for i in range(len(arr)):
	if(i%2==0):
		num1+=str(arr[i])
	else:
		num2+=str(arr[i])
res=int(num2)+int(num1)
print(res)
	