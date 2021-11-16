# your code goes here
def grovyle_string(s,sortedS):
	end=len(s)-1
	right=len(s)//2 +1
	left=right-2
	res=[0]*len(s)
	res[len(s)//2]=sortedS[end]
	end-=1
	while(left>=0 and right<len(s)):
		res[right]=sortedS[end]
		end-=1
		res[left]=sortedS[end]
		end-=1
		left-=1
		right+=1
	res="".join(res)
	return res

for _ in range(int(input())):
	s=input()
	sortedS=list(s)
	sortedS.sort()
	sortedS="".join(sortedS)
	print(grovyle_string(s,sortedS))