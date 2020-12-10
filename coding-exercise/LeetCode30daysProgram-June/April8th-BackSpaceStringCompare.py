def backspaceCompare(S, T):
    def stackCreator(string):
        stack = []
        for i, c in enumerate(string):
            if c != "#":
                stack.append(c)
            elif stack:
                stack.pop()
        return stack

    return stackCreator(S) == stackCreator(T)


s1 = "y#fo##f"
s2 = "y#f#o##f"
print(backspaceCompare(s1, s2))
