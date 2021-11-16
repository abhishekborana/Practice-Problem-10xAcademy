# your code goes here
from collections import Counter

for _ in range(int(input())):
	s1,s2=input().split()
	con1=Counter(s1)
	con2=Counter(s2)
	if(con1==con2):
		print(True)
	else:
		print(False)