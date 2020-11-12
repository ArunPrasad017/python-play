def searchMatrix(matrix, target):
    # Binary search type 2
    if not matrix:
        return False
    m,n = len(matrix),len(matrix[0])
    left,right=0,(m*n)-1
    while left<=right:
        mid = left+(right-left)//2
        mid_val = matrix[mid//n][mid%n]
        if mid_val == target:
            return True
        elif mid_val>target:
            right=mid-1
        else:
            left= mid+1
    return False


matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]]
n=100
print(searchMatrix(matrix,n))