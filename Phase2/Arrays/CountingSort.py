def sortColors(nums):
    res = []
    temp = [0] * 10
    for i in range(len(nums)):
        idx = nums[i]
        temp[idx] += 1
    for i in range(10):
        while temp[i] > 0:
            res.append(i)
            temp[i] -= 1
    return res


nums = [2, 0, 2, 1, 1, 0]
print(sortColors(nums))
