def merge(nums1, m, nums2, n):
    # two pointer from behind
    p1,p2 = m-1,n-1
    p=m+n-1
    while p1>=0 and p2>=0:
        if nums1[p1]<=nums2[p2]:
            nums1[p]=nums2[p2]
            p2-=1
        else:
            nums1[p]=nums1[p1]
            nums1[p1]=nums2[p2]
            p1-=1
        p-=1
    return nums1

nums1=[1,2,3,0,0,0]
nums2 = [2,5,6]
print(merge(nums1,3,nums2,3))