# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class RecSolution:
    def recurse(node, res):
        if node.left:
            recurse(node.left, res)
        if node:
            res.append(node.val)
        if node.right:
            recurse(node.right, res)
        return res

    def inOrder(root):
        if root is None:
            return None
        res = []
        return recurse(root, res)

class NonRecSolution:
    def inOrder(root):
        if root is None:
            return None
        stack = []
        lst = []
        curr = root
        while True:
            if curr is not None:
                stack.append(curr)
                curr=curr.left
            elif stack:
                curr = stack.pop()
                lst.append(temp.val)
                curr = curr.right
            else:
                break
        return lst
