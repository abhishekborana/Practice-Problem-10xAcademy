# your code goes here
households = int(input())
income=[]
totIncome=0
c=0
for i in range(households):
	income.append(int(input()))
for i in range(households):
	child=(int(input()))
	if(child>2):
		totIncome+=income[i]
		c+=1
if(totIncome>0):
	print(totIncome/c)
else:
	print(-1)
		
	