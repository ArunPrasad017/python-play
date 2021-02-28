"""
  Populating Next Right Pointers in Each Node

116. Populating Next Right Pointers in Each Node -TypeA
Input: root = [1,2,3,4,5,6,7]
Output: [1,#,2,3,#,4,5,6,7,#]
Explanation: Given the above perfect binary tree (Figure A), your function should populate each next pointer to point to its next right node. 
The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.

117.   Populating Next Right Pointers in Each Node II
Input: root = [1,2,3,4,5,null,7]
Output: [1,#,2,3,#,4,5,7,#]
Explanation: Given the above binary tree (Figure A), your function should populate each next pointer to point to its next right node. 
The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.

For both questions - the same result would work
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque


def connect(root):
    if root is None:
        return None
    q = deque([root])
    while q:
        size = len(q)
        for i in range(size):
            node = q.popleft()
            if i < size - 1:
                node.next = q[0]
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
    return root
