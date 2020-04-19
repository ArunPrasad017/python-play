import heapq as hq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        #corner case checks
        if intervals==[]:
            return 0
        # sorting based on start time
        sorted_intervals = sorted(intervals, key = lambda x:x[0])
        h = [] # empty heap declaration
        
        #adding the first instance for starting a room allocation
        h.append(sorted_intervals[0][1])
        
        for i in sorted_intervals[1:]:
            if h[0]<=i[0]:
                hq.heappop(h)
            hq.heappush(h,i[1])
        return len(h)

# testcases
# [[2,15],[36,45],[9,29],[16,23],[4,9]]
# []
