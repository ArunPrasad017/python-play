#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def inorderRec(node, lst):
    if node.left:
        inorderRec(node.left, lst)
    if node is not None:
        lst.append(node.value)
    if node.right:
        inorderRec(node.right, lst)
    return lst


def kthSmallestInBST(t, k):
    if t is None or k < 1:
        return 0
    # inorder traversal
    lst = inorderRec(t, [])
    return lst[k - 1]
