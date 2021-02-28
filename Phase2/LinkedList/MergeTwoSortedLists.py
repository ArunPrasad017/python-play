# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(l1, l2):
    # sentinel
    l3 = ListNode(0)
    curr = l3
    while l1 and l2:
        if l1 and l1.val <= l2.val:
            curr.next = ListNode(l1.val)
            l1 = l1.next
        elif l2 and l1.val > l2.val:
            curr.next = ListNode(l2.val)
            l2 = l2.next
        curr = curr.next
    curr.next = l1 or l2
    return l3.next
