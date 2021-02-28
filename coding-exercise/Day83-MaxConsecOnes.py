"""
"""
def findMaxConsecutiveOnes(nums):
    cnt, max_cnt=0,0
    for num in nums:
        if num == 1:
            cnt+=1
        else:
            max_cnt = max(max_cnt, cnt)
            cnt = 0
    max_cnt = max(max_cnt, cnt)
    return max_cnt