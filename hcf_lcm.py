def gcd(a,b):
	#print(a,b)
	if(a==0):
		return b
	return gcd(b%a,a)
#print(gcd(70,5))

#------------------------------#
#LCM 
# A*B = LCM(A,B)*GCD(A,B)
#LCM(A,B)=A*B/GCD(A,B)

def lcm(a,b):
	c=gcd(a,b)
	return (a*b)//c
print(lcm(11,13))

