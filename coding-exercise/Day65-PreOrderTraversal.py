# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# recursive method
class RecSolution:
    def rec_preOrder(node, lst):
        if node is not None:
            lst.append(node.val)
        if node.left:
            rec_preOrder(node.left, lst)
        if node.right:
            rec_preOrder(node.right, lst)

    def preOrder(root):
        if root is None:
            return None
        res = []
        return rec_predOrder(root, res)


class NonRecSolution:
    def preOrder(root):
        if root is None:
            return None
        res = []
        stack = [
            root,
        ]
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return res
