# your code goes here
size=int(input())
arr=list(map(int,input().split()))
f1,f2,f3,f4,f5=0,0,0,0,0
for i in arr:
	if(i==1):
		f1+=1
	elif(i==2):
		f2+=1
	elif(i==3):
		f3+=1
	elif(i==4):
		f4+=1
	elif(i==5):
		f5+=1
print("1 "*f1+"2 "*f2+"3 "*f3+"4 "*f4+"5 "*f5)