def compress(s):
    idx, count = 0, 1
    res = [0] * len(s)
    if not s:
        return idx
    for i in range(1, len(s) + 1):
        if i < len(s) and s[i - 1] == s[i]:
            count += 1
        else:
            res[idx] = s[i - 1]
            idx += 1
            for c in str(count):
                res[idx] = c
                idx += 1
            count = 1
    return idx


s = "aabbccc"
print(compress(s))
