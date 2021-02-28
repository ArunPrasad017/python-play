def removeDuplicates(nums):
    for idx, i in enumerate(nums):
        temp = nums[idx]
        for item in nums[idx+1:]:
            if temp<item:
                break
            if temp==item:
                nums.remove(item)
    return len(nums)
nums = [0,0,1,1,1,2,2,3,3,4]
print(removeDuplicates(nums))