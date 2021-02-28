def twoSum(nums, target):
    if len(nums)==2:
        return [1,2] if nums[0]+nums[1]==target else -1
    left,right = 0,len(nums)-1
    res =[]
    for i,n in enumerate(nums):
        tgt = target-n
        left,right=i+1,len(nums)-1
        while left<=right:
            mid = left+(right-left)//2
            if nums[mid]==tgt:
                res.append(i+1)
                res.append(mid+1)
                return res
            elif nums[mid]>tgt:
                right=mid-1
            else:
                left=mid+1
    return [-1,-1]

nums = [2,7,11,15]
target = 9
print(twoSum(nums,target))