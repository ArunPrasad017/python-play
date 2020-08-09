"""
442. Find All Duplicates in an Array

Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?

Solution runtime - O(nlogn) 
    - sort does o(n) or in log(n) time
    - 
"""
def findDuplicates(self, nums: List[int]) -> List[int]:
    lst2 = []
    nums.sort()
    i = 0
    while i<len(nums)-1:
        if nums[i] == nums[i+1]:
            lst2.append(nums[i])
            i+=2
        else:
            i+=1
    return lst2