class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def bfsHelper(node, level, levels):
    if node is None:
        return
    if len(levels) == level:
        levels.append([])
    levels[level].append(node.val)
    if node.left:
        bfsHelper(node.left, level + 1, levels)
    if node.right:
        bfsHelper(node.right, level + 1, levels)


def levelOrderTraversalRec(root):
    if root is None:
        return
    levels = []
    bfsHelper(root, 0, levels)
    return levels


from collections import deque


def levelOrderTraversalIter(root):
    levels = []
    if root is None:
        return levels
    queue = deque(
        [
            root,
        ]
    )
    level = 0
    while queue:
        if len(levels) == level:
            levels.append([])
        level_length = len(queue)
        for _ in range(level_length):
            node = queue.popleft()
            levels[level].append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        level += 1
    return levels


# Driver program to test above function
root = Node(3)
root.left = Node(9)
root.right = Node(20)
root.right.left = Node(15)
root.right.right = Node(7)

print(levelOrderTraversalIter(root))
