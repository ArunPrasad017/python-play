from collections import Counter
import heapq
def reOrganizeString(S):
    count = dict(Counter(S))
    pq = [(-v,k) for k,v in count.items()]
    heapq.heapify(pq)

    if any(-val >((len(S)+1)/2) for val,x in pq):
        return ""
    
    res = []
    while len(pq)>1:
        current_val, current_string = heapq.heappop(pq)
        next_val, next_string = heapq.heappop(pq)

        res.extend([current_string,next_string])
        if current_val+1:
            heapq.heappush(pq,(current_val+1,current_string))
        if next_val+1:
            heapq.heappush(pq,(next_val+1,next_string))
    return "".join(res) + (pq[0][1] if pq else '')



String = "aab"
print(reOrganizeString(String))