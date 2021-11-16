# Given a 2D integer matrix and a list of cell indexes e.g.,
# an array of (i, j) where i indicates row and j column.
# For every given cell index (i, j), find sums of all matrix elements
# except the elements present in i’th row and/or j’th column.

mtx = [[2, 3, 4],
        [2, 0, 1],
        [6, -3, -5]]


queries = [[1, 2], [0, 1], [1, 1], [2, 2]]

def mtxSumExPair(mtx, n, m, queries):
    mtxSum = 0

    rowSum = [0] * n
    colSum = [0] * m

    for i in range(n):              # 0, 1, 2
        for j in range(m):          # 0, 1, 2
            mtxSum += mtx[i][j]
            rowSum[i] += mtx[i][j]
            colSum[j] += mtx[i][j] 

    # rowSum = [0] * n # rowSum[0] = 
    # colSum = [0] * m

    # for i in range(n):
    #     for j in range(m):
    #         rowSum[i] += mtx[i][j]

    # for j in range(m):
    #     for i in range(n):
    #         colSum[j] += mtx[i][j]
    
    for q in queries:
        [i, j] = q

        print(mtxSum - rowSum[i] - colSum[j] + mtx[i][j])

mtxSumExPair(mtx, len(mtx), len(mtx[0]), queries)

# mtxSum      rowSum      colSum
# 10          [9, 3, -2]  [10, 0, 0]

# queries[i, j]       sum - rowSum[i] - colSum[j] + mtx[i][j]
# [1, 2]              10 - 3 - 0 + 1 = 8
# [0, 1]              10 - 9 - 0 + 3 = 4
# [1, 1]
# [2, 2]
