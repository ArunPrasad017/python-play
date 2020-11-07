def bin_search(nums1,target):
    l,r = 0, len(nums1)-1
    while l<=r:
        mid = l+(r-l)//2
        if nums1[mid]==target:
            nums1.pop(mid)
            return True
        else:
            if nums1[mid]>target:
                r=mid-1
            else:
                l=mid+1
    return False

def intersection(nums1,nums2):
    if len(nums1)<len(nums2):
        nums1,nums2 = nums2,nums1
    nums1.sort()
    res = []
    for c in nums2:
        if bin_search(nums1,c):
            res.append(c)
    return res

nums1 = [1,2,2,1]
nums2 = [2,2]
print(intersection(nums1,nums2))
nums1 = [3,1,2]
nums2 = [1]
print(intersection(nums1,nums2))
nums1= [4,9,5]
nums2= [9,4,9,8,4]
print(intersection(nums1,nums2))

nums1=[1,2]
nums2=[1,1]
print(intersection(nums1,nums2))