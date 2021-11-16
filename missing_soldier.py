# your code goes here
import math
barriers=int(input())
previousEnd=float("inf")
res=0
for i in range(barriers):
	x,y,width=map(int,input().split())
	end=y+width-x+1
	res+=end
	if(math.isinf(previousEnd)):
		previousEnd=res
	else:
		overlap=previousEnd-x+1
		if(overlap<0):
			res+=0
		elif(overlap==0):
			res-=1
		else:
			res-=overlap
	
			
		
		
print(res)