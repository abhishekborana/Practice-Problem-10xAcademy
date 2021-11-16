# your code goes here
size=int(input())
g,b=[],[]
for i in range(size):
	sex,talent=map(int,input().split())
	if(sex==0):
		g.append(talent)
	else:
		b.append(talent)
g.sort(reverse=True)
b.sort(reverse=True)
g=g+b
print(" ".join(map(str,g)))