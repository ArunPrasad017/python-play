"""
Given an integer array, find three numbers whose product is maximum and output the maximum product.

Input: [1,2,3,4]
Output: 24

"""
def maxProduct(nums):
    nums.sort()
    return max((nums[-3]*nums[-2]*nums[-1]), (nums[0]* nums[1]*nums[-1]))

nums= [-4,-3,-2,-1,60]
print(maxProduct(nums))