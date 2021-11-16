# your code goes here
def div(mid):
	res=0
	while(mid!=0):
		res+=mid//5
		mid=mid//5
	return res

for _ in range(int(input())):
	number =int(input())
	low=0
	high=10**10
	res=high
	while(low<=high):
		mid=low+(high-low)//2
		divisible=div(mid)
		if(divisible>=number):
			high=mid-1
			res=min(res,mid)
		else:
			low=mid+1
		#print("divisible=",divisible,"res=",res,"high=",high,"mid=",mid,"low=",low)
	print(res)