def maximalSquare(matrix):
    m = len(matrix)
    n = len(matrix[0])
    height = 0
    res_matrix = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if matrix[i - 1][j - 1] == "1":
                res_matrix[i][j] = 1 + min(
                    res_matrix[i - 1][j], res_matrix[i][j - 1], res_matrix[i - 1][j - 1]
                )
                height = max(height, res_matrix[i][j])
    return height ** 2


matrix = [
    ["1", "0", "1", "0", "0"],
    ["1", "0", "1", "1", "1"],
    ["1", "1", "1", "1", "1"],
    ["1", "0", "0", "1", "0"],
]
print(maximalSquare(matrix))
