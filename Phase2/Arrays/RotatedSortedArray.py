def findMin(nums):
    left,right=0,len(nums)-1
    if nums[left]<nums[right]:
        return nums[0]
    while left<right:
        mid = left+(right-left)//2
        if nums[mid]>nums[mid+1]:
            return nums[mid+1]
        elif nums[mid]>nums[right]:
            left=mid+1
        else:
            right=right-1
    return nums[left]

nums = [4,5,6,7,0,1]
print(findMin(nums))