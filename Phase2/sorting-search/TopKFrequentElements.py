from collections import Counter
def topKFrequent(nums, k) -> List[int]:
        # method 1
        # o(n) space
        # if len(nums) ==k:
        #     return nums
        # res = []
        # if not nums:
        #     return res
        # cntr = Counter(nums)
        # return heapq.nlargest(k,cntr,key=cntr.get)
        # method 2