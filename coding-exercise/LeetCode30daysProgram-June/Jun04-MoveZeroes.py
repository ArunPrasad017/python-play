"""
    MoveZeroes to the end
"""

def moveZeros(nums):
    if len(nums)==1:
        return nums
    slow = 0
    for fast in range(len(nums)):
        if nums[fast]!=0:
            nums[fast], nums[slow]= nums[slow], nums[fast]

        if nums[slow]!=0:
            slow+=1

    return nums

nums= [0,0,1,3,12]
print(moveZeros(nums))