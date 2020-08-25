def removeDuplicates(nums):
    for i, c in enumerate(nums):
        temp = nums[i]
        for i in nums[i+1:]:
            if i>temp:
                break
            if temp==i:
                nums.remove(i)
    return nums

nums = [1,1,2]
print(removeDuplicates(nums))