def moveZeroes(nums):
    slowPtr, fastPtr = 0, 0
    for fastPtr in range(len(nums)):
        if nums[fastPtr] != 0:
            nums[fastPtr], nums[slowPtr] = nums[slowPtr], nums[fastPtr]
        if nums[slowPtr] != 0:
            slowPtr += 1
        fastPtr += 1
    return nums


nums = [0, 1, 0, 3, 12]
print(moveZeroes(nums))
