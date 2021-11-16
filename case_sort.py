# your code goes here
size=int(input())
main=input()
lower=[]
upper=[]
res=""
for i in main:
	if(i.islower()):
		lower.append(i)
	else:
		upper.append(i)
lower.sort()
upper.sort()
l=0
u=0
i=0
while(i<len(main)):
	if(main[i].islower()):
		res+=lower[l]
		l+=1
	else:
		res+=upper[u]
		u+=1
	i+=1
print(res)