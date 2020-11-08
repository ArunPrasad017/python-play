def searchMatrix(matrix, target):
    if not matrix:
        return False
    m = len(matrix)
    n = len(matrix[0])
    left,right=0,(m*n)-1
    while left<=right:
        mid = left+(right-left)//2
        mid_val = matrix[mid//n][mid%n]
        if mid_val==target:
            return True
        elif mid_val>target:
            right=mid-1
        else:
            left=mid+1
    return False

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]]
target = 3
print(searchMatrix(matrix,target))

matrix = []
target = 0
print(searchMatrix(matrix,target))

