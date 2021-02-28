def intersect(nums1, nums2):
    dict1 = {}
    nums3 = []
    for c in nums1:
        if c not in dict1:
            dict1[c] = 1
        else:
            dict1[c] += 1
    for c in nums2:
        if c in dict1 and dict1[c] != 0:
            dict1[c] -= 1
            nums3.append(c)
    return nums3


nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]
print(intersect(nums1, nums2))
