def findMin(nums):
    if not nums:
        return 0
    left,right = 0,len(nums)-1
    while left<right:
        mid = left+(right-left)//2
        if nums[mid]<nums[right]:
            right=mid
        elif nums[mid]>nums[right]:
            left=mid+1
        else:
            right-=1
    return nums[left]

nums = [2,2,2,0,1]
nums=[1,3,5]
print(findMin(nums))