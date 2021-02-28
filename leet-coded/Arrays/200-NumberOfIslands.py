"""
Number of Islands based on input strings
we use a counter to count and use the DFS algo to help determine solution
"""

def findPath(grid,m,n,i,j):
    if i<0 or j<0 or i>=m or j>=n or grid[i][j]=='0':
        return ;
    grid[i][j] = '0'
    left = findPath(grid,m,n,i,j-1)
    right = findPath(grid,m,n,i,j+1)
    upward = findPath(grid,m,n,i-1,j,)
    downward = findPath(grid,m,n,i+1,j)

def numIslands(grid):
    if len(grid) == 0 or grid is None:
        return None
    Islands_count = 0
    m = len(grid)
    n = len(grid[0])
    for i in range(m):
        for j in range(n):
            if grid[i][j]=='1':
                Islands_count+=1
                findPath(grid,m,n,i,j)
    return Islands_count

x = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
print(numIslands(x))