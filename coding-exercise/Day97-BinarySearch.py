def search(nums, target):
    if len(nums) == 1 and nums[0] == target:
        return 0
    left = 0
    right = len(nums)-1
    while left<=right:
        mid=left+(right-left)//2
        if nums[mid] == target:
            return mid
        if nums[mid]>target:
            right=mid-1
        if nums[mid]<target:
            left=mid+1
    return -1

s = [-1,0,3,5,17,20]
t = 20
print(search(s,t))