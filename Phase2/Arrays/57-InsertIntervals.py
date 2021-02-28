def insert(intervals, newInterval):
    if not intervals and not newInterval:
        return []
    if not intervals:
        return [newInterval]
    if not newInterval:
        return [intervals]
    intervals.append(newInterval)
    intervals.sort(key=lambda x:x[0])
    i=1
    while i<len(intervals):
        if intervals[i][0]<=intervals[i-1][1]:
            intervals[i-1][0] = min(intervals[i-1][0], intervals[i][0])
            intervals[i-1][1] = max(intervals[i-1][1], intervals[i][1])
            intervals.pop(i)
        else:
            i+=1
    return intervals

intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]
print(insert(intervals,newInterval))