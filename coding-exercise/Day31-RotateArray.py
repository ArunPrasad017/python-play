def rotate(nums, k):
    if k > len(nums):
        k %= len(nums)
    nums[:] = nums[::-1]
    nums[:] = nums[:k][::-1] + nums[k:][::-1]
    return nums


nums = [1, 2, 3, 4, 5, 6, 7]
# nums = [-1]
print(rotate(nums, 3))
