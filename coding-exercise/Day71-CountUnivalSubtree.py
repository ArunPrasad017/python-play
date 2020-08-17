# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recur(self,node):
        def hasChild(node):
            if node.left or node.right:
                return True
            return False     
        if node.left is None and node.right is None:
            self.count+=1
            return self.count
        if node.left is not None and node.right is not None:
            if node.left.val == node.val and node.right.val==node.val:
                self.count+=1
        elif node.left is None and node.right.val == node.val and not(hasChild(node.right)):
            self.count+=1
        elif node.right is None and node.left.val == node.val and not(hasChild(node.left)):
            self.count+=1
        if node.left:
            self.recur(node.left)
        if node.right:
            self.recur(node.right)
        return self.count
    
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        if root is None:
            return 0
        self.count = 0
        return self.recur(root)