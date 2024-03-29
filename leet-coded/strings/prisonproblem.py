def nextday(cells):
    return [int(i > 0 and i < 7 and cells[i - 1] == cells[i + 1]) for i in range(8)]


def afterNdays(cells, N):
    seen = {}
    while N > 0:
        c = tuple(cells)
        if c in seen:
            N %= seen[c] - N
        seen[c] = N

        if N >= 1:
            N -= 1
            cells = nextday(cells)


cells = [0, 1, 0, 1, 1, 0, 0, 1]
N = 7

print(afterNdays(cells, N))
