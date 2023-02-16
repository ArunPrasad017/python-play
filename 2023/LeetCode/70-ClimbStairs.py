def climbStairs(n):
    if n < 1:
        return 0
    lst = [1] * (n + 1)
    for i in range(2, n + 1):
        lst[i] = lst[i - 2] + lst[i - 1]
    return lst[n]


print(climbStairs(10))