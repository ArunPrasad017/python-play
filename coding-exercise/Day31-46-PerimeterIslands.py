def islandPerimeter(grid):
    edges = 0; side =0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]==1:
                side+=1
                if i>0 and grid[i-1][j]==1 :
                    edges+=1
                if j>0 and grid[i][j-1]==1:
                    edges+=1
    return ((4*side) - (2*edges))
    


grid = [[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

grid2 = [
[0,1,0,0],
[0,1,0,0],
[0,1,0,0],
[0,1,0,0]
]
print(islandPerimeter(grid2))