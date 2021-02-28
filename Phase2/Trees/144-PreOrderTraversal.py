# class tree:
#     def __init__(self,val):
#         self.val = val
#         self.left = None
#         self.right = None
# iterative method
def preOrder(root):
    if root is None:
        return None
    stack = [root]
    res = []
    while stack:
        node = stack.pop()
        res.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.right)
    return res
