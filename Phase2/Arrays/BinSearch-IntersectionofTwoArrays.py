def intersection(nums1, nums2):
    if len(nums1)<len(nums2):
        nums1,nums2 = nums2,nums1
    res = []
    if set(nums1)==set(nums2):
        return nums2
    nums1.sort()
    nums2 = set(nums2)
    for c in nums2:
        l,r = 0, len(nums1)-1
        while l<=r:
            mid = l+(r-l)//2
            if nums1[mid]==c:
                res.append(c)
                break
            else:
                if nums1[mid]>c:
                    r=mid-1
                else:
                    l=mid+1
    return res

nums1 = [1,2,2,1]
nums2 = [2,2]
nums1 = [3,1,2]
nums2 = [1]
print(intersection(nums1,nums2))