def merge(nums1, m, nums2, n):
    """
    merging in place
    """
    p1,p2 = m-1,n-1
    p = m+n-1
    while p1>=0 and p2>=0:
        if nums1[p1]<nums2[p2]:
            nums1[p]=nums2[p2]
            p2-=1
        else:
            nums1[p] = nums1[p1]
            nums1[p1]= nums2[p2]
            p1-=1
        p-=1
    for i in range(p2+1):
        nums1[i] = nums2[i]
    return nums1


nums1,nums2 = [1,2,3,0,0,0], [2,5,6]
m,n = 3, 3
print(merge(nums1, m, nums2, n))