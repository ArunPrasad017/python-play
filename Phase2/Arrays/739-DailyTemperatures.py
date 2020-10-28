def dailyTemperatures(T):
    stack =[]
    res = [0]*len(T)
    for i,n in enumerate(T):
        while stack and T[stack[-1]]<n:
            curr = stack.pop()
            res[curr]=i-curr
        stack.append(i)
    return res

T = [73, 74, 75, 71, 69, 72, 76, 73]
print(dailyTemperatures(T))