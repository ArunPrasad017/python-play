class Tree:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def isMirror(node1, node2):
    if node1 is None and node2 is None:
        return True
    if node1 is not None and node2 is not None and node1.left.val == node2.right.val:
        return isMirror(node1.left, node2.right) and isMirror(node1.right, node2.left)

def isSymmetric(self,root):
    if root is None or (root.left is None and root.right is None):
        return True
    return isMirror(root,root)