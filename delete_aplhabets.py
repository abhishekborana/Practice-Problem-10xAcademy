# your code goes here
no_strings,size_of_str=map(int,input().split())
arr=[]
sortArr=[]
res1=[]
for i in range(no_strings):
	arr.append(input())
for i in range(size_of_str):
	res=""
	for j in range(no_strings):
		res+=arr[j][i]
	#print(res)
	res1.append(res)	
	res=list(res)
	res.sort()
	res="".join(res)
	sortArr.append(res)
con=0	
for i in range(len(sortArr)):
	if(sortArr[i]!=res1[i]):
		con+=1
print(con)
		