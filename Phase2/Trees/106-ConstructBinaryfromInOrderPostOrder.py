# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def buildTreeRec(inOrder, postOrder,i1,i2,p2,p2):
    if i1>=i2 or p1>=p2:
        return
    node = TreeNode(postOrder[p2-1])
    idx = inOrder.index(postOrder[p2-1])
    diff = idx-i1
    node.left = buildTreeRec(inOrder, postOrder, i1, i1+diff, p1, p1+diff)
    node.right = buildTreeRec(inOrder, postOrder, i1+diff+1, i2, p1+diff, p2-1)
    return node

def buildTree(inOrder, postOrder):
    n = len(inorder)
    if not n:
        return None
    return buildTreeRec(inOrder,postOrder,0,n,0,n)