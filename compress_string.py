def compress(st):
	val=0
	res=""
	for i in range(len(st)):
		if(i==0):
			val=1
		elif(i==len(st)-1):
			if(st[i]==st[i-1]):
				val+=1
				if(val>1):
					res+=st[i-1]+str(val)
			else:
				if(val>1):
					res+=st[i-1]+str(val)
					res+=st[i]
				else:
					res+=st[i-1]+st[i]
					#print("hello")
		elif(st[i]==st[i-1]):
			val+=1
			#print(st[i])	
		else:
			if(val>1):
				res+=st[i-1]+str(val)
			else:
				res+=st[i-1]
			val=1
			#print(st[i],val)
	print(res)
	
			

       ### Complete this function.

t = int(input())
for _ in range(t):
    st = input()
    compress(st)