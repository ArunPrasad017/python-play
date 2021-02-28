class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummyNode = ListNode(0)
        dummyNode.next = head
        slow_ptr = dummyNode
        fast_ptr = dummyNode

        for _ in range(n):
            fast_ptr = fast_ptr.next

        while fast_ptr.next is not None:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next
        slow_ptr.next = slow_ptr.next.next
        return dummyNode.next
