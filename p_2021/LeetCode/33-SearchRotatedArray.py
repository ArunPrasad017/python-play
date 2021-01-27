def search(nums,target):
    def binary_search(left,right):
        while left<=right:
            mid = left+(right-left)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                right=mid-1
            else:
                left=mid+1
        return -1
            
    def func_rotation_idx(left,right,nums):
        if nums[left]<nums[right]:
            return 0
        while left<=right:
            mid = left+(right-left)//2
            if nums[mid]>nums[mid+1]:
                return mid+1
            else:
                if nums[mid]>=nums[left]:
                    left+=1
                else:
                    right-=1
        return 0
    # corner case
    if not nums:
        return -1
    elif len(nums)==1:
        if nums[0]==target:
            return 0
        else:
            return -1
    rotation_idx = func_rotation_idx(0,len(nums)-1,nums)
    if target==nums[rotation_idx]:
        return rotation_idx
    if not rotation_idx:
        return binary_search(0,len(nums)-1)
    elif target<nums[0]:
        return binary_search(rotation_idx+1,len(nums)-1)
    else:
       return binary_search(0,rotation_idx-1)
    return -1

lst = [5,1,3]
tgt = 3
print(search(lst,tgt))