def longestCommonPrefix(strs):
    if len(strs) > 0:
        strs = sorted(strs)
    else:
        return ""
    prefix = strs[0]
    for i in range(1, len(strs)):
        str1 = ""
        for j in range(len(prefix)):
            if strs[i][j] == prefix[j]:
                str1 += prefix[j]
            else:
                break
        prefix = str1
    return prefix


s = ["flower", "flow", "flight"]
s2 = ["dog", "racecar", "car"]
print(longestCommonPrefix(s2))
