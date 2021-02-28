"""
905. Sort Array By Parity

Given an array A of non-negative integers, return an array consisting of all the even elements of A, 
followed by all the odd elements of A.
You may return any answer array that satisfies this condition

Input: [3,1,2,4]
Output: [2,4,3,1]
The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
"""

def sortArrayParity(lst):
    if lst is None:
        return lst
    i, j  = 0, len(lst)-1
    while i<j:
        if lst[i]%2 > lst[j]%2:
            lst[i], lst[j] = lst[j], lst[i]
        if lst[i]%2==0:
            i+=1
        if lst[j]%2==1:
            j-=1
    return lst

lst = [3,1,2,4]
print(sortArrayParity(lst))