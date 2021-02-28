def twoSum(nums, target):
    left,right = 0,len(nums)-1
    while left<right:
        sum_val = nums[left]+nums[right]
        if sum_val == target:
            return [left+1,right+1]
        elif sum_val<target:
            left+=1
        else:
            right-=1