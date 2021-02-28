class Node:
    def __init__(self,val,left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def postOrderTraversalIter(root):
    if root is None: return []
    res, stack = [], [root]
    while stack:
        node = stack.pop()
        res.append(node.val)
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    return res[::-1]

def postOrder(root, res):
    if root is None:
        return
    if root.left: postOrder(root.left,res)
    if root.right: postOrder(root.right,res)
    res.append(root.val)
    return res

def postOrderTraversalRec(root):
    res =[]
    postOrder(root,res)
    return res

# Driver program to test above function 
root = Node(1)
root.right = Node(2)
root.right.left = Node(3)

print(postOrderTraversalRec(root))
print(postOrderTraversalIter(root))