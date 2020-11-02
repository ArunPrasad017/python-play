
def search(self, nums, target):
    def rotate_idx(l,r,nums):
        if nums[l]<nums[r]:
            return 0
        while l<=r:
            mid = l+(r-l)//2
            if nums[mid]>nums[mid+1]:
                return mid+1
            else:
                if nums[mid]>=nums[l]:
                    l = mid+1
                else:
                    r = mid-1
    def binary_search(left,right,nums):
        while left<=right:
            mid =left+(right-left)//2
            if nums[mid]<target:
                left = mid+1
            elif nums[mid]>target:
                right=mid-1
            else:
                return mid
            return -1
    if not nums:
        return -1
    if len(nums)==1:
        if nums[0]==target:
            return 0
        else:
            return -1
    left,right =0,len(nums)-1
    idx = rotate_idx(left,right,nums)
    if idx==0:
        return binary_search(left,right,nums)
    if nums[idx] == target:
        return idx
    if target<nums[0]:
        return binary_search(idx,right,nums)
    else:
        return binary_search(left,idx,nums)
    return -1
            