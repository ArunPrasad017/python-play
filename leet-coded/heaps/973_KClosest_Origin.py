import heapq as hq
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        # edge case
        if len(points)<K:
            return points
        h = []
        for x,y in points:
            hq.heappush(h, [-(y**2+x**2),[x,y]])
            if len(h)>K:
                hq.heappop(h)
        return [x[1] for x in h]

# testcases
# [[3,3],[5,-1],[-2,4]], K =2
#  points = [[1,3],[-2,2]], K = 1