"""
2D array practice program
"""

def rooks_are_safe(matrix):
    m = len(matrix)
    n = len(matrix[0])
    counter_row= counter_col =0
    for i in range(m):
        for j in range(n):
            if matrix[i][j]==1:
                counter_row+=1
            if counter_row>=2:
                return False
        counter_row = 0
    
    for i in range(n):
        for j in range(m):
            if matrix[i][j]==1:
                counter_col+=1
            if counter_col>=2:
                return False
        counter_col=0
    return True


matrix = [[0,1,0,0],
[0,0,1,0],
[0,0,0,0],
[0,0,0,1]
]
print(rooks_are_safe(matrix))