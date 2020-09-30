def has_child(node):
    return bool(node.left or node.right)
    
def subTreeRec(node):
    if node.left is None and node.right is None:
        self.count+=1
    if node.left is not None and node.right is not None:
        if node.val == node.left.val and node.val == node.right.val:
            self.count+=1
    elif node.left is None and node.right.val==node.val and not(has_child(node.right)):
        self.count+=1
    elif node.right is None and node.left.val==node.val and not(has_child(node.left)):
        self.count+=1
    if node.left:
        self.subTreeRec(node.left)
    if node.right:
        self.subTreeRec(node.right)
    return self.count
def countUniValSubTree(root):
    self.count =0
    if root is None:
        return self.count
    subTreeRec(root)