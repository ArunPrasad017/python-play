"""
Given an integer array arr, count how many elements 
x there are, such that x + 1 is also in arr.

If there're duplicates in arr, count them seperately.

Input: arr = [1,2,3]
Output: 2
Explanation: 1 and 2 are counted cause 2 and 3 are in arr.
"""


def countElements(arr):
    dict1 = {}
    count = 0
    for i in range(len(arr)):
        if arr[i] not in dict1:
            dict1[arr[i]] = 1
        else:
            dict1[arr[i]] += 1

    for k, v in dict1.items():
        if k + 1 in dict1.keys():
            count += dict1[k]
    return count


arr = [1, 1, 3, 3, 5, 5, 7, 7]
print(countElements(arr))
