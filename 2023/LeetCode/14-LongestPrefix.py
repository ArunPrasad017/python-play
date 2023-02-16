def longestCommonPrefix(strs):
    strs.sort()
    prefix = strs[0]
    for i in range(1, len(strs)):
        temp = ""
        for j, k in zip(prefix, strs[i]):
            if j == k:
                temp += str(j)
            else:
                break
        prefix = temp
    return prefix


strs = ["flower", "flow", "flight"]
print(longestCommonPrefix(strs))