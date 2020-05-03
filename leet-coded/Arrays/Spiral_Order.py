def run_spiral(lst,m,n,final_lst):
    top = 0
    bottom = m-1
    left = 0
    right = n-1
    direction =0
    
    while (top<=bottom) and (left<=right):
        if direction ==0:
            for i in range(left,right+1):
                final_lst.append(lst[top][i])
            top+=1
            direction+=1
        elif direction==1:
            for i in range(top,bottom+1):
                final_lst.append(lst[i][right])
            right-=1
            direction+=1
        elif direction==2:
            for i in range(right,left-1,-1):
                final_lst.append(lst[bottom][i])
            bottom-=1
            direction+=1
        elif direction==3:
            for i in range(bottom,top-1,-1):
                final_lst.append(lst[i][left])
            left+=1
            direction=0
    return final_lst

final_lst = []
# matrix = [[1,2,3],[4,5,6],[7,8,9]]
matrix = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
m = len(matrix)
n = len(matrix[0])
print(run_spiral(matrix,m,n,final_lst))