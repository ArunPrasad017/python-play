def find_count_less_equal(matrix,mid,smaller,larger):
    count,n = 0,len(matrix)
    row,col = n-1,0
    while row>=0 and col<n:
        if matrix[row][col]<=mid:
            smaller=max(smaller,matrix[row][col])
            count+=row+1
            col+=1
        else:
            larger=min(matrix[row][col],larger)
            row-=1
    return count,smaller,larger

def kthSmallest(matrix,k):
    if not matrix:
        return 0
    n = len(matrix)
    start,end = matrix[0][0], matrix[n-1][n-1]
    while start<end:
        mid = start+(end-start)//2
        smaller,larger = matrix[0][0], matrix[n-1][n-1]
        count,smaller,larger = find_count_less_equal(matrix,mid,smaller,larger)
        if count==k:
            return smaller
        elif count>k:
            end=smaller
        else:
            start=larger
    return start


matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
]
k = 8
print(kthSmallest(matrix,k))