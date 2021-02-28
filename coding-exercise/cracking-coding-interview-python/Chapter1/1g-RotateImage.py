def rotate_image(matrix):
    n = len(matrix)

    for i in range(n):
        for j in range(1,n):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp

    for i in range(n):
        for j in range(n//2):
            temp = matrix[i][j]
            matrix[i][j] = matrix[i][n-j-1]
            matrix[i][n-j-1] = temp
    return matrix
    
lst =[
  [1,2,3],
  [4,5,6],
  [7,8,9]
]

lst1 = [
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
]

# step1 :
# [
# [1, 4, 7], 
# [2, 5, 8], 
# [3, 6, 9]
# ]

# step2:
# [
#  [7,4,1],
#  [8,5,2],
#  [9,6,3]
# ]

print(rotate_image(lst1))
