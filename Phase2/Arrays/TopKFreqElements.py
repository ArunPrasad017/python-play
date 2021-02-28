from collections import Counter
import heapq
def topKFrequentElements(lst,k):
    cntr = Counter(lst)
    return heapq.nlargest(k,cntr,key=cntr.get)

lst =["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
k = 4
print(topKFrequentElements(lst,k))