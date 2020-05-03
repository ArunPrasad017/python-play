"""
minimum cost of sticks program - we utilize the greedy algorithm 
and the min heap (using heapq)
"""

import heapq as hq
def connectSticks(sticks):
    hq.heapify(sticks)
    cost = 0

    while len(sticks)>1:
        sum_q = hq.heappop(sticks)+hq.heappop(sticks)
        cost+=sum_q
        hq.heappush(sticks,sum_q)
    return cost

# test
sticks = [1,8,3,5]
print(connectSticks(sticks))