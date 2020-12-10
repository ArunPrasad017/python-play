"""
Given a list of 24-hour clock time points in "Hour:Minutes" format, 
find the minimum minutes difference between any two time points in the list.

Input: ["23:59","00:00"]
Output: 1
"""


def findMinDifference(timePoints):
    def minute(a):
        return int(a[:2]) * 60 + int(a[-2:])

    timePoints.sort()
    min_time = 24 * 60
    for i in range(0, len(timePoints)):
        j = (i + 1) % len(timePoints)
        val = (minute(timePoints[j]) - minute(timePoints[i])) % 1440
        min_time = min(min_time, val)
    return min_time


lst = ["23:59", "00:00"]
print(findMinDifference(lst))
