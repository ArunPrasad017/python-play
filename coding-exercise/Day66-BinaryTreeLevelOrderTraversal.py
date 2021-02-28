"""
Binary Tree Level order traversal practice
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

    3
   / \
  9  20
    /  \
   15   7

   [
  [3],
  [9,20],
  [15,7]
]
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


def levelOrderTraversal(root):
    if root is None:
        return None
    queue = deque([root])
    res = []
    level = 0
    while queue:
        if len(levels) == level:
            res.append([])
        level_length = len(queue)
        for _ in range(level_length):
            node = queue.popleft()
            res[level].append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        level += 1
    return res
