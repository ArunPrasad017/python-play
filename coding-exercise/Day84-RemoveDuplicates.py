"""
  Remove Duplicates from Sorted Array

Example 1:
Given nums = [0,0,1,1,1,2,2,3,3,4],
Your function should return length= 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.
It doesn't matter what values are set beyond the returned length.
"""
def removeDuplicates(nums):
    writePointer = 1
    for readPointer in range(1, len(nums)):
        if nums[readPointer] != nums[readPointer-1]:
            nums[writePointer] = nums[readPointer]
            writePointer+=1
    return nums[:writePointer]

nums = [0,0,1,1,1,2,2,3,3,4]
print(removeDuplicates(nums))
