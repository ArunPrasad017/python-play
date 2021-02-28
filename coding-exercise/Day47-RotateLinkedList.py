"""
Given a linked list, rotate the list to the right by k places, where k is non-negative.

Input: 1->2->3->4->5->NULL, k = 2
Output: 4->5->1->2->3->NULL
Explanation:
rotate 1 steps to the right: 5->1->2->3->4->NULL
rotate 2 steps to the right: 4->5->1->2->3->NULL

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def rotateRight(head, k):
    if k == 0 or head is None:
        return head
    # find the length of the linkedlist first - as when k>len(list) the k = k%len(list)
    cur = head
    cnt = 0
    while cur is not None:
        cnt += 1
        cur = cur.next
    k %= cnt
    if k == 0:
        return head
    # we use the two pointer along with dummy nodes in order to identify the
    dummyNode = ListNode(0)
    dummyNode.next = head
    slow_ptr, fast_ptr = dummyNode, dummyNode

    # shifting the fast ptr until k-1 so we can detach this part of the linkedlist and add it/repoint to the front
    for _ in range(k):
        fast_ptr = fast_ptr.next

    while fast_ptr is not None:
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next
    # creating a new head term to enable the rotation
    newHead = slow_ptr.next
    slow_ptr.next = None
    fast_ptr.next = head
    return newHead
