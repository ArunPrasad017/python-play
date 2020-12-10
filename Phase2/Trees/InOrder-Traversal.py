# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


def traverse(root, res):
    if root.left:
        traverse(root.left, res)
    res.append(root.val)
    if root.right:
        traverse(root.right, res)


def inorderTraversal(root):
    if not root:
        return []
    res = []
    traverse(root, res)
    return res
