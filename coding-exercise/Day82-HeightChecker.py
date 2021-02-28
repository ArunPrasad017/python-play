"""
1051. Height Checker

Input: heights = [1,1,4,2,1,3]
Output: 3
Explanation: 
Current array : [1,1,4,2,1,3]
Target array  : [1,1,1,2,3,4]
On index 2 (0-based) we have 4 vs 1 so we have to move this student.
On index 4 (0-based) we have 1 vs 3 so we have to move this student.
On index 5 (0-based) we have 3 vs 4 so we have to move this student.

"""

def heightChecker(arr):
    newArr = sorted(arr)
    # alternate code 
    # cnt = 0
    # for i,j in zip(arr, newArr):
    #     if i!=j:
    #         cnt+=1
    # return cnt
    
    #one liner
    return sum(1 for i,j in zip(arr, newArr) if i!=j)