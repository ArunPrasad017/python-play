"""
  Duplicate Zeros

    Input: [1,0,2,3,0,4,5,0]
    Output: null
    Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]
"""
def duplicateZeros(arr):
    """
    Do not return anything, modify arr in-place instead.
    """
    count = 0
    i = 0
    while i+1<len(arr):
        if arr[i] == 0:
            arr.insert(i+1,0)
            count+=1
            i+=2
        else:
            i+=1
    while count>0:
        arr.pop()
        count-=1