"""
941. Valid Mountain Array

Given an array A of integers, return true if and only if it is a valid mountain array.

Recall that A is a mountain array if and only if:

A.length >= 3
There exists some i with 0 < i < A.length - 1 such that:
A[0] < A[1] < ... A[i-1] < A[i]
A[i] > A[i+1] > ... > A[A.length - 1]

Example 3:

Input: [0,3,2,1]
Output: true

"""


def validMountainArray(A):
    if A[0] > A[1]:
        return False
    i = 0
    n = len(A)
    while i + 1 < n and A[i] < A[i + 1]:
        i += 1
    if i in [0, n - 1]:
        return False
    while i + 1 < n and A[i] > A[i + 1]:
        i += 1

    return i == n - 1


lst = [0, 1, 2, 4, 2, 1]
print(validMountainArray(lst))
