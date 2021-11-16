n=int(input())
for i in range(n):
	size=int(input())
	s=input()
	d={}
	sum1=0
	for j in range(len(s)):
    	 if s[j] in d:
        	d[s[j]]+=1
    	 else:
        	d[s[j]]=0
    	 sum1+=d[s[j]]
	print(sum1)