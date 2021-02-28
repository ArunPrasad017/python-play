# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class RecSolution:
    def recurse(node):
        if node is None:
            return []
        return recurse(node.left) + recurse(node.right) + [node.val]
    def postOrder(root):
        if root is None:
            return None
        return recurse(root)

class NonRecSolution(node):
    def postOrder(root):
        if root is None:
            return None
        stack = [root,]
        res = []
        while stack:
            root = stack.pop()
            res.append(root.val)
            if root.left:
                stack.append(root.left)
            if root.right:
                stack.append(root.right)
        return res[::-1]