t=int(input())
for i in range(t):
	N=int(input())
	l=list(map(int, input().split()))
	if(len(l)==1):
		print("1")
		continue
	if(l[0]>l[1]):
		print("1")
		continue
	flag=0
	for i in range(1,N-1):
		if(l[i] >  l[i-1] and l[i] > l[i+1]):
			flag=1
			print(i+1)
			break
	if(flag==0):
		if(l[len(l)-1] > l[len(l)-2]):
			print(len(l))
		else:
			print("-1")