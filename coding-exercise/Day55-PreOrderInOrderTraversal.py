"""
Construct Binary Tree from Inorder and Postorder Traversal

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]

    3
   / \
  9  20
    /  \
   15   7
"""
class Solution:
    def buildTreeRec(self,preorder,inorder, i1, i2, p1, p2):
        if i1>=i2 or p1>=p2:
            return
        val = preorder.pop(0)
        root = TreeNode(val)
        idx = inorder.index(val)
        diff = idx - i1
        
        root.left = self.buildTreeRec(preorder,inorder,i1,i1+diff, p1, p1+diff)
        root.right = self.buildTreeRec(preorder,inorder,i1+diff+1,i2, p1+diff+1, p2)
        return root
    
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        n = len(inorder)
        if not n:
            return None
        return self.buildTreeRec(preorder, inorder,0,n,0,n)