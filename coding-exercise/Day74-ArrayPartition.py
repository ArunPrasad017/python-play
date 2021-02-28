"""
561. Array Partition I
Given an array of 2n integers, your task is to group these integers into n pairs of integer, 
say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of min(ai, bi) for all i from 1 to n as large as possible.

Example 1:
Input: [1,4,3,2]
Output: 4
Explanation: n is 2, and the maximum sum of pairs is 4 = min(1, 2) + min(3, 4).
"""


def arrayPairSum(nums):
    # easy method
    nums.sort()
    return sum(nums[::2])


def arrayPairsTwoPointer(nums):
    nums.sort()
    pos1 = 0
    total = 0
    if len(nums) == 2:
        return min(nums)
    for pos2 in range(1, len(nums) - 1 + 1, 2):
        total += min(nums[pos1], nums[pos2])
        pos1 += 2
    return total


def arrayPairsSourcery(nums):
    # using for instead of while - this is a suggested method by sourcery
    nums.sort()
    pos1 = 0
    total = 0
    if len(nums) == 2:
        return min(nums)
    for pos2 in range(1, len(nums), 2):
        total += min(nums[pos1], nums[pos2])
        pos1 += 2
    return total
