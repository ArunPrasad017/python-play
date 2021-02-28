# method 1 tried with o(1) space and fails for certain conditions
# def length_of_longest_substring(s,k):
#     start,max_cnt = 0,0
#     counter=0
#     for end in range(1,len(s)-1):
#         if s[start]==s[end]:
#             continue
#         else:
#             if counter<=k:
#                 counter+=1
#             else:
#                 counter=0
#                 max_cnt = max(max_cnt, end-start+1)
#                 start=end
#     return max_cnt

def length_of_longest_substring(s,k):
    if not s:
        return 0
    start,max_cnt,max_repeat_cntr =0,0,0
    d={}
    for end in range(len(s)):
        end_str = s[end]
        if end_str not in d:
            d[end_str]=0
        d[end_str]+=1
        max_repeat_cntr=max(max_repeat_cntr,d[end_str])
        if(end-start+1 -max_repeat_cntr)>k:
            start_str = s[start]
            d[start_str]-=1
            start+=1
        max_cnt = max(max_cnt, end-start+1)
    return max_cnt

String="abbcb"
k=1
print(length_of_longest_substring(String,k))

s="aabccbb"
k=2
print(length_of_longest_substring(s,k))