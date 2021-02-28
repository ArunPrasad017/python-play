def remove_duplicates(nums):
    for i in range(len(nums)-1,-1,-1):
        if nums[i] == nums[i-1]:
            del(nums[i])
    return nums

nums = [1,1,2]
print(remove_duplicates(nums))
nums = [0,0,1,1,1,2,2,3,3,4]
print(remove_duplicates(nums))