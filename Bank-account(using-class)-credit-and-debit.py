# your code goes here
class Bank:
	def __init__(self,balance):
		self.balance=balance
	def credit(self,credit):
		self.balance+=credit
	def debit(self,debit):
		self.balance+=debit

myaccount=Bank(0)
for i in range(int(input())):
	m=int(input())
	if(m>0):
		myaccount.credit(m)
	else:
		myaccount.debit(m)
print(myaccount.balance)