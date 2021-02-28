from collections import defaultdict


class Solution:
    def firstUniqChar(self, s: str) -> int:
        cntr = defaultdict(list)
        for i, c in enumerate(s):
            cntr[c].append(i)
        for k, v in cntr.items():
            if len(v) == 1:
                return v[0]
        return -1
