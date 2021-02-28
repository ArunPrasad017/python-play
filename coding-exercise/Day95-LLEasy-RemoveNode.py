# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        slowPtr = fastPtr = dummy
        dummy.next = head
        while n > 0 and fastPtr.next:
            fastPtr = fastPtr.next
            n -= 1
        while fastPtr.next is not None:
            slowPtr = slowPtr.next
            fastPtr = fastPtr.next
        slowPtr.next = slowPtr.next.next
        return dummy.next
