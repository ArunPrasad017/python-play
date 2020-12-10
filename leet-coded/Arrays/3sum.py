# Given an array nums of n integers,
# are there elements a, b, c in nums such that a + b + c = 0?
# Find all unique triplets in the array which gives the sum of zero.


def threeSum(nums):

    nums.sort()
    res = []

    length = len(nums)

    for i in range(length - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        l = i + 1
        r = length - 1

        while l < r:
            sum_val = nums[i] + nums[l] + nums[r]
            if sum_val < 0:
                l = l + 1
            elif sum_val > 0:
                r = r - 1
            else:
                res.append([nums[i], nums[l], nums[r]])
                while l < r and nums[l] == nums[l + 1]:
                    l = l + 1
                while l < r and nums[r] == nums[r - 1]:
                    r = r - 1
                l = l + 1
                r = r - 1
    return res


nums = [0, 0, 0]  # sorted - [-4,-1,-1,0,1,2]

print(threeSum(nums))
