# your code goes here
morse=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
alpha=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
code={}
for i in range(len(morse)):
	code[alpha[i]]=morse[i]

for _ in range(int(input())):
	res=[]
	r=""
	s=list(input().split())
	for i in s:
		i=i.lower()
	for i in s:
		for j in range(len(i)):
			r+=code[i[j]]
		res.append(r)
		#print(res,r)
		r=""
	print(len(list(set(res))))
    