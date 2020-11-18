def moveZeroes(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    slow_ptr, fast_ptr =0,0
    for i in range(len(nums)):
        if nums[i]!=0:
            nums[slow_ptr],nums[fast_ptr] = nums[fast_ptr],nums[slow_ptr]
            slow_ptr+=1
        fast_ptr+=1
    return nums

nums = [0,1,0,3,12]
print(moveZeroes(nums))