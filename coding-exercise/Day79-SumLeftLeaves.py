"""
404. Sum of Left Leaves
Find the sum of all left leaves in a given binary tree.
Example:

    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


def sumLeftLeavesRec(node, isLeft):
    if node.left is None and node.right is None:
        if isLeft:
            return node.val
        else:
            return 0
    else:
        total = 0
        if node.left:
            total += sumLeftLeavesRec(node.left, True)
        else:
            total += sumLeftLeavesRec(node.right, False)
    return total


def sumLeftLeaves(root):
    if root is None:
        return 0
    sumLeftLeavesRec(root, False)
