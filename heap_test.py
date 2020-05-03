def min_heapify(array, i):
    left = 2 * i + 1
    right = 2 * i + 2
    length = len(array) - 1
    smallest = i
    if left <= length and array[i] > array[left]:
        smallest = left
    if right <= length and array[smallest] > array[right]:
        smallest = right
    if smallest != i:
        array[i], array[smallest] = array[smallest], array[i]
        min_heapify(array, smallest)

def ()

def build_min_heap(array):
    for i in reversed(range(len(array)//2)):
        min_heapify(array, i)
    return array

array = [5,4,3,2,1]
print(build_min_heap(array))


import heapq as hq

def minMeetingRooms(intervals):
    intervals.sort(key=lambda x:x[0]) # sorting listoflists using the first val
    mhp = [] # heap initialized
    hq.heappush(mhp, intervals[0][1])
    for i in intervals[1:]:
        if mhp[0]<=i[0]:
            hq.heappop(mhp)
        hq.heappush(mhp,i[1])
    return len(mhp)

lst = [[0, 30],[5, 10],[15, 20]]

print(minMeetingRooms(lst))