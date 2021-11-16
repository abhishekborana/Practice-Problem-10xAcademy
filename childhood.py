from collections import defaultdict

A=[-1]*256
d=defaultdict(int)
q=int(input())
for _ in range(q):
	charA,charB=input().lower().split()
	ordA,ordB=ord(charA),ord(charB)

	A[ordB if d[ordB]==0 else d[ordB]] = ordA
	A[ordA if d[ordA]==0 else d[ordA]] = ordB

	print(A)
	d[ordB],d[ordA]=ordA if d[ordA]==0 else d[ordA],ordB if d[ordB]==0 else d[ordB]
	print(d)
sentence=list(input())
for i in range(len(sentence)):
	curCharNumber=ord(sentence[i])
	if(curCharNumber>=65 and curCharNumber<=90):
		if(A[ord(sentence[i].lower())])!=-1:
			sentence[i]=chr(A[ord(sentence[i].lower())])
		sentence[i]=sentence[i].upper()
	else:
		if(A[ord(sentence[i].lower())])!=-1:
			sentence[i]=chr(A[ord(sentence[i].lower())])
print("".join(sentence))

