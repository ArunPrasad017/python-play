"""
Replace Elements with Greatest Element on Right Side

Given an array arr, replace every element in that array with the greatest element among the elements to its right, 
and replace the last element with -1.

After doing so, return the array.

Input: arr = [17,18,5,4,6,1]
Output: [18,6,6,6,1,-1]
"""


def replaceElements(arr):
    for i in range(len(arr)):
        if i == len(arr) - 1:
            arr[i] = -1
            break
        arr[i] = max(arr[i + 1 :])
    return arr


input = [17, 18, 5, 4, 6, 1]
print(replaceElements(input))
