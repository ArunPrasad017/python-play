"""
Given a binary tree, determine if it is height-balanced.

height-balanced binary tree = a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


def isBalancedDFS(root):
    if not root:
        return True, -1
    leftBalanced, leftHeight = isBalancedDFS(root.left)
    if not leftBalanced:
        return False, 0
    rightBalanced, rightHeight = isBalancedDFS(root.right)
    if not rightBalanced:
        return False, 0

    return (abs(leftHeight - rightHeight) < 2), 1 + max(leftHeight, rightHeight)


def isBalanced(root):
    return isBalancedDFS(root)[0]
