# your code goes here
size=int(input())
arr=list(map(int,input().split()))
check=[]
for i in arr:
	if(i%2==0):
		check.append(1)
	else:
		check.append(-1)
d={0:1}
temp=0
for i in check:
	temp+=i
	if(temp in d):
		d[temp]+=1
	else:
		d[temp]=1
print(arr,check,d)
con=0
for i in d.values():
	con+=i*(i-1)//2
print(con)
	