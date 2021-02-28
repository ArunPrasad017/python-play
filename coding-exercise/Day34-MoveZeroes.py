def moveZeroes(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    slow_ptr = 0
    fast_ptr = 0

    while fast_ptr < len(nums):
        if nums[fast_ptr] != 0:
            nums[slow_ptr], nums[fast_ptr] = nums[fast_ptr], nums[slow_ptr]
        if nums[slow_ptr] != 0:
            slow_ptr += 1
        fast_ptr += 1
    return nums


nums = [0, 1, 3, 12, 0]
print(moveZeroes(nums))
