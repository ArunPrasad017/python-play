"""
1089 - Duplicate Zeros

Given a fixed length array arr of integers, duplicate each occurrence of zero, shifting the remaining elements to the right.
Note that elements beyond the length of the original array are not written.
Do the above modifications to the input array in place, do not return anything from your function.

Example 1:
Input: [1,0,2,3,0,4,5,0]
Output: null
Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]
"""

def duplicateZeros(arr):
    """
    Do not return anything, modify arr in-place instead.
    """
    n = len(arr)
    i = 0
    count = 0
    while i<len(arr):
        if arr[i]==0:
            arr.insert(i+1,0)
            i+=2
            count+=1
        else:
            i+=1
    while count:
        arr.pop()
        count-=1
    

lst = [1,0,2,3,0,4,5,0]
duplicateZeros(lst)
print(lst)