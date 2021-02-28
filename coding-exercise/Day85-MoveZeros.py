def moveZeroes(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    slowPtr, fastPtr = 0, 0
    while fastPtr in range(len(nums)):
        if nums[fastPtr] != 0:
            nums[slowPtr], nums[fastPtr] = nums[fastPtr], nums[slowPtr]
        if nums[slowPtr] != 0:
            slowPtr += 1
        fastPtr += 1
    return nums


print(moveZeroes([0, 1, 0, 3, 12]))
