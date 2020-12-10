# class tree:
#     def __init__(self,val):
#         self.val = val
#         self.left = None
#         self.right = None
# iterative method
# a) inverse the preorder
# b) iteratively calculate postOrder

# a)
def postOrder(root):
    stack, res = [root], []
    while stack:
        node = stack.pop()
        res.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return res[::-1]


def postOrder2(root):
    if root is None:
        return None
    temp, res = [root], []  # two stacks
    while temp:
        node = temp.pop()
        res.insert(0, node.val)
        if node.left:
            temp.append(node.left)
        if node.right:
            temp.append(node.right)
    return res
