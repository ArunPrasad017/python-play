import collections
import heapq as hq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # egde case
        if not nums:
            return None
        # creating a counter dictionary with elements frequency
        count = collections.Counter(nums)
        # using n largest heap function
        # note - the heap offers multiple options to get keys and values and using two here for the same.
        return hq.nlargest(k, count.keys(), key=count.get)
