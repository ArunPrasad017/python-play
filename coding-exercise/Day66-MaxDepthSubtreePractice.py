"""
Max Depth practice
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    # max depth topdown approach
    def maxDepthRec(self, node, depth):
        if node is None:
            return
        if node.left is None and node.right is None:
            self.ans = max(depth, self.ans)
        self.maxDepthRec(node.left, depth + 1)
        self.maxDepthRec(node.right, depth + 1)
        return self.ans

    # maxdepth bottom up approach
    def maxDepthRecBottom(self, node):
        if node is None:
            return 0
        left_depth = self.maxDepthRecBottom(node.left)
        right_depth = self.maxDepthRecBottom(node.right)
        return max(left_depth, right_depth) + 1

    def maxDepth(self, root):
        if root is None:
            return None
        return self.maxDepthRec(root, depth)
