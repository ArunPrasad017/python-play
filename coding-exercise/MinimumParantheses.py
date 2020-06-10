def minRemoveToMakeValid(s):
    remove_set = set()
    stack = []
    for i,c in enumerate(s):
        if c not in "()":
            continue
        if c =='(':
            stack.append(i)
        elif not stack:
            remove_set.add(i)
        else:
            stack.pop()
    remove_set = remove_set.union(set(stack))
    string = []
    for i,c in enumerate(s):
        if i not in remove_set:
            string.append(c)
    return "".join(string)

s = "(a(b(((c)d)"
print(minRemoveToMakeValid(s))