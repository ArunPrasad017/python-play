import heapq
from collections import defaultdict

def kClosest(points, K):
     temp_res = defaultdict(int)
     if not points:
         return temp_res
     for pt in points:
         res =abs(((pt[0]-0)**2 + (pt[1]-0)**2)**0.5)
         pts = tuple(pt)
         temp_res[pts] = res
     return heapq.nsmallest(K,temp_res,key=temp_res.get)