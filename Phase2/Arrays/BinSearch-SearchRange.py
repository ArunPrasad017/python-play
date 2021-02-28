def extreme_insertion_idx(nums, target,left):
    low, high = 0,len(nums)-1
    while low<high:
        mid = low+(high-low)//2
        if nums[mid]>target or (left and target==nums[mid]):
            high=mid
        else:
            low=mid+1
    return low


def searchRange(nums,target):
    left_idx = extreme_insertion_idx(nums,target,True)
    if left_idx==len(nums) or nums[left_idx]!=target:
        return [-1,-1]
    return [left_idx, extreme_insertion_idx(nums,target,False)-1]


nums = [5,7,7,8,8,10]
target = 8
print(searchRange(nums,target))