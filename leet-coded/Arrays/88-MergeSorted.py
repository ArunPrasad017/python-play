# Modify to add to new array
#  def merge(nums1,nums2,m,n):
#     nums3 = []
#     while m>0 and n>0:
#         if nums1[0]<=nums2[0]:
#             nums3.append(nums1.pop(0))
#             m-=1
#         else:
#             nums3.append(nums2.pop(0))
#             n-=1
#     if m==0:
#         return nums3+nums2[:n]
#     if n==0:
#         return nums3+nums1[:m]

# Modify to update arrays in place
# using the double ptr with temp array -
# TC: o(m+n) SC: o(n)
# def merge(nums1,nums2,m,n):
#     nums1_copy = nums1[:m]
#     nums1[:] = []
#     p1,p2 = 0,0

#     while p1<m and p2<n:
#         if nums1_copy[p1] <= nums2[p2]:
#             nums1.append(nums1_copy[p1])
#             p1+=1
#         else:
#             nums1.append(nums2[p2])
#             p2+=1
#     if p2<n:
#         nums1+=nums2[p2:]
#     if p1<m:
#         nums1+=nums1_copy[p1:]
#     return nums1

# Modify to update arrays in place
# Without temporary array and using double ptr technique
def merge(nums1, nums2, m, n):
    p1, p2 = m - 1, n - 1
    p = m + n - 1

    while p1 >= 0 and p2 >= 0:
        if nums1[p1] <= nums2[p2]:
            nums1[p] = nums2[p2]
            p2 -= 1
        else:
            nums1[p] = nums1[p1]
            p1 -= 1
        p -= 1
    nums1[: p2 + 1] = nums2[: p2 + 1]
    return nums1


nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3

print(merge(nums1, nums2, m, n))
