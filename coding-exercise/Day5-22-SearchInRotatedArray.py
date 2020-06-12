"""
33. Search in Rotated Sorted Array

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Hint:Use Binary search tree to find the elemenet
 and find the rotation index using similar technique
"""
import pytest
def search(nums,target):
    if len(nums)==1:
        return 0 if nums[0]==target else -1
    if len(nums)==0:
        return -1

    def rotation_index(nums,left,right):
        if nums[left] < nums[right]:
            return 0
        while left<=right:
            mid = (left+right)//2
            if nums[mid]>nums[mid+1]:
                return mid+1
            else:
                if nums[mid]<nums[left]:
                    right=mid-1
                else:
                    left=mid+1
        
    def binary_search(left,right):
        while left<=right:
            pivot = (left+right)//2
            if nums[pivot] == target:
                return pivot
            else:
                if nums[pivot] > target:
                    right =pivot-1
                else:
                    left =pivot+1
                    
        return -1

    left = 0
    right = len(nums)-1
    rotation_index = rotation_index(nums,left,right)

    if nums[rotation_index] == target:
        return rotation_index
    
    if rotation_index==0:
        return binary_search(0,len(nums)-1)
    if target<nums[0]:
        return binary_search(rotation_index,len(nums)-1)
    else:
        return binary_search(0,rotation_index)

nums = [4,5,6,7,0,1,2]
target = 0

def test_search():
    assert search([4,5,1,2,3],1) ==2
    assert search([1,3],3)
    assert search([4,5,6,7,0,1,2],3)==-1
    assert search([4,5,6,7,0,1,2],0)==4

print(search(nums,target))