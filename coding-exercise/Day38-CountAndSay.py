def countAndSay(n):
    s = "1"
    while n - 1:
        ns = ""
        i = 0
        while i < len(s):
            count = 1
            while i + 1 < len(s) and s[i] == s[i + 1]:
                count += 1
                i += 1
            ns += str(count) + s[i]
            i += 1
        n -= 1
        s = ns
    return s


print(countAndSay(4))
