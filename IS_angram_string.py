# your code goes here
# your code goes here
str1=input()
str2=input()
if(len(str1)!=len(str2)):
	print("0")
else:
	str1Alpa=[0]*256
	str2Alpa=[0]*256
	f=1
	for i in str1:
		str1Alpa[ord(i)]+=1
	for i in str2:
		str2Alpa[ord(i)]+=1
	for i in range(256):
		if(str1Alpa[i]!=str2Alpa[i]):
			f=0
			break
	if(f):
		print("1")
	else:
		print("0")