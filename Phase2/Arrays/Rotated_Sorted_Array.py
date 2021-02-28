def findInRotatedSortedArray(nums,target):
    if len(nums)==1:
        return 0 if nums[0]==target else -1
    if len(nums)==0:
        return -1
    left,right = 0,len(nums)-1
    while left<=right:
        mid =left+(right-left)//2
        if nums[mid]==target:
            return mid
        elif nums[mid]<nums[left]:
            if nums[mid]<target and target<=nums[right]:
                left=mid+1
            else:
                right=mid-1
        else:
            if target<nums[mid] and target>=nums[left]:
                right=mid-1
            else:
                left=mid+1
    return -1



nums = [4,5,6,7,0,1,2,3]
target = 3
print(findInRotatedSortedArray(nums,target))