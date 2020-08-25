"""
283. Move Zeroes

Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:
Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
"""

def moveZeroes(lst):
    slow,fast = 0,0
    while fast<len(lst):
        if lst[fast]!=0:
            lst[slow], lst[fast] = lst[fast], lst[slow]
        if lst[slow]!=0:
            slow+=1
        fast+=1
    return lst

print(moveZeroes([1,0,0,4,12]))