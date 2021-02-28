def moveZeroes(nums):
    slow_ptr,fast_ptr =0,0
    while fast_ptr<len(nums):
        if nums[fast_ptr]!=0:
            nums[fast_ptr],nums[slow_ptr]=nums[slow_ptr],nums[fast_ptr]
            slow_ptr+=1
        fast_ptr+=1
    return nums

nums = [0,1,0,3,12]
print(moveZeroes(nums))