"""
Find the duplicate number:
using 3 methods 
1) brute force using sort
2) set
3) cycle detection algo -tortoise and hare
"""
def findDuplicate(nums):
    # brute force and sort 
    # Time: O(nlogn) and space: o(1)

    nums.sort()
    prev = nums[0]
    for i in range (1,len(nums)):
        if nums[i] == prev:
            return nums[i]
        prev = nums[i]
    return None

def findDuplicate_set(nums):
    # with set and time:o(n) 
    # and space:O(n)
    nums_set=set()
    for i in range(0,len(nums)):
        if nums[i] in nums_set:
            return nums[i]
        nums_set.add(nums[i])


def findDuplicate_cycle(nums):
    # Using floyd's Hare and Tortoise
    t = nums[0]
    h = nums[0]

    while True:
        t=nums[t]
        h=nums[nums[h]]
        if t==h:
            break
    t = nums[0]
    while t!=h:
        t = nums[t]
        h = nums[h]
    return h

print(findDuplicate([1,3,4,2,2]))
print(findDuplicate_set([1,3,4,2,2]))
print(findDuplicate_cycle([1,3,4,2,2]))