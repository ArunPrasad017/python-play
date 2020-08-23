from collections import deque
def reverseWords(s):
    q,word = deque(),[]
    left, right = 0, len(s)-1
    while left<right and s[left]==" ":
        left+=1
    while left<right and s[right]== " ":
        right-=1
    while left<=right:
        if s[left]!=' ':
            word.append(s[left])
        elif word:
            q.appendleft(''.join(word))
            word = []
        left+=1
    q.appendleft(''.join(word))
    return ' '.join(q)

s= "a good   example"
print(reverseWords(s))