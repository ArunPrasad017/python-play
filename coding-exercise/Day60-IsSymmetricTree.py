class Solution:
    def isMirror(self, root1, root2):
        if root1 is None and root2 is None:
            return True
        if root1 is not None and root2 is not None and root1.val == root2.val:
            return self.isMirror(root1.left, root2.right) and self.isMirror(root1.right, root2.left)

    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        return self.isMirror(root, root)