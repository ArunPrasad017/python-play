def findMin(nums):
    #method2
    if len(nums)==1:
        return nums[0]
    def find_rotation_idx(nums):
        left,right=0,len(nums)-1
        if nums[left]<nums[right]:
            return nums[0]
        while left<=right:
            mid = left+(right-left)//2
            if nums[mid]>nums[mid+1]:
                return nums[mid+1]
            elif nums[mid]>nums[right]:
                left=mid+1
            else:
                right=mid
        return nums[left]
    return find_rotation_idx(nums)

nums = [4,5,6,7,0,1,2]
print(findMin(nums))