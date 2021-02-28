"""
Inorder traversal:
left -> root -> right
"""


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def InOrderTraversalIter(root):
    if root is None:
        return []
    stack, res = [], []
    curr = root
    while True:
        if curr is not None:
            stack.append(curr)
            curr = curr.left
        elif stack:
            curr = stack.pop()
            res.append(curr.val)
            curr = curr.right
        else:
            break
    return res


def inOrder(root, res):
    if root is None:
        return
    if root.left:
        inOrder(root.left, res)
    res.append(root.val)
    if root.right:
        inOrder(root.right, res)


def inOrderTraversalRec(root):
    res = []
    inOrder(root, res)
    return res


# Driver program to test above function
root = Node(1)
root.right = Node(2)
root.right.left = Node(3)

print(InOrderTraversalIter(root))
print(inOrderTraversalRec(root))
