def CountAndSay(n):
    s = "1"
    while n > 1:
        new_str = ""
        i = 0
        while i < len(s):
            count = 1
            while i + 1 < len(s) and s[i] == s[i + 1]:
                count += 1
                i += 1
            new_str += str(count) + s[i]
            i += 1
        s = new_str
        n -= 1
    return s


print(CountAndSay(6))
