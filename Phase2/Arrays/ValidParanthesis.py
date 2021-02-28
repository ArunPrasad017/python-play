def isValid(s):
    dict1 = {
        '(':')',
        '{':'}',
        '[':']'
    }
    stack=[]
    for c in s:
        if c in dict1:
            stack.append(c)
        elif c in dict1.values():
            if not stack:
                return False
            if dict1[stack.pop()]!=c:
                return False
    return len(stack)==0

s = "()[]{}"
print(isValid(s))
s = "()[]]"
print(isValid(s))
s = "({{{{}}}}}})"
print(isValid(s))
s = "(]"
print(isValid(s))