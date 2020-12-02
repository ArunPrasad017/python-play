def spiralOrder(matrix):
    res = []
    if not matrix:
        return res
    left,right= 0,len(matrix[0])-1
    top,bottom= 0,len(matrix)-1
    size= len(matrix)*len(matrix[0])
    while len(res)<size:
        for i in range(left,right+1):
            if len(res)<size:
                res.append(matrix[top][i])
        top+=1
        for j in range(top,bottom+1):
            if len(res)<size:
                res.append(matrix[j][right])
        right-=1
        for i in range(right,left-1,-1):
            if len(res)<size:
                res.append(matrix[bottom][i])
        bottom-=1
        for j in range(bottom,top-1,-1):
            if len(res)<size:
                res.append(matrix[j][left])
        left+=1
    return res

matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print(spiralOrder(matrix))