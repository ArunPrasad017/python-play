"""
LeetCode: 106
Construct Binary Tree from Inorder and Postorder Traversal
Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]

    3
   / \
  9  20
    /  \
   15   7

"""


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def binaryTreeRecursive(inorder, postorder, i1, i2, p1, p2):
    if i1 >= i2 or p1 >= p2:
        return
    root = TreeNode(postorder[p2 - 1])
    it = inorder.index(postorder[p2 - 1])
    diff = it - i1
    root.left = binaryTreeRecursive(inorder, postorder, i1, i1 + diff, p1, p1 + diff)
    root.right = binaryTreeRecursive(
        inorder, postorder, i1 + diff + 1, i2, p1 + diff, p2 - 1
    )
    return root


def binaryTree(inorder, postorder):
    n = len(inorder)
    if not n:
        return None
    return binaryTreeRecursive(inorder, postorder, 0, n, 0, n)


inorder = [9, 3, 15, 20, 7]
postorder = [9, 15, 7, 20, 3]

print(binaryTree(inorder, postorder))
