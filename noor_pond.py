# your code goes here
for _ in range(int(input())):
	s=int(input())
	eat=[]
	size=[]
	for i in range(s):
		se,e=map(int,input().split())
		eat.append(e)
		size.append(se)
	eat.sort()
	size.sort()
	i=0
	j=0
	con=1
	while(i<s):
		if(eat[i]>=size[j]):
			con=max(con,i-j)
			j+=1
		else:
			i+=1
	print(con)
		