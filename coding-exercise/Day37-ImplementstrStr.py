def strStr(haystack, needle):
    if needle == "":
        return -1
    l = len(needle)
    for i, c in enumerate(haystack):
        if haystack[i : i + l] == needle:
            return i
    return -1


haystack = "aaaaa"
needle = "bba"
print(strStr(haystack, needle))
