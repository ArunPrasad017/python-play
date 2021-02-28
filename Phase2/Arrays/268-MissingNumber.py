def missingNumber(nums):
    nums.sort()
    if nums[0]!=0:
        return 0
    if nums[-1]!=len(nums):
        return len(nums)
    slow,fast = 0, 1
    while fast!=len(nums):
        if nums[slow]+1!=nums[fast]:
            return nums[slow]+1
        slow+=1
        fast+=1
    return nums[-1]+1

nums = [9,6,4,2,3,5,7,0,1]
print(missingNumber(nums))