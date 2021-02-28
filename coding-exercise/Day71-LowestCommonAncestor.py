# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        def hasPath(root, node, lst):
            if root is None:
                return
            if node.val == root.val:
                lst.append(node)
                return lst
            left = hasPath(root.left, node, lst + [root])
            right = hasPath(root.right, node, lst + [root])
            if left:
                return left
            if right:
                return right

        lst1 = hasPath(root, p, [])
        lst2 = hasPath(root, q, [])
        if not lst1 or not lst2:
            return -1
        i = 0
        if lst1 is not None and lst2 is not None:
            while i < len(lst1) and i < len(lst2):
                if lst1[i] != lst2[i]:
                    break
                i += 1
        return lst1[i - 1]
