"""
Given a linked list, remove the n-th node from the end of list and return its head.

ex:
Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.

"""


def removeNthFromEnd(head, n):
    dummmynode = ListNode()
    dummmynode.next = head
    slow = dummmynode
    fast = dummmynode

    for i in range(0, n + 1):
        fast = fast.next

    while slow != None:
        slow = slow.next
        fast = fast.next

    slow.next = slow.next.next
    return dummmynode.next
