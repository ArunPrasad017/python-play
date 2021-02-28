"""
487. Max Consecutive Ones II

Given a binary array, find the maximum number of consecutive 1s in this array if you can flip at most one 0.

Example 1:
Input: [1,0,1,1,0]
Output: 4
Explanation: Flip the first zero will get the the maximum number of consecutive 1s.
    After flipping, the maximum number of consecutive 1s is 4.

Note:
The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000
"""

def findMaxConsecutiveOnes(nums):
    # sliding window concept with arrays
    zeroCnt,start,end = 0,0,0
    max_ones = 0
    for end in range(len(nums)):
        if nums[end]==0:
            zeroCnt+=1
        while zeroCnt>1:
            if nums[start]==0:
                zeroCnt-=1
            start+=1
        max_ones = max(max_ones, end-start+1)
    return max_ones

# driver code
nums = [1,1,0,0,1,1,1,1,1,1]
print(findMaxConsecutiveOnes(nums))