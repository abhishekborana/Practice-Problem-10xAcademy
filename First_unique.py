# your code goes here
from collections import Counter
t=int(input())
for _ in range(t):
	s=input()
	sCoun=Counter(s)
	res=-1
	for i in sCoun:
		if(sCoun[i]==1):
			res=s.index(i)
			break
	print(res)