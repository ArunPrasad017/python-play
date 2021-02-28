"""
54. Spiral Matrix
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
"""

def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
    res=[]
    if not matrix:
        return res
    left = 0
    right = len(matrix[0])-1
    top =0
    bottom=len(matrix)-1
    matrix_size = len(matrix)*len(matrix[0])
    while len(res)<matrix_size:
        for i in range(left,right+1):
            if len(res)<matrix_size:
                res.append(matrix[top][i])
        top+=1
        for j in range(top,bottom+1):
            if len(res)<matrix_size:
                res.append(matrix[j][right])
        right-=1
        for k in range(right, left-1,-1):
            if len(res)<matrix_size:
                res.append(matrix[bottom][k])
        bottom-=1
        for l in range(bottom, top-1, -1):
            if len(res)<matrix_size:
                res.append(matrix[l][left])
        left+=1
    return res
