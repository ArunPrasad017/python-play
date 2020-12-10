def lengthOfLongestSubstring(s):
    if not s:
        return 0
    max_cnt,l = float('-inf'),0
    seen ={}
    for r,c in enumerate(s):
        if c in seen:
            l = max(l,seen[c])
        max_cnt = max(max_cnt,(r-l)+1)
        seen[c] = r+1
    return max_cnt


s=' '
print(lengthOfLongestSubstring(s))

s='pwwkew'
print(lengthOfLongestSubstring(s))