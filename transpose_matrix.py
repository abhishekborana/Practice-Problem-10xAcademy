# name you function as transpose_matrix and takes a list
# you should return a list of lists
def transpose_matrix(mat):
	res=[]
	for col in range(len(mat[0])):
		currCol=[]
		for row in range(len(mat)):
			currCol.append(mat[row][col])
		res.append(currCol)
	return res
			



# do not change anything below this line
if __name__ == "__main__":
    h = int(input())
    lst = []
    for val in range(0, h):
        lst.append([int(i) for i in input().split(' ')])
    out = transpose_matrix(lst)
    for val in out:
        print(" ".join(str(i) for i in val))