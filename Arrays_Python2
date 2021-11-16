# Given a binary matrix, find out the maximum size square sub-matrix with all 1s. 
# For example, consider the below binary matrix.

mtx = [[0, 1, 1, 0, 1],
        [1, 1, 0, 1, 0],
        [0, 1, 1, 1, 0],
        [1, 1, 1, 1, 0],
        [1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0]]

# Maximum size sub-matrix is: 3
# 1 1 1 
# 1 1 1 
# 1 1 1


def maxSquareSubMatrix(mtx, n, m):
    res = -1

    aux = [[0] * m for i in range(n)]

    # copy first row
    for j in range(m):
        aux[0][j] = mtx[0][j]

    # copy first column
    for i in range(n):
        aux[i][0] = mtx[i][0]

    for r in range(1, n):
        for c in range(1, m):
            if mtx[r][c] == 1:
                aux[r][c] = min(aux[r - 1][c - 1], aux[r - 1][c], aux[r][c - 1]) + 1

            res = max(res, aux[r][c])
    
    return res


res =  maxSquareSubMatrix(mtx, len(mtx), len(mtx[0]))

print(res)
