"""
236. Lowest Common Ancestor of a Binary Tree

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T 
                                                    that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.

Given the following binary tree:  root = [3,5,1,6,2,0,8,null,null,7,4]
"""
def lowestCommonAncestor(root, p, q):
    lst1, lst2 = [],[]
    if not(findPath(root,lst1,p)) and not(findPath(root, lst2,q)):
        return -1
    i = 0
    while i<len(lst1) and i<len(lst2):
        if lst1[i]!=lst2[i]:
            break
        i+=1
    return lst1[i-1]

def findPath(root,lst,val):
    if root is None:
        return False
    lst.append(root.val)
    if root.val == val:
        return True
    if (root.left is not None and findPath(root.left, lst, val)) or \
        (root.right is not None and findPath(root.right, lst,val)):
        return True
    lst.pop()
    return False


 # LeetCode approach
def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode': 
    def findPath(root,node,lst):
        if root is None:
            return []
        if node.val == root.val:
            lst.append(node)
            return lst
        left = findPath(root.left, node, lst+[root])
        right = findPath(root.right, node, lst+[root])
        if left:
            return left
        if right:
            return right
        
    lst1 = findPath(root,p,[])
    lst2 = findPath(root,q,[])    
    if not lst1 and not lst2:
        return -1
    i = 0
    while i<len(lst1) or i<len(lst2):
        if lst1[i]!=lst2[i]:
            break
        i+=1
    return lst1[i-1]