"""
"""


def minSubArrayLen(s, nums):
    if not nums:
        return 0
    ptr1 = ptr2 = 0
    n = len(nums)
    sumVal = nums[0]
    res = float("inf")
    while ptr2 < n:
        if sumVal >= s:
            res = min(res, ptr2 - ptr1 + 1)
            sumVal -= nums[ptr1]
            ptr1 += 1
        else:
            ptr2 += 1
            if ptr2 < n:
                sumVal += nums[ptr2]
            else:
                break
    return res if res != float("inf") else 0


s = 7
nums = [2, 3, 1, 2, 4, 3]
print(minSubArrayLen(s, nums))
