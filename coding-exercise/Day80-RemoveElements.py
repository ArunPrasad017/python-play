"""
26. Remove Duplicates from Sorted Array
27. Remove Element

both to be done with no extra space allocations
"""


def removeElement(nums, val):
    k = 0
    for num in nums:
        if num != val:
            nums[k] = num
            k += 1
    return k


nums = [3, 2, 2, 3]
val = 3


def removeDuplicates(nums):
    for i, c in enumerate(nums):
        temp = nums[i]
        for num in nums[i + 1 :]:
            if num > temp:
                break
            if num == temp:
                nums.remove(num)
    return nums


nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
print(removeDuplicates(nums))
