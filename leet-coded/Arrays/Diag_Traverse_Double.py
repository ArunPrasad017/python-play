def diagonal_order(matrix):
    if not matrix or not matrix[0]:
        return []
    # dimensions of matrix
    n, m = len(matrix), len(matrix[0])

    # indices that help progress through the matrix
    r, c = 0, 0
    # direction to indicate the upward or downward slope
    direction = 1

    result = []

    while r < n and c < m:
        result.append(matrix[r][c])

        new_row = r + (-1 if direction == 1 else 1)
        new_col = c + (1 if direction == 1 else -1)

        # Checking bound or not for next element of matrices
        if new_row < 0 or new_row == n or new_col < 0 or new_col == m:
            if direction:
                r += c == m - 1
                c += c < m - 1
            else:
                c += r == n - 1
                r += r < n - 1
            direction = 1 - direction
        else:
            r = new_row
            c = new_col

    return result


lst1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(diagonal_order(lst1))
