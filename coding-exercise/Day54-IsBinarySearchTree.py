"""
  Validate Binary Search Tree

Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

    2
   / \
  1   3

Input: [2,1,3]
Output: true
"""
class Solution:
    def isBinarySearchTreeRec(self,node,min_val,max_val):
        if node is None:
            return True
        elif node.val >= max_val or node.val<=min_val:
            return False
        else:
            return self.isBinarySearchTreeRec(node.left,min_val,node.val) and self.isBinarySearchTreeRec(node.right,node.val, max_val)

    def isBinarySearchTree(self,root):
        return self.isBinarySearchTreeRec(root,float(-inf), float(inf))