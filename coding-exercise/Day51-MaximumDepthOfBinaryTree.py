"""
  Maximum Depth of Binary Tree

Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7

return its depth = 3.

"""
class Solution:
    def maxDepthTreeRec(self,root,depth):
        if root is None:
            return
        if root.left is None and root.right is None:
            answer = max(answer,depth)
        if root.left:
            self.maxDepthTreeRec(root.left, depth+1)
        if root.right:
            self.maxDepthTreeRec(root.right, depth+1)
        return self.answer

    def maxDepthTree(self,root):
        if node is None:
            return 0
        depth =1
        self.answer = 0
        return self.maxDepthTreeRec(root, depth)
