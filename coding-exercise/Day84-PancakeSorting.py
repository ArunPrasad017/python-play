"""
Given an array of integers A, We need to sort the array performing a series of pancake flips.

In one pancake flip we do the following steps:

Choose an integer k where 0 <= k < A.length.
Reverse the sub-array A[0...k].
For example, if A = [3,2,1,4] and we performed a pancake flip choosing k = 2, we reverse the sub-array [3,2,1], so A = [1,2,3,4] after the pancake flip at k = 2.

Return an array of the k-values of the pancake flips that should be performed in order to sort A. Any valid answer that sorts the array within 10 * A.length flips will be judged as correct.

Input: A = [3,2,4,1]
Output: [4,2,4,3]
Explanation: 
We perform 4 pancake flips, with k values 4, 2, 4, and 3.
Starting state: A = [3, 2, 4, 1]
After 1st flip (k = 4): A = [1, 4, 2, 3]
After 2nd flip (k = 2): A = [4, 1, 2, 3]
After 3rd flip (k = 4): A = [3, 2, 1, 4]
After 4th flip (k = 3): A = [1, 2, 3, 4], which is sorted.
Notice that we return an array of the chosen k values of the pancake flips.

"""

def flip(arr, index):
    for i in range(index//2+1):
        temp = arr[i]
        arr[i] = arr[index-i]
        arr[index-i] = temp
    
def pancakeSort(arr):
    if not arr:
        return []
    res = []
    for i in range(len(arr)-1, 0,-1):
        for j in range(1,i+1):
            if arr[j] == i+1:
                flip(arr,j)
                res.append(j+1)
                break
        flip(arr,i)
        res.append(i+1)
    return res

A = [3, 2, 4, 1]
print(pancakeSort(A))
print(A)