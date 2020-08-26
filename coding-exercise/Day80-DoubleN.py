"""
Given an array arr of integers, check if there exists two integers N and M such that 
N is the double of M ( i.e. N = 2 * M).

More formally check if there exists two indices i and j such that :

i != j
0 <= i, j < arr.length
arr[i] == 2 * arr[j]

Input: arr = [10,2,5,3]
Output: true
Explanation: N = 10 is the double of M = 5,that is, 10 = 2 * 5.

input [-2,0,10,-19,4,6,-8]
output = False
"""
def checkIfExists(arr):
    if not arr:
        return False
    dict1= {num:i for i, num in enumerate(arr)}
    zeroCount=0
    for num in arr:
        if num*2 in dict1 and num!=0:
            return True
        if num==0:
            zeroCount+=1
    return zeroCount>1

lst = [-2,0,10,-19,4,6,-8]
lst = [0,0]
print(checkIfExists(lst))