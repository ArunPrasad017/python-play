import heapq as hq
import collections
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        if not words:
            return None
        count = collections.Counter(words)
        h = [(-freq,word) for word,freq in count.items()]
        hq.heapify(h)
        return [hq.heappop(h)[1] for i in range(k)]

# testcases
# Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
# Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
