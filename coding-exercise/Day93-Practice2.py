def count(s):
    w_count, l_count, d_count = 0, 0, 0
    for c in s:
        if c == "W":
            w_count += 1
        elif c == "D":
            d_count += 1
        elif c == "L":
            l_count += 1
    res = ""
    while l_count or d_count or w_count:
        if w_count > 0:
            res += "W"
            w_count -= 1
        if d_count > 0:
            res += "D"
            d_count -= 1
        if l_count > 0:
            res += "L"
            l_count -= 1
    return res


s = "DLWDL"
print(count(s))
