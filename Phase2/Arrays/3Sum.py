def twoSumPtr(nums, i, res):
    # two pointer method
    low, high = i + 1, len(nums) - 1
    while low < high:
        sumVal = nums[i] + nums[low] + nums[high]
        if sumVal > 0:
            high -= 1
        elif sumVal < 0:
            low += 1
        else:
            res.append([nums[i], nums[low], nums[high]])
            low += 1
            high -= 1
            if low < high and nums[low] == nums[low - 1]:
                low += 1


def threeSum(nums):
    if len(nums) < 3 or not nums:
        return []
    res = []
    nums.sort()
    for i in range(len(nums)):
        if nums[i] > 0:
            break
        # important to not forget this condition
        elif i == 0 or nums[i] != nums[i + 1]:
            twoSumPtr(nums, i, res)
    return res


nums1 = [-1, 0, 1, 2, -1, -4]
nums2 = [-2, 0, 0, 2, 2]
nums3 = [-1, 0, 1, 2, -1, -4, -2, -3, 3, 0, 4]

print(threeSum(nums1))
print(threeSum(nums2))
print(threeSum(nums3))
