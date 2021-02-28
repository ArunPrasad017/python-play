# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(l1, l2):
    while l1 is None:
        return l2
    while l2 is None:
        return l1

    l3 = ListNode(0)
    cur = l3
    while l1 or l2:
        if l1.val > l2.val:
            cur = l1
            l1 = l1.next
        else:
            cur = l2
            l2 = l2.next
    if l1:
        l3.next = l1
    elif l2:
        l3.next = l2
    return l3.next
