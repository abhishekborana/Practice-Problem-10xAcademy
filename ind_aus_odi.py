# your code goes here
def game(matchesRes,matches,wins,played,won,s):
	if(played==matches):
		if(won>=wins):
			matchesRes.append(s)
		return
	game(matchesRes,matches,wins,played+1,won+1,s+"I")
	game(matchesRes,matches,wins,played+1,won,s+"A")

matches=int(input())
wins=0
if(matches%2==0):
	wins=matches//2+1
else:
	wins=(matches+1)//2
matchesRes=[]
game(matchesRes,matches,wins,0,0,"")
matchesRes.sort()
for i in matchesRes:
	print(i)