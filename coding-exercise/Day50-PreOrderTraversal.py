"""
    Method
    a) Create a new stack/list to store the values
    b) first node of stack = root node
    c) as this implementation asks for an output result lst create that too - if not have a print statement when we pop and print the corresponding node
    d) once popped - append the value of the popped node to the result list
    e) check if node has right and left nodes. We have to append them right first then left because of the pop() operation looking for last element in stack
    f) iterate until stack eventually runs out
"""

class Node:
    def __init__(self,val,left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def preOrderTraversal(root):
    if root is None:
        return
    stack = [root]
    out = []
    while stack:
        node =stack.pop()
        out.append(node.val)
        if node.right is not None:
            stack.append(node.right)
        if node.left is not None:
            stack.append(node.left)
    return out

def preOrder(root,res):
    if root is None:
        return
    res.append(root.val)
    if root.left: preOrder(root.left, res)
    if root.right: preOrder(root.right, res)

def preOrderTraversalRec(root):
    res = []
    preOrder(root,res)
    return res
# Driver program to test above function 
root = Node(1)
root.right= Node(2)
root.right.left = Node(3)

print(preOrderTraversal(root))
print(preOrderTraversalRec(root))