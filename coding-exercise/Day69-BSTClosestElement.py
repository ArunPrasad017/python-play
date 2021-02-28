# class newNode:

#     # Constructor to create a new node
#     def __init__(self, val):
#         self.val = val
#         self.left = None
#         self.right = None


def closest(root, target):
    if root is None:
        return None
    res = root.val
    while root:
        if (root.val - target) == 0:
            return root.val
        if abs(root.val - target) < abs(res - target):
            res = root.val
        if target < root.val:
            root = root.left
        elif target > root.val:
            root = root.right
    return res
