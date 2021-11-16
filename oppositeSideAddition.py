# your code goes here
# your code goes here
testCase =int(input())
carry=0

def checking_sum(num1,num2,carry):
	res=[]
	for i in range(len(num1)):
		n = int(num1[i])+int(num2[i])+carry
		carry=0
		if(n>=10):
			n2=n
			n=n%10
			carry=n2//10
			res.append(n)
			if(i==(len(num1)-1) and carry>=1):
				res.append(carry)
		else:
			res.append(n)
			if(i==(len(num1)-1) and carry>=1):
				res.append(carry)
	return res
	



num1=[]
num2=[]
res=[]
for i in range(testCase):
	num1 = list(input().split())
	num2 = list(input().split())
	n1=len(num1)
	n2=len(num2)
	if(n1>n2):
		n1=n1-n2
		list2=[0]*n1
		num2=num2+list2
	else:
		n2=n2-n1
		list2=[0]*n2
		num1=num1+list2
	res=checking_sum(num1,num2,carry)
	print("".join(map(str,res)))

		
		