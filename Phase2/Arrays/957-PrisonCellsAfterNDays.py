
def prisonAfterNDays(cells, N):
    def cell_generator(cells):
        res =[]
        if not cells:
            return res
        res.append(0)
        for i in range(1,len(cells)-1):
            if cells[i-1]==cells[i+1]:
                res.append(1)
            else:
                res.append(0)
        res.append(0)
        return res
    seen = set()
    cycle,k = False,0
    for i in range(N):
        next_day = cell_generator(cells)
        if tuple(next_day) in seen:
            cycle =True
            break
        seen.add(tuple(next_day))
        cells = next_day
        k+=1
    if not cycle:
        return cells
    return prisonAfterNDays(cells,N%k)

cells = [0,1,0,1,1,0,0,1]
N = 7
print(prisonAfterNDays(cells,N))

cells = [1,0,0,1,0,0,1,0]
N = 1000000000
print(prisonAfterNDays(cells,N))