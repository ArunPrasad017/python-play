def orangesRotting(grid):
    if len(grid) == 0:
        return -1
    rotten_set = set()
    fresh_set = set()
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                fresh_set.add(str(i) + str(j))
            elif grid[i][j] == 2:
                rotten_set.add(str(i) + str(j))
    mins = 0
    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    while len(fresh_set) > 0:
        infected_set = set()
        for s in rotten_set:
            i = int(s[0])
            j = int(s[1])
            for d in directions:
                next_i = i + d[0]
                next_j = j + d[1]
                val = str(next_i) + str(next_j)
                if val in fresh_set:
                    fresh_set.remove(val)
                    infected_set.add(val)
        if len(infected_set) == 0:
            return -1
        rotten_set = infected_set
        mins += 1
    return mins


grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
print(orangesRotting(grid))
