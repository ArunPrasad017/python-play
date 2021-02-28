"""
Number of Distinct Islands based on input strings
we use a set and the DFS algo to help determine solution

Directional logic
"Start" - starting position(s)
"left"  - seek towards left direction(L)
"right" - seek towards right direction(R)
"down"  - seek towards downward direction(D)
"up"    - seek towards upward direction(U)
"""


def findPath(grid, m, n, i, j, direction):
    if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] == 0:
        return
    grid[i][j] = 0
    direction.append("S")

    direction.append("L")
    left = findPath(grid, m, n, i, j - 1, direction)
    direction.append("R")
    right = findPath(grid, m, n, i, j + 1, direction)
    direction.append("U")
    upward = findPath(grid, m, n, i - 1, j, direction)
    direction.append("D")
    downward = findPath(grid, m, n, i + 1, j, direction)


def numDistinctIslands(grid):
    if len(grid) == 0 or grid == None:
        return None
    Islands_set = set()
    m = len(grid)
    n = len(grid[0])

    for i in range(0, m):
        for j in range(0, n):
            if grid[i][j] == 1:
                direction = []
                findPath(grid, m, n, i, j, direction)
                Islands_set.add("".join(direction))
    return Islands_set


x = [[1, 1, 0, 1, 1], [1, 0, 0, 0, 0], [0, 0, 0, 0, 1], [1, 1, 0, 1, 1]]
print(numDistinctIslands(x))
