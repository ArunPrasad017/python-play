# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

 #Preorder recursive
def traverse(node,res):
    res.append(node.val)
    if node.left:
        traverse(node.left,res)
    if node.right:
        traverse(node.right,res)

def preorderTraversal(root):
    res =[]
    if not root:
        return res
    traverse(root,res)
    return res

#iterative
def preorderTraversal(root):
    res = []
    if not root:
        return res
    stack =[root,]
    while stack:
        root=stack.pop()
        if root is not None:
            res.append(root.val)
            if root.right is not None:
                stack.append(root.right)
            if root.left is not None:
                stack.append(root.left)
    return res