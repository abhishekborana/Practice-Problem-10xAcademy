def minDiff(arr, arr_size):
	if(arr_size<=1):
		return "NA"
	else:
		res=float('inf')
		arr.sort()
		for i in range(1,len(arr)):
			if(arr[i]-arr[i-1]<res):
				res=arr[i]-arr[i-1]
		return res

def maxDiff(arr, arr_size):
	if(arr_size<=1):
		return "NA"
	else:
		maxi=max(arr)
		mini=min(arr)
		return (maxi-mini)
	

def prodDiff(arr, arr_size):
	### Complete this and the above functions!
	mini= minDiff(arr, arr_size)
	maxi=maxDiff(arr, arr_size)
	if(mini=="NA" or maxi=="NA"):
		return "NA"
	else:
		return mini*maxi

for _ in range(int(input())):
    length = int(input())
    arr = [int(x) for x in input().split()]
    print(prodDiff(arr, length))