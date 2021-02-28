def strStr(haystack, needle):
    if len(haystack)<len(needle):
        return -1
    if haystack == needle:
        return 0
    n=len(needle)
    for i in range(len(haystack)-n):
        if haystack[i:i+n]==needle:
            return i
    return -1

haystack = "hello"
needle = "ll"
print(strStr(haystack,needle))