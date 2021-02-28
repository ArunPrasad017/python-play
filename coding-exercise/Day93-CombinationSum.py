def dfs(lst, res, temp, start_idx, target):
    if target == 0:
        res.append(temp[:])
        return
    for i in range(start_idx, len(lst)):
        if lst[i] > target:
            return
        temp.append(lst[i])
        # dfs(lst, res, temp, start_idx, target-lst[i])
        dfs(lst, res, temp, i, target - lst[i])
        temp.pop()


def combinationSum(lst, target):
    lst.sort()
    res, temp = [], []
    dfs(lst, res, temp, 0, target)
    return res


# candidates = [2,3,6,7]
# target = 7
# print(combinationSum(candidates, target))


def dfs(lst, res, temp, start_idx, target):
    if target == 0:
        res.append(temp[:])
        return
    for i in range(start_idx, len(lst)):
        if lst[i] > target:
            return
        temp.append(lst[i])
        # dfs(lst, res, temp, start_idx, target-lst[i])
        dfs(lst, res, temp, i + 1, target - lst[i])
        temp.pop()


def combinationSum2(lst, target):
    lst.sort()
    res, temp = [], []
    dfs(lst, res, temp, 0, target)
    return res


candidates = [
    135,
    101,
    170,
    125,
    79,
    159,
    163,
    65,
    106,
    146,
    82,
    28,
    162,
    92,
    196,
    143,
    28,
    37,
    192,
    5,
    103,
    154,
    93,
    183,
    22,
    117,
    119,
    96,
    48,
    127,
    0,
    172,
    0,
    139,
    0,
    0,
    70,
    113,
    68,
    100,
    36,
    95,
    104,
    12,
    123,
    134,
]
target = 468
print(combinationSum2(candidates, target))
