def rotate(matrix):
    """
    Do not return anything, modify matrix in-place instead.
    """
    m,n = len(matrix), len(matrix[0])
    for i in range(m):
        for j in range(i,n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for i in range(m):
        matrix[i]=matrix[i][::-1]
    return matrix

matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
print(rotate(matrix))