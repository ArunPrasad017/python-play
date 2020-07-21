"""
LeetCode 203: Remove Linked List Elements

Remove all elements from a linked list of integers that have value val.

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5

done for daily challenge
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def removeElements(head,val):
    sentinel = ListNode(0)
    sentinel.next = head
    curr = head
    prev = sentinel
    while curr is not None:
        if curr.val==val:
            prev.next = curr.next
        else:
            prev = curr
        curr = curr.next
    return sentinel.next
