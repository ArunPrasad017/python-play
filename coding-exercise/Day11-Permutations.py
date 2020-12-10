def permute(nums):
    res = []
    path = []
    used = [False] * len(nums)

    dfs(nums, res, path, used)
    return res


def dfs(nums, res, path, used):
    if len(path) == len(nums):
        res.append(path[:])
        return
    for i in range(len(nums)):
        if not used[i]:
            used[i] = True
            path.append(nums[i])
            dfs(nums, res, path, used)
            path.pop()
            used[i] = False


nums = [1, 2, 3]
print(permute(nums))
