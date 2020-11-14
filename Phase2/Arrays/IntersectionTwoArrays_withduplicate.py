def binary_search(nums,tgt):
    left,right = 0,len(nums)-1
    while left<=right:
        mid = left+(right-left)//2
        if nums[mid]==tgt:
            return True
        else:
            if nums[mid]>tgt:
                right=mid-1
            else:
                left=mid+1
    return False

def intersect(nums1, nums2):
    if len(nums1)<len(nums2):
        nums1,nums2 = nums2,nums1
    res = []
    nums1.sort()
    for item in nums2:
        if binary_search(nums1,item):
            res.append(item)
            nums1.remove(item)
    return res

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
print(intersect(nums1,nums2))