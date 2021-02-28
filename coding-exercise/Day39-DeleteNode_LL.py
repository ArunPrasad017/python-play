# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
"""
The usual way of deleting a node node from a linked list is to modify the next pointer of the node before it, to point to the node after it.

Since we do not have access to the node before the one we want to delete, we cannot modify the next pointer of that node in any way. 
Instead, we have to replace the value of the node we want to delete with the value in the node after it, and then delete the node after it.
"""


def deleteNode(node):
    if node is None:
        return
    else:
        temp = node.next
        node.val = temp.val
        node.next = temp.next
