from collections import defaultdict
from itertools import combinations


def containsCloseNums(nums, k):
    if not nums or k == 0:
        return False
    if len(nums) == 1:
        return False
    dict1 = defaultdict(list)
    for i, n in enumerate(nums):
        dict1[n].append(i)
    for key, val in dict1.items():
        if len(val) > 1:
            temp = [abs(a - b) for a, b in combinations(val, 2)]
            return any(i <= k for i in temp)
    return False
