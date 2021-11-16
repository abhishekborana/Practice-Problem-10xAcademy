# your code goes here
str1=input()
str2=input()
if(len(str1)!=len(str2)):
	print("0")
else:
	for i in str1:
		if(i in str2):
			str2=str2.replace(i,"")
	if(len(str2)==0):
		print("1")
	else:
		print("0")