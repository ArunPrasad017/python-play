def maxSubArray(nums):
    maxVal = nums[0]
    for i in range(1, len(nums)):
        if nums[i - 1] > 0:
            nums[i] += nums[i - 1]
        maxVal = max(maxVal, nums[i])
    return maxVal


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(maxSubArray(nums))
