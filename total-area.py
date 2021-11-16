# your code goes here
for i in range(int(input())):
	a1,b1,c1,d1,a2,b2,c2,d2=map(int,input().split())
	l1 = [a1, b1]
	r1 = [c1, d1]
	l2 = [a2, b2]
	r2 = [c2, d2]
	x=0
	y=1
	area1=abs(l1[x] - r1[x]) * abs(l1[y] - r1[y])
	area2=abs(l2[x] - r2[x]) * abs(l2[y] - r2[y])
	xIntersect = (min(r1[x], r2[x]) -max(l1[x], l2[x]))
	yIntersect = (min(r1[y], r2[y]) -max(l1[y], l2[y]))
	area3=0
	if(xIntersect>0 and yIntersect>0):
		area3=xIntersect*yIntersect
	print(area1+area2-area3)
