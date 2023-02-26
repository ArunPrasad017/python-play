def countOdds(low: int, high: int) -> int:
    res = 0
    if (low & 1) == 0:
        low += 1
    return (high - low) // 2 + 1


print(countOdds(3, 7))
