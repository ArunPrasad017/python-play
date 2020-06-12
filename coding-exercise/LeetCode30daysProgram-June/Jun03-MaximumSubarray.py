"""
Given an integer array nums, find the contiguous subarray (containing at least one number) 
which has the largest sum and return its sum.

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Hint: Dynamic Programming
"""
import pytest
def maxSubarray(nums):
    max_sum = nums[0]
    
    for i in range(1, len(nums)):
        if nums[i-1]>0:
            nums[i]+=nums[i-1]
            max_sum =max(nums[i],max_sum)
    return max_sum

def test_maxSubarray():
    assert maxSubarray([-2,1,-3,4,-1,2,1,-5,4]) == 6
    assert maxSubarray([-2,1,-3,4,-1,2,1,-5,4]) == 5