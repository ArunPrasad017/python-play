def intersect(nums1, nums2):
    # set1,set2 = set(nums1), set(nums2)
    # return set1.intersection(set2)
    if len(nums1) < len(nums2):
        nums1, nums2 = nums2, nums1
    dict1, res = {}, []
    for n in nums1:
        if n not in dict1:
            dict1[n] = 1
        else:
            dict1[n] += 1
    for n in nums2:
        if n in dict1 and dict1[n] != 0:
            dict1[n] -= 1
            res.append(n)
    return res


nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]
print(intersect(nums1, nums2))
