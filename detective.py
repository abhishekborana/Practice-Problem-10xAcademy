# your code goes here
from collections import Counter
for _ in range(int(input())):
	n1=input().lower().split()
	n2=input().lower().split()
	n1="".join(n1)
	n2="".join(n2)
	char1=""
	char2=""
	symbols1=""
	symbols2=""
	for i in n1:
		if(ord(i)>=97 and ord(i)<=122):
			char1+=i
		else:
			symbols1+=i
	for i in n2:
		if(ord(i)>=97 and ord(i)<=122):
			char2+=i
		else:
			symbols2+=i
	char1=sorted(char1)
	char2=sorted(char2)
	symbols1=sorted(symbols1)
	symbols2=sorted(symbols2)
	#print(char1,char2,symbols1,symbols2)
	char1="".join(char1)
	char2="".join(char2)
	symbols1="".join(symbols1)
	symbols2="".join(symbols2)
	if(char2 in char1 and symbols2 in symbols1):
		print("YES")
	else:
		print("NO")
	#print(n1,n2)
