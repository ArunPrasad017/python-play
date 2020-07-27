"""
Given a string s of '(' , ')' and lowercase English characters. 

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) 
so that the resulting parentheses string is valid and return any valid string.

Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.

Input: s = "))(("
Output: ""
Explanation: An empty string is also valid.
"""
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
    string = [c for i,c in enumerate(s) if i not in remove_set]
    return "".join(string)

s = "(a(b(((c)d)"
print(minRemoveToMakeValid(s))