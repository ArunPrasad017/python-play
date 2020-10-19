def canAttendMeetings(intervals):
    if not intervals:
        return True
    intervals.sort(key=lambda x:x[0])
    i=1
    while i<len(intervals):
        if intervals[i][0]<intervals[i-1][1]:
            return False
        i+=1
    return True

lst = [[0,30],[5,10],[15,20]]
print(canAttendMeetings(lst))
lst = [[13,15],[1,13]]
print(canAttendMeetings(lst))