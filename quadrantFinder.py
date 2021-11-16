# your code goes here
testCase = int(input())
for i in range (0,testCase):
	x,y = input().split() 
	if(int(x)>0 and int(y)>0):
		print("Q1")
	elif(int(x)<0 and int(y)>0):
		print("Q2")
	elif(int(x)<0 and int(y)<0):
		print("Q3")
	elif(int(x)>0 and int(y)<0):
		print("Q4")