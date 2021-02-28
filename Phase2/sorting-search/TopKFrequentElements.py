from collections import Counter
import heapq


def topKFrequent(nums, k):
    # method 1 - o(n) space
    if len(nums) == k:
        return nums
    if not nums:
        return []
    cntr = Counter(nums)
    return heapq.nlargest(k, cntr, key=cntr.get)
