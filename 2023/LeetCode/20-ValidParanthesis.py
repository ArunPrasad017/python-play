def isValid(s):
    if (len(s)) % 2 != 0:
        return False

    d = {"{": "}", "(": ")", "[": "]"}
    stack = []
    for i in s:
        if i in d:
            stack.append(i)
        elif i in d.values():
            if not stack:
                return False
            elif i != d[stack.pop()]:
                return False
    return not stack


s = "()[]{}"
print(isValid(s))