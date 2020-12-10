def verify(preorder):
    stack = []
    low = -1 << 31
    for n in preorder:
        if n < low:
            return False
        while stack and n > stack[-1]:
            low = stack.pop()
        stack.append(n)
    return True


preorder_lst1 = [5, 2, 1, 3, 6]
preorder_lst2 = [5, 2, 4, 1, 6]

print(verify(preorder_lst1))
print(verify(preorder_lst2))
