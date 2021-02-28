class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val


from collections import deque


def printLevelOrder(root):
    if root is None:
        return
    queue = []
    queue.append(root)
    while len(queue) > 0:
        print(queue[0].val)
        node = queue.pop(0)
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)


def bstToGstUtils(root, total):
    if root == None:
        return
    # recursive call for Right side sub tree
    bstToGstUtils(root.right, total)
    total += root.val
    root.val = total - root.val
    # recurring call for left side sub tree
    bstToGstUtils(root.left, total)
    return root


def bstToGst(root):
    total = 0
    bstToGstUtils(root, total)


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.right = Node(5)
    root.left.left = Node(4)

    printLevelOrder(root)
