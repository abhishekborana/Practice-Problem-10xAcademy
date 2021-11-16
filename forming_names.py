# your code goes here
size=int(input())
string=input()
listChar=list(input().split())
f=1
for i in range(len(string)):
	if(string[i] not in listChar):
		f=0
		break
if(f):
	print("true")
else:
	print("false")
		