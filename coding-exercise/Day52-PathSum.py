"""
Given a binary tree and a sum, determine if the tree has a root-to-leaf path 
such that adding up all the values along the path equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathRec(self,node,target):
        target-=node.val
        res = 0
        if node.left is None and node.right is None:
            return target==0
        if node.left:
            res = res or self.hasPathRec(node.left, target)
        if node.right:
            res = res or self.hasPathRec(node.right, target)
        return res
    
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root is None and sum>=0:
            return False
        return self.hasPathRec(root, sum)