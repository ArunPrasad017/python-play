"""
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7

output:
[
  [3],
  [9,20],
  [15,7]
]

"""

def bfsHelper(node, level,levels):
    if len(levels) == level:
        levels.append([])
    if level%2==1:
        levels[level].insert(0,node.val)
    else:
        levels[level].append(node.val)    
    if node.left:
        bfsHelper(node.left,level+1,levels)
    if node.right:
        bfsHelper(node.right,level+1,levels)


def levelOrder(root):
    ## Recursive method
    levels = []
    if root is None:
        return levels
    bfsHelper(root,0,levels)
    return levels