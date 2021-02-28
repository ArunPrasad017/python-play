"""
Path Sum practice
"""


def recPathSum(node, target):
    res = False
    target -= node.val
    if node.left is None and node.right is None:
        return target == 0
    if node.left:
        res = res or recPathSum(node.left, target)
    if node.right:
        res = res or recPathSum(node.right, target)
    return res


def hasPathSum(root, sum_val):
    if root is None and sum_val > 0:
        return False
    return recPathSum(root, sum_val)
