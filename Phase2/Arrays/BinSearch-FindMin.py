def findMin(nums):
    def find_rotation_idx(nums):
        left,right = 0, len(nums)-1
        if nums[left]<nums[right]:
            return 0
        while left<right:
            mid = (left+right)//2
            if nums[mid]>nums[mid+1]:
                return mid+1
            else:
                if nums[mid]>=nums[left]:
                    left = mid+1
                else:
                    right=mid
    idx = find_rotation_idx(nums)
    return nums[idx] if idx else nums[0]

nums=[3,1,2]
print(findMin(nums))