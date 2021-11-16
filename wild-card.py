# your code goes here
def check(arr,currques,ques,res,i,s,t):
	if(ques==currques and i==t):
		arr.append(res)
		return
	if(s[i]=="?"):
		check(arr,currques+1,ques,res+"0",i+1,s,t)
		check(arr,currques+1,ques,res+"1",i+1,s,t)
	else:
		check(arr,currques,ques,res+s[i],i+1,s,t)

arr=[]
s=input()
ques=s.count("?")
check(arr,0,ques,"",0,s,len(s))
arr.sort()
for i in arr:
	print(i)