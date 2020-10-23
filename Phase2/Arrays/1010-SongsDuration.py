from collections import defaultdict
def numPairsDivisibleBy60(self, time: List[int]) -> int:
    # two sum method not working
    d = defaultdict(int)
    for t in time:
        d[t%60]+=1
    res = 0
    d1 = d.copy() # this is to force the issue due to error faced at runtime
    for k,v in d1.items(): # if we iterate through same array we are trying to lookup as in elif clause then we will break because it revokes the access
        if k in [0, 30]:
            res+=(v*(v-1))//2
        elif k<30:
            res+=(v*d[60-k])
    return res
        
#         # brute force time limit exceeded
#         count = 0
#         if not time:
#             return count
#         time.sort()
#         for i in range(len(time)):
#             for j in range(i+1,len(time)):
#                 if (time[i]+time[j])%60==0:
#                     count+=1
#         return count