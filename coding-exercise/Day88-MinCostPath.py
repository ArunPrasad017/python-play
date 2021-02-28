def minCost(lst):
    m = len(lst) - 1
    n = len(lst[0]) - 1
    temp = [[0 for x in range(n + 1)] for y in range(m + 1)]
    sumval = 0
    temp[0][0] = lst[0][0]
    for i in range(1, m + 1):
        aboveCost = temp[i - 1][0]
        temp[i][0] = aboveCost + lst[i][0]
    for j in range(1, n + 1):
        leftCost = temp[0][j - 1]
        temp[0][j] = leftCost + lst[0][j]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            leftCost = temp[i - 1][j]
            aboveCost = temp[i][j - 1]
            diagonalCost = temp[i - 1][j - 1]
            temp[i][j] += lst[i][j] + min(leftCost, aboveCost, diagonalCost)
    return temp[m - 1][n]


#    return temp

lst = [[2, 3, 4, 5], [5, 9, 8, 7], [7, 2, 1, 1]]

city = [[-1, 5, 20], [21, -1, 10], [-1, 1, -1]]

print(minCost(city))
