def arraySign(nums):
    res = 1
    for i in range(len(nums)):
        res = res * nums[i]
    if res > 0:
        return 1
    elif res < 0:
        return -1
    else:
        return 0


nums = [1, 2, 4, -1, 2, -2]
arraySign()