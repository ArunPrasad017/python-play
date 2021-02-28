"""
Count Univalue Subtrees

Given a binary tree, count the number of uni-value subtrees.

A Uni-value subtree means all nodes of the subtree have the same value.

Input:  root = [5,1,5,5,5,null,5]

              5
             / \
            1   5
           / \   \
          5   5   5

Output: 4
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countUnivalSubtreesRec(self, node):
        if node.left is None and node.right is None:
            self.count += 1
            return self.count
        if node.left and node.right:
            if node.val == node.right.val and node.val == node.left.val:
                self.count += 1
        elif (
            node.left is None
            and node.right.val == node.val
            and (node.right.left is None and node.right.right is None)
        ):
            self.count += 1
        elif (
            node.right is None
            and node.left.val == node.val
            and (node.left.left is None and node.left.right is None)
        ):
            self.count += 1
        if node.left:
            return countUnivalSubtreesRec(node.left)
        if node.right:
            return countUnivalSubtreesRec(node.right)

        return self.count

    def countUnivalSubtrees(self, root):
        if root is None:
            return 0
        self.count = 0
        return self.countUnivalSubtreesRec(root)
