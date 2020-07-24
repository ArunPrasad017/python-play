"""
Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. 
Find the two elements that appear only once.

Example:
Input:  [1,2,1,3,2,5]
Output: [3,5]
"""

# method1 using o(n) time and o(n) space
def singleNumber(nums):
    hash_set = set()
    for num in nums:
        if num not in hash_set:
            hash_set.add(num)
        else:
            hash_set.remove(num)
    return list(hash_set)

# method2 using o(n) time and o(1) space
def singleNumberLow(nums):
    val = 0
    res = [0,0]
    for num in nums:
        val^=num
    lsb = val&(-val)
    for num in nums:
        if (num&lsb):
            res[0]^=num
        else:
            res[1]^=num
    return res

lst = [1,2,1,3,2,5]
print(singleNumberLow(lst))


