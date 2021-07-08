"""
"""
def merge(nums1, m, nums2, n):
    """
    Do not return anything, modify nums1 in-place instead.
    """
    p1, p2 = m-1, n-1
    p = m+n-1
    while p1>=0 and p2>=0:
        if nums1[p1]<=nums2[p2]:
            nums1[p] = nums2[p2]
            p2-=1
        else:
            nums1[p] = nums1[p1]
            nums1[p1] = nums2[p2]
            p1-=1
        p-=1
    # for the corner case condition
    for i in range(p2+1):
        nums1[i] = nums2[i]

# driver code
def main():
    lst1= [4,0,0,0,0,0]
    m ,n= 1,5
    lst2 = [1,2,3,5,6]
    merge(lst1,m,lst2,n)
    print(lst1)

if __name__ == "__main__":
    main()
