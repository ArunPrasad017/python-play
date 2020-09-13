"""
You are given an integer array nums sorted in ascending order, and an integer target.

Suppose that nums is rotated at some pivot unknown to you beforehand (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

If target is found in the array return its index, otherwise, return -1.

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
"""

def func_rotation_index(nums,left,right):
    if nums[left]<nums[right]:
        return 0
    while left<=right:
        mid = left+(right-left)//2
        if nums[mid]>nums[mid+1]:
            return mid
        else:
            if nums[mid]>=nums[left]:
                left = mid+1
            else:
                right = mid-1

def binary_search(nums,left,right,target):
    while left<=right:
        mid = left+(right-left)//2
        if nums[mid]==target:
            return mid
        else:
            if nums[mid]>target:
                right = mid-1
            else:
                left=mid+1
    return -1

def rotated_search(nums, target):
    if not nums:return -1

    if len(nums)==1:
        if nums[0] == target:
            return 0
        else:
            return -1
    left = 0
    right = len(nums)-1
    rotation_idx= func_rotation_index(nums,left,right)
    if rotation_idx == 0:
        return binary_search(nums, left,right,target)
    if nums[rotation_idx] == target:
        return rotation_idx
    elif target<nums[0]:
        return binary_search(nums,rotation_idx,right, target)
    else:
        return binary_search(nums,left,rotation_idx, target)

def main():
    nums = [4,5,6,7,0,1,2]
    target = 0
    print(rotated_search(nums,target))
    
if __name__ == "__main__":
    main()