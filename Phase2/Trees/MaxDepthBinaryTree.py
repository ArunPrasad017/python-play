# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxDepthRec(node,depth):
    if node.left is None and node.right is None:
        self.maxDepth = max(depth, self.maxDepth)
    if node.left:
        maxDepthRec(node.left, depth+1)
    if node.right:
        maxDepthRec(node.right, depth+1)
    return self.maxDepth


def maxDepth(root):
    if root is None:
        return None
    # as root is not none then depth by default is one
    self.maxDepth, depth = 0,1 
    return maxDepthRec(root,depth)

root = TreeNode(3)