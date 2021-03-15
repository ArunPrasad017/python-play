def lengthOfLongestSubstring(self, s: str) -> int:
    l=0
    d={}
    dist = 0
    for r,c in enumerate(s):
        if c in d:
            l=max(l,d[c])
        dist = max((r-l)+1,dist)
        d[c]=r+1
    return dist