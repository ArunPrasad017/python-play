def strStr(haystack, needle):
    if needle == haystack:
        return 0
    if needle == "":
        return 0
    for i in range(len(haystack) + 1):
        if haystack[i : (i + len(needle))] == needle:
            return i
    return -1
