"""
977. Squares of a Sorted Array

Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, 
also in sorted non-decreasing order.

Example 1:

Input: [-4,-1,0,3,10]
Output: [0,1,9,16,100]
"""
def sortedSquares(A):
    ###################################
    # one liner
    # return sorted([x**2 for x in A])
    ###################################
    # trying quick sort method
    def partition(lst, start, end):
        pivot = lst[start]
        low,high = start+1, end
        while True:
            while low<=high and lst[high]>pivot:
                high-=1
            while low<=high and lst[low]<=pivot:
                low+=1
            if low<=high:
                lst[low], lst[high] = lst[high], lst[low]
            else:
                break
        lst[start], lst[high] = lst[high], lst[start]
        return high

    def quickSort(lst, start, end):
        if start>=end:
            return
        p = partition(lst,start,end)
        quickSort(lst, start, p-1)
        quickSort(lst, p+1, end)
        
    for i,num in enumerate(A):
        A[i] = num**2
    quickSort(A,0,len(A)-1)
    return A

A = [-7,-3,2,3,11]
# [16,1,0,9,10]
print(sortedSquares(A))