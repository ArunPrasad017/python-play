# def reverseWords(s):
#     s = s.split()
#     return " ".join(reversed(s))

#using deque and two pointer
from collections import deque
def reverseWords(s):
    if len(s)<1:
        return ""
    left = 0
    right =len(s)-1
    while left<=right and s[left]==' ':
        left+=1
    while left<=right and s[right]==' ':
        right-=1
    dq = deque()
    word = []
    while left<=right:
        if s[left]==' ' and word:
            dq.appendleft(''.join(word))
            word = []
        elif s[left]!=' ':
            word.append(s[left])
        left+=1
    dq.appendleft(''.join(word))
    return " ".join(dq)

# s = "a good   example"
s = "  hello world!  "
print(reverseWords(s))