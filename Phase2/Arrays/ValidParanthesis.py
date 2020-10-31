def isValid(self, s: str) -> bool:
    if not s:
        return True
    d = {
        '{':'}',
        '[':']',
        '(':')'
    }
    stack=[]
    for c in s:
        if c in d.values() and stack:
            if c==d[stack[-1]]:
                stack.pop()
            else:
                return False
        elif c in d:
            stack.append(c)
        else:
            return False
    return not stack