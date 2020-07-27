def dfs(grid,i,j):
    if i==0 or i>=len(grid) or j==0 or j>=len(grid[i]) or grid[i][j]==0:
        return 0
    grid[i][j] = 0
    dfs(grid,i+1,j)
    dfs(grid,i-1,j)
    dfs(grid,i,j+1)
    dfs(grid,i,j-1)
    return 1

def numDistinctIslands(grid):
    if not grid or len(grid)==0:
        return 0
    numislands = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (grid[i][j] == 1):
                numislands+=dfs(grid,i,j)
    return numislands

grid = [[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]
print(grid[0][0])
print('---------------------')
print(numDistinctIslands(grid))