def combinationSum2(nums, target):
    res = []
    lst = []
    nums.sort()
    dfs(nums, res, lst, 0, target)
    return res


def dfs(nums, res, lst, start, target):
    if target == 0 and lst not in res:
        res.append(lst[:])
        return
    for i in range(start, len(nums)):
        if nums[i] > target:
            return
        lst.append(nums[i])
        dfs(nums, res, lst, i + 1, target - nums[i])
        lst.pop()


candidates = [10, 1, 2, 7, 6, 1, 5]
target = 8
print(combinationSum2(candidates, target))
