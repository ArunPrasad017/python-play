# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recursive(self, inorder, postorder, i1, i2, p1, p2):
        if i1 >= i2 or p1 >= p2:
            return
        root = TreeNode(postorder[p2 - 1])
        idx = inorder.index(postorder[p2 - 1])
        diff = idx - i1

        root.left = self.recursive(inorder, postorder, i1, i1 + diff, p1, p1 + diff)
        root.right = self.recursive(
            inorder, postorder, i1 + diff + 1, i2, p1 + diff, p2 - 1
        )
        return root

    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        n = len(inorder)
        if not n:
            return None
        return self.recursive(inorder, postorder, 0, n, 0, n)
