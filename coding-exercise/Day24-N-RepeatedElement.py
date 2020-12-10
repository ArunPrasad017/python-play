"""
In a array A of size 2N, there are N+1 unique elements, and exactly one of these elements is repeated N times.

Input: [1,2,3,3]
Output: 3

Input: [5,1,5,2,5,3,5,4]
Output: 5
"""


def repeatedNTimes(A):
    dict1 = {}
    for ele in A:
        if ele not in dict1.keys():
            dict1[ele] = 1
        else:
            dict1[ele] += 1
    for k, v in dict1.items():
        if v == (len(A) / 2):
            return k
    return None


lst = [5, 1, 5, 2, 5, 3, 5, 4]
print(repeatedNTimes(lst))
