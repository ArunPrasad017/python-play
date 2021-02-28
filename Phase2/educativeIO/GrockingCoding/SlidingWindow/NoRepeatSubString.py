def max_no_repeat_sub_length(s):
    if not s:
        return 0
    max_cnt,start = 0,0
    d={}
    for end in range(len(s)):
        end_str = s[end]
        if end_str in d:
            start = max(start,d[end_str]+1)
        d[end_str]=end
        max_cnt = max(max_cnt,end-start+1)
    return max_cnt

String="aab"
print(max_no_repeat_sub_length(String))