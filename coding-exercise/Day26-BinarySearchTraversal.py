"""
  Binary Tree Level Order Traversal II

Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

Given binary tree [3,9,20,null,null,15,7],

res = [
  [15,7],
  [9,20],
  [3]
]
"""
class Node():
    def __init__(self,val):
        self.left = None
        self.right = None
        self.val = val

from collections import deque
def printLevelOrder(root):
    if root is None:
        return

    queue = [root]
    while queue:
        print(queue[0].val)
        node = queue.pop(0)

        if node.left is not None:
            queue.append(node.left)

        if node.right is not None:
            queue.append(node.right)

def printReverseOrder(root):
    if root is None:
        return

    queue = []
    stack = deque()
    queue.append(root)

    while queue:
        # print(queue[0].val)
        node = queue.pop(0)
        stack.append(node.val)

        if node.right is not None:
            queue.append(node.right)

        if node.left is not None:
            queue.append(node.left)
    stack.reverse()
    return list(stack)


# the below function did not work
# def levelOrderBottom(root):
#     if root is None:
#         return
    
#     res = []
#     queue = deque()
#     queue.append(root)

#     while len(queue)>0:
#         size = len(queue)
#         curr_level = []
#         for i in range(0,size):
#             node = queue.pop()
#             curr_level.append(node.val)
#             if node.left is not None:
#                 queue.append(node.left)
#             if node.right is not None:
#                 queue.append(node.right)
#         res.append(curr_level[::-1])
#     return res[::-1]


def levelOrderBottom(root):
    if root is None:
        return
    res = []
    nodes = [root]
    while nodes:
        res.append([node.val for node in nodes])
        next_nodes = []
        for node in nodes:
            if node.left is not None:
                next_nodes.append(node.left)
            if node.right is not None:
                next_nodes.append(node.right)
        nodes = next_nodes
    return res[::-1]
    
    
if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.right = Node(5)
    root.left.left = Node(4)

    # printLevelOrder(root)
    print(levelOrderBottom(root))