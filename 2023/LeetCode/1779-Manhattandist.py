def nearestValidPoint(x, y, points):
    manhattan_dist, res_idx = float("inf"), -1
    for idx, val in enumerate(points):
        a, b = val
        dist = abs(x - a) + abs(y - b)
        if dist < manhattan_dist and (x == a or y == b):
            manhattan_dist = dist
            res_idx = idx
    return res_idx


x = 3
y = 4
points = [[1, 2], [3, 1], [2, 4], [2, 3], [4, 4]]
print(nearestValidPoint(x, y, points))
