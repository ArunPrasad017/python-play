"""
  Symmetric Tree

Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3


But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isMirror(root1, root2):
    if root1 is None and root2 is None:
        return True
    if root1 is not None and root2 is not None and root1.val == root2.val:
        return isMirror(root1.left, root2.right) and isMirror(root1.right, root2.left)
    return False


def isSymmteric(root):
    return isMirror(root, root)
