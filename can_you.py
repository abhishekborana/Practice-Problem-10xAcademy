def ncr(n):
	return (n*(n-1))//2
	

	
test =int(input())
for t in range(test):
	n = int(input())
	pos = {}
	neg = {}
	for i in range(n):
		x,y=map(int,input().split())
 
		val = y-x
		if val in neg.keys():
			neg[val] = neg[val]+1
		else:
			neg[val] = 1
        print(neg)
		
		nval = y+x
		if nval in pos.keys():
			pos[nval] = pos[nval]+1
		else:
			pos[nval] = 1
		print(pos)
	
	count=0
	for x in pos:
		count+=(ncr(pos[x]))
	for x in neg:
		count+=(ncr(neg[x]))
		
	print(count)