"""
Write an algorithm if element in MxN matrix is 0 
then entire row and column are set to 0

Input: 
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
Output: 
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
Hint: Using constant space
"""

def setZeroes(matrix):
    if len(matrix)==0 or len(matrix[0])==0:
        return None

    m = len(matrix)
    n = len(matrix[0])
    firstRow = any(matrix[0][j]==0 for j in range(n))
    firstColumn = any(matrix[i][0]==0 for i in range(m))
    for i in range(1,m):
        for j in range(1,n):
            if matrix[i][j]==0:
                matrix[0][j]=0
                matrix[i][0]=0

    for i in range(1,m):
        for j in range(1,n):
            if matrix[i][0]==0 or matrix[0][j]==0:
                matrix[i][j]=0

    if firstRow:
        for j in range(n):
            matrix[0][j]=0

    if firstColumn:
        for i in range(m):
            matrix[i][0]=0

    return matrix
matrix = [[1,1,1],[1,0,1],[1,1,1]]
matrix2 =[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]

matrix3= [[1,0]]
print(setZeroes(matrix3))