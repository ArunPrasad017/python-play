def floodfill(image, sr, sc, newColor):
    rows, column = len(image), len(image[0])
    color = image[sr][sc]
    if color == newColor:
        return image

    def dfs(r, c):
        if image[r][c] != color:
            return
        image[r][c] = newColor
        if r >= 1:
            dfs(r - 1, c)
        if r + 1 < rows:
            dfs(r + 1, c)
        if c >= 1:
            dfs(r, c - 1)
        if c + 1 < column:
            dfs(r, c + 1)

    dfs(sr, sc)
    return image


image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
sr, sc = 1, 1
color = 2

print(floodfill(image, sr, sc, color))