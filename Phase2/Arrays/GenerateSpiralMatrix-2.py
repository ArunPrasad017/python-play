def generateMatrix(n):
    if not n:
        return 0
    num = 1
    if n == 1:
        return [[1]]
    left, right, top, bottom = 0, n - 1, 0, n - 1
    res = [[0 for i in range(n)] for i in range(n)]
    while left <= right and top <= bottom:
        for i in range(left, right + 1):
            res[top][i] = num
            num += 1
        top += 1
        for i in range(top, bottom + 1):
            res[i][right] = num
            num += 1
        right -= 1
        for i in range(right, left - 1, -1):
            res[bottom][i] = num
            num += 1
        bottom -= 1
        for i in range(bottom, top - 1, -1):
            res[i][left] = num
            num += 1
        left += 1
    return res


n = 5
print(generateMatrix(n))
