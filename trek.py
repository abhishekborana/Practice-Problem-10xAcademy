# your code goes here
t=int(input())

for i in range(t):
	val=0
	res=0
	size=int(input())
	s=input()
	s=list(s)
	U=s.count("U")
	D=s.count("D")
		
	print(U//D,U,D)
	