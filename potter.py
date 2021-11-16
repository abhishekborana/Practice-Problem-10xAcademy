# your code goes here
for i in range(int(input())):
	size,rotation=map(int,input().split())
	arr=list(map(int,input().split()))
	if(rotation>=size):
		rotation=rotation%size
	print(*arr[rotation : ],*arr[:rotation])