# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


def isMirror(node1, node2):
    if node1 is None and node2 is None:
        return True
    if node1 is not None and node2 is not None and node1.val == node2.val:
        return isMirror(node1.left, node2.right) and isMirror(node1.right, node2.left)
    return False


def isSymmetric(root):
    if root is None:
        return True
    return isMirror(root, root)
