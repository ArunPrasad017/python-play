
# brute force
# def prisonCell(cells,N):
#     for i in range(N):
#         cells = bruteforce(cells)
#     return cells

def prisonCellSet(cells,N):
    seen = set()
    length = 0
    cycle = False
    for i in range(N):
        next = cellAssigner(cells)
        if tuple(next) in seen:
            cycle = True
            break
        seen.add(tuple(cells))
        length+=1
        cells = next
    if not cycle:
        return cells
    return prisonCellSet(cells, N%length)

def cellAssigner(cells):
    next_day = []
    # note that first and last cells in prison row don't have 
    # adjacent neighbours and hence can be vacant
    next_day.append(0)
    for i in range(1,len(cells)-1):
        if cells[i-1] == cells[i+1]:
            next_day.append(1)
        else:
            next_day.append(0)
    next_day.append(0)
    return next_day


cells = [1,0,0,1,0,0,1,0]
N=1000000000
print(prisonCellSet(cells, N))