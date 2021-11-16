# your code goes here
order =int(input())
for i in range(order+1):
	for j in range(order,0,-1):
		if j>i:
			print(" ",end="")
		elif (j%2==0):
			print("$",end="")
		else:
			print("*",end="")
	for j in range(1,i):
		if(j%2==0):
			print("*",end="")
		else:
			print("$",end="")
	print('')