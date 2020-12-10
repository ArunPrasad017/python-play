"""
31. Next Permutation
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).
The replacement must be in-place and use only constant extra memory.
Ex:
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1

-- [6,2,1,5,4,3,0]
"""


def nextPermutation(nums):
    def swap(nums, a, b):
        nums[a], nums[b] = nums[b], nums[a]

    def reverse(nums, i):
        nums[i:] = nums[i:][::-1]

    k = len(nums) - 2
    while k >= 0 and nums[k] >= nums[k + 1]:
        k -= 1
    if k >= 0:
        j = len(nums) - 1
        while j >= 0 and nums[j] <= nums[k]:
            j -= 1
        swap(nums, k, j)
    reverse(nums, k + 1)

    return nums


nums = [1, 5, 1]
print(nextPermutation(nums))
