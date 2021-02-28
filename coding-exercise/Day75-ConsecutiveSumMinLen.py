"""
209. Minimum Size Subarray Sum

Given an array of n positive integers and a positive integer s, 
find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

Example: 
Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.
"""
def minSubArrayLen(s, nums):
    if not nums:
        return 0
    ptr1 = ptr2 = 0
    res = float('inf')
    sumVal = nums[ptr1]
    while ptr2<len(nums):
        if sumVal>=s:
            res = min(res,ptr2-ptr1+1)
            sumVal-=nums[ptr1]
            ptr1+=1
        else:
            ptr2+=1
            if ptr2<len(nums):
                sumVal+=nums[ptr2]
            else:
                break
    return res if res!=float('inf') else 0

lst = [2,3,1,2,4,3]
s = 7
print(minSubArrayLen(s,lst))