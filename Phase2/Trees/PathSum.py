def hasPathSumRec(node, tgt):
    res = False
    tgt-=node.val
    if node.left is None and node.right is None:
        return tgt == 0
    if node.left:
        res = res or self.hasPathSumRec(node.left, tgt)
    if node.right:
        res = res or self.hasPathSumRec(node.right, tgt)
    return res

def hasPathSum(tgt,root):
    if root is None:
        return None
    hasPathSumRec(root, tgt)