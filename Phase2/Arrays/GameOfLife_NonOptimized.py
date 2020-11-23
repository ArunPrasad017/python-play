import copy
def gameOfLife(grid):
    """
    Do not return anything, modify board in-place instead.
    """
    def count_neighbors(temp_board,x,y,rows,cols):
        total_cnt = 0
        for i in range(-1,2):
            for j in range(-1,2):
                if ((x + i < rows and x + i >= 0) and \
                    (y + j < cols and y + j >= 0)) and (temp_board[x + i][y + j]) == 1:
                    total_cnt+=1
            total_cnt-=temp_board[x][y]
            return total_cnt
        
    temp_board = copy.deepcopy(grid)
    rows,cols = len(grid), len(grid[0])
    for i in range(rows):
        for j in range(cols):
            curr_state = temp_board[i][j]
            neighbors = count_neighbors(temp_board,i,j,rows,cols)
            if curr_state==0 and neighbors==3:
                grid[i][j]=1
            # ideal for live cells
            elif curr_state == 1 and neighbors in [2, 3]:
                grid[i][j]=1
            # death from stravation or overcrowding for any cell considered as living
            elif curr_state==1 and (neighbors>3 or neighbors<2):
                grid[i][j]=0
    return grid
lst = [
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]

print(gameOfLife(lst))