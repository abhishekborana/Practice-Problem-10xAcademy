def reverseSelectionSort(A, n):
	
	for i in range(1,n):
		j=i
		while(j>0 and A[j]>A[j-1]):
			A[j],A[j-1]=A[j-1],A[j]
			j-=1
	return A
    

if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        arr = [int(x) for x in input().split()]
        print(*reverseSelectionSort(arr, n))