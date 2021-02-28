def perfectCity(departure, destination):
    import math

    (depX, depY) = departure
    (destX, destY) = destination
    distances = []

    for i in [math.floor, math.ceil]:
        x = depX
        y = depY
        distance = 0
        while 1:
            (dx, dy) = (0, 0)
            if x == destX:
                dy = destY - y
            elif y == destY:
                dx = destX - x
            elif x % 1 != 0:
                dx = i(x) - depX
            elif y % 1 != 0:
                dy = i(y) - depY
            elif destX % 1 != 0:
                dy = destY - y
            elif destY % 1 != 0:
                dx = destX - x

            distance += abs(dx + dy)
            x += dx
            y += dy

            if x == destX and y == destY:
                break

        distances.append(distance)

    return min(distances)


departure = [0.4, 1]
destination = [0.9, 3]
print(perfectCity(departure, destination))
