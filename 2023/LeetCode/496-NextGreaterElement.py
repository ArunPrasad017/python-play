def nextGreaterElement(nums1, nums2):
    d = {n: i for i, n in enumerate(nums2)}
    res = [-1] * len(nums1)
    for i in range(len(nums1)):
        for j in range(d[nums1[i]], len(nums2)):
            if nums1[i] < nums2[j]:
                res[i] = nums2[j]
                break
    return res


nums1 = [4, 1, 2]
nums2 = [1, 3, 4, 2]
print(nextGreaterElement(nums1, nums2))