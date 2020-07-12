"""
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:
"""
from itertools import combinations

#recursive
def subset_recursive(nums,idx, res):
    if idx == len(nums)-1:
        res.append([nums[idx]])
    else:
        subset_recursive(nums,idx+1,res)
        n = len(res)
        for i in range(n):
            r=res[i]
            r=r[:]
            r.insert(0,nums[idx])
            res.append(r)

def subsets(nums):
    # easy solution - using itertools
    # res = []
    # for i in range(len(nums)+1):
    #     val = [list(x) for x in combinations(nums,i)]
    #     res+=val
    # return res

    if len(nums)==0:
        return []
    res = [[]]
    subset_recursive(nums,0,res)
    return res


nums = [1,2,3]
print(subsets(nums))