def twoSum(nums,res,i):
    left, right =i+1, len(nums)-1
    while left<right:
        target = nums[i]+nums[left]+nums[right]
        if target==0:
            temp = [nums[left],nums[right],nums[i]]
            res.append(temp)
            left+=1
            right-=1
            while left<right and nums[left]==nums[right]:
                left+=1
        elif target>0:
            right-=1
        else:
            left+=1
    
def threeSum(nums):
    res = []
    if not nums:
        return res
    nums.sort()
    for i in range(len(nums)):
        if nums[i]>0:
            break
        elif nums[i]!=nums[i-1]:
            twoSum(nums,res,i)
    return res

nums = [-1,0,1,2,-1,-4]
print(threeSum(nums))