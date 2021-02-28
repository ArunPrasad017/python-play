def canAttendMeetings(intervals):
    if not intervals:
        return True
    intervals.sort(key=lambda x:x[0])
    return all(
        intervals[i][0] >= intervals[i - 1][1]
        for i in range(1, len(intervals))
    )

lst = [[0,30],[5,10],[15,20]]
print(canAttendMeetings(lst))
lst = [[13,15],[1,13]]
print(canAttendMeetings(lst))