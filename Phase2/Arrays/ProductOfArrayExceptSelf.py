"""
238. Product of Array Except Self
"""

# def productExceptSelf(nums):
#     left,right = [1]*len(nums), [1]*len(nums)
#     for i in range(1,len(nums)):
#         left[i] = left[i-1]*nums[i-1]
#     for j in range(len(nums)-1,-1,-1):
#         if j==len(nums)-1:
#             right[j]=1
#         else:
#             right[j]=right[j+1]*nums[j+1]
#     return [a*b for a,b in zip(left,right)]

def productExceptSelf(nums):
    left,right = [1]*len(nums), [1]*len(nums)
    for i in range(1,len(nums)):
        left[i] = left[i-1]*nums[i-1]
    for j in range(len(nums)-1,-1,-1):
        right[j] = 1 if j==len(nums)-1 else right[j+1]*nums[j+1]
    return [a*b for a,b in zip(left,right)]