def romanToInt(s: str) -> int:
    if not s:
        return 0
    r_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    res = r_dict[s[len(s) - 1]]
    for i in range(len(s) - 2, -1, -1):
        if r_dict[s[i]] < r_dict[s[i + 1]]:
            res -= r_dict[s[i]]
        else:
            res += r_dict[s[i]]
    return res


print(romanToInt("III"))
print(romanToInt("XIX"))
