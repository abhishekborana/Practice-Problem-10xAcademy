# your code goes here
def check_max(s1):
	if(len(s1) == 0):
		return 0
	else:
		charIndex=[-1]*256
		left=-1
		res=0
		for i in range(len(s1)):
			left=max(left,charIndex[ord(s1[i])])
			sub=i-left
			res=max(sub,res)
			print(charIndex[ord(s1[i])])
			charIndex[ord(s1[i])]=i

		return res
	
	
t=int(input())
for _ in range(t):
	print(check_max(input()))
	