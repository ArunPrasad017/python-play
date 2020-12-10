def toLowerCase(s):
    str1 = ""
    for c in s:
        if ord(c) in range(65, 91):
            cr = chr(ord(c) + 32)
            str1 += cr
        else:
            str1 += c
    return str1


s = "Hello"
print(toLowerCase(s))
