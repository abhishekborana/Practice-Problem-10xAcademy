# your code goes here
#### Flag Approach if 1 added than adding zero otherwise ################

def check(arr,k,i,s,c):
	if(c==k):
		arr.append(s)
		return
	if(i==1):
		check(arr,k,0,s+"0",c+1)
	else:
		check(arr,k,0,s+"0",c+1)
		check(arr,k,1,s+"1",c+1)

k=int(input())
if(k<=0):
	print(0)
else:
	arr=[]
	check(arr,k,0,"",0)
	arr.sort()
	print(*arr)


######################################## Second Approach ##############################################
##### Checking last char if it is "1" or not #########
# your code goes here
def check(arr,k,i,s,c):
	if(c==k):
		arr.append(s)
		return
	if(len(s)>=1):
		if(s[-1]=="1"):
			check(arr,k,0,s+"0",c+1)
		else:
			check(arr,k,0,s+"0",c+1)
			check(arr,k,0,s+"1",c+1)
	else:
		check(arr,k,0,s+"1",c+1)
		check(arr,k,0,s+"0",c+1)

k=int(input())
if(k<=0):
	print(0)
else:
	arr=[]
	check(arr,k,0,"",0)
	arr.sort()
	print(*arr)