"""
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
Example 1:
Input: [2,2,1]
Output: 1
"""


def singleNumber(nums):
    # use of exor operation helps in determining the unique values and it reverses the numbers based on digits
    a = 0
    for num in nums:
        a ^= num
    return a


nums = [1, 1, 2]
print(singleNumber(nums))
