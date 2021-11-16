# your code goes here
for i in range(int(input())):
	strg =input().lower()
	res=""
	for i in strg:
		if(i.isalnum()):
			res+=i
	if(res==res[::-1]):
		print(True)
	else:
		print(False	)