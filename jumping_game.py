# your code goes here
def game(arr,i,con,res):
	print(arr,i,con,res)
	if(i>=len(arr)):
		res.append(con)
		return
	game(arr,i+1,con+1,res)
	game(arr,i+arr[i],con+1,res)

size=int(input())
arr=list(map(int,input().split()))
res=[]
game(arr,0,0,res)
print(min(res))