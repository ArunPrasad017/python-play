def findDuplicate(nums):
    left,right=0,len(nums)-1
    while left<right:
        mid = left+(right-left)//2
        count = 0
        for i in nums:
            if i<=mid:
                count+=1
        if count<=mid:
            left=mid+1
        else:
            right=mid
    return left

nums = [1,3,4,2,2]
print(findDuplicate(nums))