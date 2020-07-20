# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


""" use concept of sentinel or dummy node in order to solve for the issue with continous values 
and use a two ptr technique which is prev and curr node
"""
def removeElements(head,val):
    sentinel = ListNode(0)
    prev, curr = head,sentinel 
    while curr is not None:
        if curr.val == val:
            prev.next = curr.next
        else:
            prev = curr
        curr=curr.next
    return sentinel.next
