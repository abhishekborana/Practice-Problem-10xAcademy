# your code goes here
arr=[]
for i in range(int(input())):
    name,rollNo,marks=input().split()
    arr.append([name,int(rollNo),int(marks)])
arr.sort(key=lambda x: x[1])
#print(arr)

arr.sort(key=lambda x: x[0])
#print(arr)
arr.sort(key=lambda x: x[2],reverse=True)
for i in arr:
	print(*i)