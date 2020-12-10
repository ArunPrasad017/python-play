def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    stack = []
    dict_balanced = {"(": ")", "[": "]", "{": "}"}

    for char in s:
        is_balanced = False
        if char in dict_balanced.keys():
            stack.append(char)
        elif char in dict_balanced.values():
            if len(stack) == 0:
                return False
            else:
                item = stack[len(stack) - 1]
                try:
                    if dict_balanced[item] == char:
                        is_balanced = True
                except KeyError:
                    is_balanced = False
                if is_balanced:
                    stack = stack[: len(stack) - 1]
    if (len(stack)) == 0:
        return True
    else:
        return False


if __name__ == "__main__":
    s = "(])"
    bal_check = isValid(s)
    print(bal_check)
