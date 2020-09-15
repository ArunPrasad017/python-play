def findPeakElement(nums):
    # linear search
    i = 0
    while i+1<len(nums):
        if nums[i+1]>nums[i]:
            i+=1
        else:
            return i
    return len(nums)-1

def binarySearch_findPeakElement(nums):
    left = 0
    right = len(nums)-1
    while left<right:
        mid = (left+right)//2
        if nums[mid]>nums[mid+1]:
            right = mid
        elif nums[mid]<nums[mid+1]:
            left = mid+1
    return left

nums = [1,2,3,1]
print(binarySearch_findPeakElement(nums))