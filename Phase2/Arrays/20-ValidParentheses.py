class Solution:
    def isValid(self, s: str) -> bool:
        dict1 = {
            '{':'}',
            '[':']',
            '(':')'
        }
        stack = []
        for c in s:
            if c in dict1:
                stack.append(c)
            elif c in dict1.values() and len(stack)>0:
                if dict1[stack[-1]]==c:
                    stack.pop()
                else:
                    return False
            else:
                return False
        return len(stack)==0