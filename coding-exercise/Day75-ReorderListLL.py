"""
143. Reorder List
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example 1:
Given 1->2->3->4, reorder it to 1->4->2->3.

Example 2:
Given 1->2->3->4->5, reorder it to 1->5->2->4->3.

"""


def reorderList(head):
    """
    Do not return anything, modify head in-place instead.
    """
    if not head:
        return None

    def reverseList(prev, head):
        prevNode = prev
        currNode = head
        nextNode = None
        while head:
            currNode = head
            nextNode = head.next
            head.next = prevNode
            prevNode = currNode
            head = nextNode
        return prevNode

    # find the mid point of the list
    slow_ptr, fast_ptr = head, head
    while fast_ptr is not None and fast_ptr.next is not None:
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next.next

    # reverse the second part of the list
    second = reverseList(None, slow_ptr)
    first = head
    while second.next:
        tmp = first.next
        first.next = second
        first = tmp

        tmp = second.next
        second.next = first
        second = tmp
