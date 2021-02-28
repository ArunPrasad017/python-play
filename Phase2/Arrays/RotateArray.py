def rotate(matrix):
    """
    modify matrix in-place
    """
    for i in range(len(matrix)):
        for j in range(i, len(matrix[0])):
            matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]
    for k in range(len(matrix)):
        matrix[k] = matrix[k][::-1]
    return matrix


matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
print(rotate(matrix))
