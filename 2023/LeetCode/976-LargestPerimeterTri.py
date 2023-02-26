def largestPerimeter(nums):
    res = 0
    nums.sort()
    for i in range(2, len(nums)):
        temp_res = float("-inf")
        if nums[i] < nums[i - 1] + nums[i - 2]:
            temp_res = nums[i] + nums[i - 1] + nums[i - 2]
        res = max(temp_res, res)
    return res


largestPerimeter([2, 1, 2])
