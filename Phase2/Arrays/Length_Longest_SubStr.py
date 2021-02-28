def lengthOfLongestSubstring(s):
    if not s:
        return 0
    p1,p2 = 0,0
    max_ptr,i=float('-inf'),0
    distinct={}
    while p2<len(s):
        if s[p2] in distinct:
            max_ptr=max(max_ptr,p2-p1)
            p1=max(p1,distinct[s[p2]]+1)
        distinct[s[p2]]=p2
        p2+=1
    max_ptr=max(max_ptr,p2-p1)
    return max_ptr

s = "pwwkew"
print(lengthOfLongestSubstring(s))