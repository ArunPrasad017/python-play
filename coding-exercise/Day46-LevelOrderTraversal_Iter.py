"""
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7

output:
[
  [3],
  [9,20],
  [15,7]
]

"""
from collections import deque


def levelOrder(root):
    # iterative method
    levels = []
    if not root:
        return levels
    level = 0
    queue = deque(
        [
            root,
        ]
    )
    while queue:
        levels.append([])
        level_length = len(queue)
        print(level_length)
        for _ in range(level_length):
            node = queue.popleft()
            if level % 2 == 0:
                levels[level].append(node.val)
            else:
                levels[level].insert(0, node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
                print(queue)
        level += 1
    return levels
