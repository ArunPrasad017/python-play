from collections import deque
N = int(input())
d = deque()
for _ in range(N):
    step = input().split(' ')
    if step[0].lower()=='append':
        d.append(step[1])
    elif step[0].lower()=='appendleft':
        d.appendleft(step[1])
    elif step[0].lower()=='pop':
        d.pop()
    elif step[0].lower()=='popleft':
        d.popleft()
print(*d)