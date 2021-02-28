def twoSum(nums, i, res):
    seen = set()
    j = i + 1
    while j < len(nums):
        composite = -nums[i] - nums[j]
        if composite in seen:
            res.append([nums[i], nums[j], composite])
            while j + 1 < len(nums) and nums[j] == nums[j + 1]:
                j += 1
        seen.add(nums[j])
        j += 1


def threeSum(nums):
    res = []
    if not nums:
        return res
    for i in range(len(nums)):
        if i > 0:
            break
        elif i == 0 or nums[i] != nums[i - 1]:
            twoSum(nums, i, res)
    return res


nums = [-1, 0, 1, 2, -1, -4]
print(threeSum(nums))
