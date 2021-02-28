"""

Given a binary tree, return the vertical order traversal of its nodes values.

For each node at position (X, Y), its left and right children respectively will be at positions (X-1, Y-1) and (X+1, Y-1).
Running a vertical line from X = -infinity to X = +infinity, whenever the vertical line touches some nodes, 
we report the values of the nodes in order from top to bottom (decreasing Y coordinates).

If two nodes have the same position, then the value of the node that is reported first is the value that is smaller.
Return an list of non-empty reports in order of X coordinate.  Every report will have a list of values of nodes.

Input: [3,9,20,null,null,15,7]
Output: [[9],[3,15],[20],[7]]
Explanation: 
Without loss of generality, we can assume the root node is at position (0, 0):
Then, the node with value 9 occurs at position (-1, -1);
The nodes with values 3 and 15 occur at positions (0, 0) and (0, -2);
The node with value 20 occurs at position (1, -1);
The node with value 7 occurs at position (2, -2).

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        res = []
        if root is None:
            return result
        cache = {}
        self.min_val,self.max_val = 0, 0
        
        def dfs(node,r,c):
            if node is None:return
            if c in cache:
                cache[c].append([r,node.val])
            else:
                cache[c]= [[r, node.val]]
            self.min_val = min(self.min_val,c)
            self.max_val = max(self.max_val,c)

            dfs(node.left,r+1,c-1)
            dfs(node.right,r+1,c+1)
        
        dfs(root,0,0)
        for c in range(self.min_val, self.max_val+1):
            col = sorted(cache[c], key=lambda x:(x[0], x[1]))
            col_sorted = []
            for p in col:
                col_sorted.append(p[1])
            res.append(col_sorted)
        return res