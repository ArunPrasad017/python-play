def searchMatrix(matrix, target):
    if len(matrix) == 0 or matrix == None:
        return 0
    row = 0
    col = len(matrix[0]) - 1
    rlength = len(matrix)
    while row < rlength and col >= 0:
        if target == matrix[row][col]:
            return True
        if target < matrix[row][col]:
            col -= 1
        elif target > matrix[row][col]:
            row += 1
    return False


x = [
    [1, 4, 7, 11, 15],
    [2, 5, 8, 12, 19],
    [3, 6, 9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30],
]
print(searchMatrix(x, 499))
