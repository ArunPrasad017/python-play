# [10,-1,20,4,5,-9,-6]
# [-1,-9,-6,10,20,4,5]

# --try1
# def rearrange(nums):
#     ptr1,ptr2 = 0,1
#     n=len(nums)
#     while ptr1<n and ptr2<n:
#         if nums[ptr1]>0 and nums[ptr2]>0:
#             ptr1+=1
#             ptr2+=1
#         elif nums[ptr1]>0 and nums[ptr2]<0:
#             nums[ptr1],nums[ptr2]=nums[ptr2],nums[ptr1]
#         elif nums[ptr1]<0 and nums[ptr2]>0:
#             ptr2+=1
#         elif nums[ptr1]<0 and nums[ptr2]<0:
#             ptr1+=1
#             ptr2+=1
#     return nums

# --try2 (using two temp lists for negative and positive - which will not be ideal as it's twice to go through array and extra space)

# --try3 (rearranging in place)
def rearrange(nums):
    left_most_pos = 0
    for i in range(len(nums)):
        if nums[i]<0:
            if i != left_most_pos:
                nums[i],nums[left_most_pos] = nums[left_most_pos],nums[i]
            left_most_pos+=1
    return nums

print(rearrange([10,-1,20,4,5,-9,-6]))