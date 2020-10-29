def lengthOfLongestSubstring(s):
    if not s:
        return 0
    l,r =0,0
    seen = {}
    maxRes =0
    for r in range(len(s)):
        if s[r] not in seen:
            maxRes=max(maxRes,(r-l)+1)
        else:
            if seen[s[r]]<l:
                maxRes=max(maxRes,(r-l)+1)
            else:
                l = seen[s[r]]+1
                seen[s[r]] = r
    return maxRes