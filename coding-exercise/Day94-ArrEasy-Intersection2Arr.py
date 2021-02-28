from collections import Counter
def intersection(nums1, nums2):
    dict1 = Counter()
    res = []
    if len(nums1)>len(nums2):
        nums1, nums2 = nums2, nums1
    for num in nums1:
        dict1[num]+=1
    for num in nums2:
        if num in dict1 and dict1[num]!=0:
            dict1[num]-=1
            res.append(num)
    return res

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
print(intersection(nums1, nums2))
